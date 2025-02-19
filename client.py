import argparse
import socket

BUFFER_SIZE = 16


def main():
    parser = argparse.ArgumentParser(
        description="Simple command line application.")
    parser.add_argument('address', type=str, help='Address to use')
    parser.add_argument('server_port', type=str, help='Address to use')
    parser.add_argument('filename', type=str, help='Filename to use')

    args = parser.parse_args()

    server_address = socket.gethostbyname(args.address)
    server_port = int(args.server_port)
    file_name = args.filename

    # Create a TCP/IP socket
    socket_kind = socket.SOCK_STREAM  # TCP socket
    sock = socket.socket(socket.AF_INET, socket_kind)

    server_address = (server_address, server_port)
    sock.connect(server_address)

    print(f"Address provided: {args.address}")
    print(f"Filename provided: {args.filename}")

    # send the file name to the server
    sock.sendall(file_name.encode() + b'\x00')

    # receive the requested file
    data = b''
    while True:

        data_chunk: bytes = sock.recv(BUFFER_SIZE)  # blocking

        if not data_chunk:
            # returned empty bytes object indicates that the server has disconnected
            break

        data += data_chunk

    print("File contents:", data.decode())


if __name__ == "__main__":
    main()
