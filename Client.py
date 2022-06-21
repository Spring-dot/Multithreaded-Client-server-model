import socket
import random
# pickle module for data Serialisation/De-Serialisation
import pickle
import os
import sys


def main():

    host = ""
    try:
         host = "localhost"
        # host = os.environ["http://192.168.1.75:12345/"]
    except KeyError:
        print('Provide correct IP Address')

        sys.exit(1)

    # Port on which connection is to be established

    port = 6000

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to server on local machine
        print('TCP-Client: host=', host, 'port=', port)
        s.connect((host, port))

        while True:

            try:
                # <------------ Generate Random array to be sent to server ----------->
                arr = []
                # Generate random size between 10 and 20
                random_size = random.randint(10, 20)

                for i in range(0, random_size):
                    arr.append(random.randint(0, 100))
                print('TCP Client: Random array to be sent to Server, Size:', str(random_size), ' Array:', str(arr))

                # <------------ Send random int array to TCP-Server ----------->
                # Serialise (convert) the array to byte stream before sending to server
                data_stream = pickle.dumps(arr)
                print('DEBUG:data_stream', data_stream)
                # Send serialised byte stream to server
                s.sendall(data_stream)

                # Sorted accumulated byte stream received from TCP-Server
                data = s.recv(1024)
                print('DEBUG:data', data)

                # De-Serialise (Re-convert) the byte stream into array after receiving from server
                sorted_int_arr = pickle.loads(data)

                print('TCP Client: Received from Server, New Size:', len(sorted_int_arr), 'New Sorted Array:', sorted_int_arr)

                yes_no = input('\nClient: Do you want to send more data to Server? (y/n) : ')
                if yes_no == 'y':
                    continue
                else:
                    break
            except:
                print('TCP Client: Exception thrown while processing data to be sent to server, processing next data...')

    except socket.error:
        print('TCP Client: Socket Creation Failed, Check if TCP Server has been started, then start client again...')

    finally:
        # Close the connection to TCP-Server
        s.close()


if __name__ == '__main__':
    main()