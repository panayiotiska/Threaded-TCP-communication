import socket
import threading
import time

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.BUFFER_SIZE = 1024
        self.socket = socket.socket()

    def Writer(self):
        ACTION = "write"
        DATA = "DF111,departure,03:10" #dummy data for illustration (will write the same data again and again)

        data = ACTION + "," + DATA
        print('Data sent: ', data)
        self.socket.send(data.encode('utf-8')) #sends the data
        dataFromServer = self.socket.recv(self.BUFFER_SIZE) #recieves a reply from the server (WOK)
        dataFromServer = dataFromServer.decode()
        time.sleep(5) #writer is been set to need more time to finish his action
        print ("received data:", dataFromServer)

    def Reader(self):
        ACTION = "read"
        DATA = "DF111" #A code of a specific flight (dummy data for illustration)

        data = ACTION + "," + DATA
        self.socket.send(data.encode('utf-8')) #sends the data
        dataFromServer = self.socket.recv(self.BUFFER_SIZE) #recieves a reply with the information asked for by code
        dataFromServer = dataFromServer.decode()
        time.sleep(2)
        print ("received data:", dataFromServer)

    def connect(self):

        self.socket.connect((self.host, self.port)) #connects to localhost in port 1234
        while True:
            print('Connected to: ', self.host, 'in port: ', self.port)
            w = threading.Thread(target=self.Writer) #assign thread for writing(run the Writer method)
            w.start()
            time.sleep(3)
            r = threading.Thread(target=self.Reader) #assign thread for reading(run the Reader method)
            r.start()
            time.sleep(3)

if __name__ == '__main__':
    port_num = 1234
    c = Client('localhost', port_num)
    c.connect()
