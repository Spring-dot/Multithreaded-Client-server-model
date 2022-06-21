# Client-Server-Model
## Overview

- This project is a client-server based model, where they perform some operations on random generated data. These operations and results are shown by RESTful API. Multiple clients can request to server so have used lock method to avoid racing conditions due to multiple threads. 


## Working 

### Details

- Basically, a client sends some random generated array to server, and server returns a sorted array, over which operations like - get_array, add value to array and clear the array can be performed as well and displayed through REST API using flask. Racing conditions due to multithreading is handled using lock method. We can run multiple clients. 

### Client 

-  The client is configured to connect to the server. It will create some random integer array using function, the size of the array is kept between 10-20 (randomly chosen), and is send to server. Then it waits for server's response, to return array after few operations like sorting, adding new value or deleting the array. If the server successfully returns a sorted array, the work is done and connection is closed. 

### Server

- 
### REST API

-
### Additional Task

-

## How to run the project?

## Screenshots

## Demo Video

## Reference

