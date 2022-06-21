# Client-Server-Model
## Overview

- This project is a client-server based model, where they perform some operations on random generated data. These operations and results are shown by RESTful API. Multiple clients can request to server so have used lock method to avoid racing conditions due to multiple threads. 


## Working 

### Details

- Basically, a client sends some random generated array to server, and server returns a sorted array, over which operations like - get_array, add value to array and clear the array can be performed as well and displayed through REST API using flask. Racing conditions due to multithreading is handled using lock method. We can run multiple clients. 

### Client 

-  The client is configured to connect to the server. It will create some random integer array using function, the size of the array is kept between 10-20 (randomly chosen), and is send to server. Then it waits for server's response, to return array after few operations like sorting, adding new value or deleting the array. If the server successfully returns a sorted array, the work is done and connection is closed. 

### Server

- The server and client has socket connection. The server maintains a global internal array of intergers. The constraint on this array is - it should remain sorted in increasing order, at any time. After every request from client, the array will be filled by numbers, or the add_value and the array is empty when server first fires up. The server should be always-on and accepting new client connection. After returning the sorted array back to client, the connection is closed by client. The server is able to handle multiple client connections using lock concept and multithreading. The server shows response through REST API.

### REST API

- After the socket connection with the client(s), the server exposes a RESTful API and offers these three operations:
- Clean_array: a DELETE request, so that all the integers from the server's array
- Get_array: a GET request, it will respond to server's array
- Add_value: a POST request, it will add an integer to the server's array (a random integer)
- It is implemented using flask.

### Additional Task

- Socket Programing with some basic  operations on data and RESTful API using flask.

## How to run the project?

- Clone the repo to your local machine and change the localhost address
- Install - flask and sortedcontainers
- Run server then client

## Screenshots



## My learning

- Socket programming in python
- Flask and RESTful API
- Multithreading and syncronisation of threads using Mutex

## Reference

1. https://www.geeksforgeeks.org/socket-programming-python/ 
2. https://www.geeksforgeeks.org/multithreading-python-set-1/



