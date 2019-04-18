import socket
import threading

class ThreadedServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket()
        self.sock.bind((self.host, self.port))

        self.LIST_SIZE = 10
        self.listCode = ["XY123", "AB098", "QW456"]
        self.listStatus = ["arrival", "arrival", "departure"]
        self.listTime = ["00:00", "01:00", "02:00"]

    def listen(self): 
        self.sock.listen() #listening/waiting to recieve a connection
        print('Listening...')
        while True:
            client, address = self.sock.accept() #accepts the requst
            print('Accepted!')
            threading.Thread(target = self.protocol,args = (client,address)).start() #starts a new thread for every connection recieved from the client

    def protocol(self, client, address):
        buffer_size = 1024
        while True:
            try:
                data = client.recv(buffer_size) #recieve data from client
                if data:
                    data = data.decode()
                    print('Data received by server: ', data)
                    separatedData = data.split(",") #separates data into a list

                    if separatedData[0] == "read" :
                        print('Action => read')
                        try:
                            i = self.listCode.index(separatedData[1]) #returs the index of the element whose code is equal to the code recieved from the client
                            response = self.listCode[i] + "," + self.listStatus[i] + "," + self.listTime[i] #puts the whole information in the response string
                        except:
                            response = "Code not found in the list"
                        print('Response to be sent: ', response)

                    elif separatedData[0] == "write" :
                        print('Action => write')
                        if len(self.listCode) > self.LIST_SIZE : #in order to keep the list size
                            self.listCode.pop(0) #removes the element from the left side of the list
                            self.listStatus.pop(0)
                            self.listTime.pop(0)
                        print('Appending...')
                        self.listCode.append(separatedData[0]) #Add recieved data to the right side of the list
                        self.listStatus.append(separatedData[1])
                        self.listTime.append(separatedData[2])
                        print('Action: ', separatedData[0], ' Status: ', separatedData[1], ' Time: ', separatedData[2])
                        print('Putting ' + data
                                      + ' : ' + str(len(self.listCode)) + ' items in queue')
                        response = "Written successfully"

                    try:
                        response = response.encode('utf-8')
                        client.send(response)
                    except:
                        print('Failed to send response: ', response)
                else:
                    raise print('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":

    port_num = 1234
    ThreadedServer('',port_num).listen() #localhost in port 1234
