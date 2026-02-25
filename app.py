from flask import Flask, Response

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
def catch_all(path):
    return Response('Hello, World!\n', status=200, content_type='text/plain')


@app.errorhandler(405)
def method_not_allowed(e):
    return Response('Hello, World!\n', status=200, content_type='text/plain')


if __name__ == '__main__':
    hostname = '127.0.0.1'
    port = 3000
    print(f'Server running at http://{hostname}:{port}/')
    app.run(host=hostname, port=port)
