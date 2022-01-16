#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import pywhatkit
import csv
import datetime
import emoji

def send_message(contact, message):
    pywhatkit.sendwhatmsg_instantly(contact, message, 15, True, 3)

def readFile():
    now = datetime.datetime.now()
    n = datetime.datetime(now.year, now.month, now.day)
    with open('contacts.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for line in csvFile:
            day = int(line['day'])
            month = int(line['month'])
            birthday = datetime.datetime(now.year, month, day)
            if(n == birthday):
                name = line['name']
                message = emoji.emojize(f"Happy Happy Birthday {name}! :partying_face: :birthday_cake: :party_popper: :confetti_ball: :balloon:")
                contact = line['phone']
                send_message(contact,message)
                
if __name__ == '__main__':
    readFile()