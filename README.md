# Threaded-TCP-communication

**A TCP communication between a Server and a Client using threads to demonstrate python's thread-safety.**

Practically it is a simple Flight-Table in an airport.<br/>
The Client uses a reader and a writer function asking the server to make a connection.<br/>
Afterwards different threads can read a record or write a new one at the same table (list inside the server).<br/>
We can see how well python handles this in order to avoid any conflicts.<br/>

## This image will help you better understand the problem : 

![alt text](https://i.imgur.com/BRa78TS.png)
