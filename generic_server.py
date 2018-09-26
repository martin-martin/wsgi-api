# Python's bundled WSGI server
from wsgiref.simple_server import make_server
import inventory


encoding = 'utf-8'  # set the encoding
port = 8000  # set port
my_obj = inventory.MyApp()  # create object of MyApp


def application(environ, start_response):

    try:
        # checkup
        response_list = [f'{key}: {value}'
                            for key, value
                            in sorted(environ.items())]
        response_body = '\n'.join(response_list)

        # response_body = my_obj.dispatch(environ)
        status = '200 OK'  # set HTTP Status
    except Exception as e:
        response_body = ''
        status = "500 Internal Server Error"  # set HTTP Status

    # create HTTP Headers
    headers = [('Content-Type', f'text/plain; charset={encoding}'),
               ('Content-Length', str(len(response_body)))]
    # sending to the server, using in-built function
    start_response(status, headers)

    # return the body wrapped in an iterable (here we use a list)
    return [response_body.encode('utf-8')]


httpd = make_server('localhost',
                    port,
                    application)

print(f"Serving on port {port}...")

# Serve until process is killed
httpd.serve_forever()
