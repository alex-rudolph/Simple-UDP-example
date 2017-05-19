## Alexander Rudolph
## William Cervantes
## Zosimo Geluz

import socket
import sys

# check and make sure connection is stable
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

except socket.error:
    print 'Failed to create socket'
    sys.exit()

host = 'localhost';
port = 7000;

#menu that displays available commands
menu = 'Displaying current menu: \n\
	-To search for a model, enter\n\
		1) \'search\':\
			a) Enter keyword(s): manufacturer, model, color, year, or condition(new/used)\n\
			\n\
	-To sell a car, enter: \n\
		2) \'sell\': \n\
			a) All:  format is --> manufacturer, model, color, year.\n\
		\n\
	-To display all available models, enter: \n\
		3) \'display\': \n\
		\n\
	-To purchase a car, enter: \n\
		4) \'purchase\': \n\
			a) manufacturer, model, color, year, condition\n\
            \n\
	-To exit, enter: \n\
		5) \'exit\' \n\
        \n\
        -To see menu again, enter: \n\
                6) \'menu\' \n '

print(menu)

while(1) :
    msg = raw_input('Enter message to send : ')
    msg = str.lower(msg)

    if msg == 'exit':
        print("Closing Socket")
        sock.sendto(msg, (host, port))
        break
    if msg == 'menu':
        print(menu)
    else:
        try :

            sock.sendto(msg, (host, port))

            ##listen for 2 seconds before timeout and error message
            sock.settimeout(2)
            d = sock.recvfrom(1024)
            reply = d[0]
            addr = d[1]

            print 'Server reply : \n' + reply

        except socket.error, msg:
            print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
