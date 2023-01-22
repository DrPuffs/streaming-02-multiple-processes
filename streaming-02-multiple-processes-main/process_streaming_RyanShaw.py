"""

Streaming Process - port 9999

First we need a fake stream of data. 

We'll use the temperature data from the batch process.

But we need to reverse the order of the rows 
so we can read oldest data first.

Important! We'll stream forever - or until we 
           read the end of the file. 
           Use use Ctrl-C to stop.
           (Hit Control key and c key at the same time.)

Explore more at 
https://wiki.python.org/moin/UdpCommunication

"""

import csv
import socket
import time

host = "localhost"
port = 9999
address_tuple = (host, port)

# use an enumerated type to set the address family to (IPV4) for internet
socket_family = socket.AF_INET 

# use an enumerated type to set the socket type to UDP (datagram)
socket_type = socket.SOCK_DGRAM 

# use the socket constructor to create a socket object we'll call sock
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# read from a file to get some fake data
input_file = open("C:\\Users\\User\\Desktop\\streaming-02-multiple-processes-main\\players.csv", "r")

# use the built0in sorted() function to get them in chronological order
reversed = sorted(input_file)

# create a csv reader for our comma delimited data
reader = csv.reader(reversed, delimiter=",")

output_file = open("C:\\Users\\User\\Desktop\\streaming-02-multiple-processes-main\\out9.txt", "w")

x = 0


    
for row in reader:
    # read a row from the file
    tag, game, characters  = row

    # use an fstring to create a message from our data
    # notice the f before the opening quote for our string?
    fstring_message = f"[{tag} plays {game} and their main characters are: {characters}]"

    print(fstring_message)

    with open("C:\\Users\\User\\Desktop\\streaming-02-multiple-processes-main\\out9.txt", "a") as output_file:
            
        output_file.write(fstring_message)
        output_file.write('\n')
        x += 1

        if x > 9:
            break


         
            

    # sleep for a few seconds
    time.sleep(3)
