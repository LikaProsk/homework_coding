import re
import socket
from http import HTTPStatus

MAX_PACKET = 32768
HOST = '127.0.0.1'
PORT = 8080


def normalize_line_endings(s):
    return ''.join((line + '\n') for line in s.splitlines())


def get_status(request_uri):
    res_search = re.search(r'status\=(\d+)', request_uri)
    return 200 if res_search is None else int(res_search.groups()[0])


def validate_status(request_uri):
    status = get_status(request_uri)
    list_status = list(HTTPStatus)
    if status in list_status:
        status = [s for s in list_status if s == status][0]
        return status.value, status.phrase
    else:
        status = 200
        status_phrase = 'OK'
    return status, status_phrase


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    while True:
        client_sock, client_addr = server_socket.accept()

        request = client_sock.recv(MAX_PACKET).decode('utf-8')
        request_head, request_body = normalize_line_endings(request).split('\n\n', 1)

        request_head = request_head.splitlines()
        request_headline = request_head[0]
        request_headers = '\n'.join([x for x in request_head[1:]])
        request_method, request_uri, request_proto = request_headline.split(' ', 3)

        status, status_phrase = validate_status(request_uri)
        send_response(client_addr, client_sock, request_headers, request_method, status, status_phrase)

        client_sock.close()


def send_response(client_addr, client_sock, request_headers, request_method, status, status_phrase):
    response_body = f'Request Method: {request_method}\n' \
                    f'Request Source: {client_addr}\n' \
                    f'Response Status: {status} {status_phrase}\n' \
                    f'{request_headers}'
    response_headers = {
        'Content-Type': 'text/plain; encoding=utf8',
        'Connection': 'close',
    }
    response_headers_raw = ''.join(f'{k}: {v}\n' for k, v in response_headers.items())
    client_sock.send(f'HTTP/1.1 {status} {status_phrase}'.encode('utf-8'))
    client_sock.send(response_headers_raw.encode('utf-8'))
    client_sock.send('\n'.encode('utf-8'))
    client_sock.send(response_body.encode('utf-8'))


if __name__ == '__main__':
    server_program()
