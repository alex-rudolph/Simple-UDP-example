## Alexander Rudolph
## William Cervantes
## Zosimo Geluz

import socket
import sys

class Car(object):
    ##  This is the definition for Cars
    ## contains info for:  Manfacturer, Model, Color, Year, and Condition

    def __init__(self, manufacturer, model, color, year, condition):
        # initialize the parameters for a new Car
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.year = year
        self.condition = condition

        #didn;t really need these, but they are here nonetheless
    def return_manufacturer(self):
        return self.manufacturer

    def return_model(self):
        return self.model

    def return_color(self):
        return self.color

    def return_year(self):
        return self.year

    def return_condition(self):
        return self.condition

    def print_car(self):
        return self.manufacturer + ' ' + self.model + ' ' + self.color + ' ' + self.year + ' ' + self.condition

##car1 = Car('Ford', 'Mustang', 'Orange', '1997', 'Used')
## print(car1.manufacturer)

##Car.print_car(car1)


#create some cars to fill the dealership with
# is a default list for test purposes

car1 = Car('Ford', 'Mustang', 'Orange', '1997', 'Used')
car2 = Car('Honda', 'Civic', 'Blue', '2015', 'New')
car3 = Car('Honda', 'CR-V', 'Brown', '2006', 'Used')
car4 = Car('BMW', '3-Series', 'Red', '2016', 'New')
car5 = Car('Chevrolet', 'Traverse', 'Silver', '2016', 'New')
car6 = Car('Chevrolet', 'Impala', 'Blue', '2015', 'Used')
car7 = Car('Toyota', 'Tacoma', 'Silver', '2014', 'Used')
car8 = Car('Toyota', '4Runner', 'Silver', '2009', 'Used')
car9 = Car('Ford', 'F-150', 'Green', '2017', 'New')
car10 = Car('Jeep', 'Grand-Cherokee', 'Blue', '2016', 'New')

# populate a list with the cars
carsInStock = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]

# An example of hopw to print a car object
# Car.print_car(carsInStock[2])

## client_car = 'Blue'  ## to be filled in with client's query

def search(attr):
    car_list = ""
    count = 0 ## also used to check if search failed
    attr.remove('search')

    for temp in carsInStock:
        if all(s in str.lower(Car.print_car(temp)) for s in attr):
            ##print("YES!!!")
            count = count + 1
            car_list += str(count) + ') ' + str(Car.print_car(temp)) + '\n'

    if count == 0:
        sock.sendto("SEARCH FAILED" , address)
    else:
        sock.sendto(car_list , address)


def sell(carToSell):
    if len(carToSell) < 6:
        return -1
        sock.sendto("ERROR" , address)
    else:
        temp = Car(carToSell[1], carToSell[2], carToSell[3], carToSell[4], carToSell[5])
        carsInStock.append(temp)
        sock.sendto("SOLD" , address)
        print('[' + str(Car.print_car(temp)) + ']' + " was added")

def buy(carToBuy):
    if len(carToBuy) < 6:
        return -1
        sock.sendto("ERROR" , address)
    else:
        sellCar = Car(carToBuy[1], carToBuy[2], carToBuy[3], carToBuy[4], carToBuy[5])
        # print(str(Car.print_car(sellCar)))
        chk_num = 0
        for temp in carsInStock:
            if str.lower(Car.print_car(sellCar)) == str.lower(Car.print_car(temp)):
                carsInStock.remove(temp)
                chk_num = 1
                print('[' + str(Car.print_car(temp)) + ']' + " was sold")
        if chk_num == 1:
            sock.sendto("PURCHASED" , address)
        else:
            sock.sendto("NO CAR AVAILABLE" , address)


def display():
    # vprint 'Displaying all cars:'
    car_list = ""
    count = 0
    for temp in carsInStock:
        # temp.print_car()
        count = count + 1
        car_list += str(count) + ') ' + str(Car.print_car(temp)) + '\n'

    if count == 0:
        sock.sendto("SEARCH FAILED" , address)
    else:
        sock.sendto(car_list , address)

#display()
#search('Blue')

## begin server compenents
HOST = 'localhost'
PORT = 7000

try :
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'SOCKET CREATED'
except socket.error, msg :
    print 'Failed to create socket.  Error Code: ' + str(msg[0]) + ' Message '
    sys.exit()

try:
    sock.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code: ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print('Socket bind completed')

# wait for and respond to the client's request.  Only exit or a system failure
# will exit the program
while True:

    #connect to the socket and bind
    d = sock.recvfrom(4096)
    data = d[0]
    address = d[1]
    #  translate to all lowercase.  Makes it easier on the user when entering queries
    data = str.lower(data)


    if data == 'exit':
        break

        ## search for any car
    elif 'search' in data:
        print('Client is searching...')
        srch_msg = data.split(" ")
        ## print srch_msg[1]
        search(srch_msg)
        #search('Blue')

    # Client sells a car.  It is added to the carsInStock list
    elif 'sell' in data:
        print('Client is selling...')
        sell_msg = data.split(" ")
        sell(sell_msg)

    # Client buys a car. It is removed from the carsInStock list
    elif 'buy' in data:
        print('Client is buying...')
        buy_msg = data.split(" ")
        buy(buy_msg)

    elif 'display' in data:
        print('Displaying all cars...')
        display()

    # Displayed in case client does not enter correct input
    else:
        sock.sendto("Wrong input, re-enter message: " , address)
print("Closing Socket")
sock.close()
