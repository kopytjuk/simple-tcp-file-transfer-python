# Simple file transfer over TCP

Client and server implementatations for a simple file transfer service over TCP/IP in Python.

## Server

A server has to be started first with a port (e.g. 4243) which is open for connections:

```shell
python server.py 4243
```

## Client

A client requests a file from a server `localhost` and port `4243`

```shell
python client.py localhost 4243 hello.txt
```
