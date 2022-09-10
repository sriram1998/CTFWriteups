#nc neoannophobia.chal.imaginaryctf.org 1337

import socket
import time
import re

hostname = 'neoannophobia.chal.imaginaryctf.org'
port = 1337

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

winning_months = {20: "January", 21: "February", 22: "March", 23: "April", 24: "May", 25: "June", 26: "July", 27: "August", 28: "September", 29: "October", 30: "November", 31: "December"}
winning_dates = {"January": 20, "February": 21, "March": 22, "April": 23, "May": 24, "June": 25, "July": 26, "August": 27, "September": 28, "October": 29, "November": 30, "December": 31}
losing_tuples = [("January",20), ("February",21), ("March",22), ("April",23), ("May",24), ("June",25), ("July",26), ("August",27), ("September",28), ("October",29), ("November",30), ("December",31)]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))
time.sleep(.5)
prev_date = 0
while 1:
    data = s.recv(1024).decode().split("\n")

    time.sleep(0.5)

    print("computer input ", data)

    month = ''
    date = 0

    for i in data:
        if i.split(" ")[0] == 'You':
            prev_date = 0
        if i.split(" ")[0] in months:
            month = i.split(" ")[0]
            date = int(i.split(" ")[1])
            
    time.sleep(0.2)

    print(month, date)

    if date == 0 or month == '':
        continue

    if (month, date) in losing_tuples:
        input = month + " " + str(date+1) + "\n"
        prev_date = date+1
        print("sending " + input)
        s.send(input.encode())
        continue

    if date == prev_date and date != 0:
        date = winning_dates[month]
        prev_date = date
        input = month + " " + str(date) + "\n"
        print("sending " + input)
        s.send(input.encode())
        continue


    if date < 20 and date != 0:
        print("sending January 20")
        prev_date = 20
        s.send(b'January 20\n')
        continue
    
    else:
        month = winning_months[date]
        input = month + " " + str(date) + "\n"
        prev_date = date
        print("sending " + input)
        s.send(input.encode())
        continue

#ictf{br0ken_game_smh_8b1f014a}
        


