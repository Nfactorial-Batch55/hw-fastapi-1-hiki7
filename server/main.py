def app(environ, start_response):
    path = environ.get('PATH_INFO')
    method = environ.get('REQUEST_METHOD')

    if method == 'GET' and path == '/ping':
        data = b"pong\n"
        start_response(
            "200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
        )
        return iter([data])
    elif method == 'GET' and path == '/info':
        data = f"Method: {method}\nURL: {environ.get('PATH_INFO')}\nProtocol: {environ.get('SERVER_PROTOCOL')}\n".encode('utf-8')
        start_response(
            "200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
        )
        return iter([data])
    else:
        data = b"Not Found\n"
        start_response(
            "404 Not Found", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
        )
        return iter([data])
