import argparse
import socket

BUFFER_SIZE = 32
MAX_NUM_OF_CONNECTIONS = 10


def main():
    parser = argparse.ArgumentParser(
        description="Simple command line application.")
    parser.add_argument('port', type=int, help='Port number to use')

    args = parser.parse_args()

    port = int(args.port)

    # Create a TCP/IP socket
    socket_kind = socket.SOCK_STREAM  # TCP socket
    sock = socket.socket(socket.AF_INET, socket_kind)

    server_address = ('localhost', port)
    sock.bind(server_address)

    print(
        f"Server listening at '{server_address[0]}' on port {server_address[1]}")

    sock.listen(MAX_NUM_OF_CONNECTIONS)

    while True:

        # blocking call, if there are no connections
        connection, client_addr = sock.accept()
        print("Incoming connection from:", client_addr)

        # receive the file path requested from the client
        file_name_bytes = b''
        while True:
            data_chunk: bytes = connection.recv(BUFFER_SIZE)

            # last byte indicates that the file name is transmitted
            if data_chunk[-1] == 0x00:
                file_name_bytes += data_chunk[:-1]
                break

            file_name_bytes += data_chunk

        print(f"Requested file path: {file_name_bytes.decode()}")

        # open file and read all file contents at once
        file_path = file_name_bytes.decode()
        with open(file_path, 'r') as file:
            file_contents = file.read()

        # send the file contents to the client
        connection.sendall(file_contents.encode())
        print("File sent!")

        # closes the connection
        connection.close()


if __name__ == "__main__":
    main()
