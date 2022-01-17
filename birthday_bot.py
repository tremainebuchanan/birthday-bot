#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import pywhatkit
import csv
import datetime
import emoji

def send_message(contact, message):
    pywhatkit.sendwhatmsg_instantly(contact, message, 15, True, 3)

def is_birthday_today(day, month):
    now = datetime.datetime.now()
    birthday = datetime.datetime(now.year, month, day)
    today = datetime.datetime(now.year, now.month, now.day)
    return today == birthday

def start():
    filename = "contacts.csv"
    csvFile = False
    try:
        with open(filename, mode='r') as file:
            csvFile = csv.DictReader(file)
            for line in csvFile:
                name = line['name']
                try:
                    day = int(line['day'])
                    month = int(line['month'])
                    if is_birthday_today(day, month):
                        message = emoji.emojize(f"Happy Happy Birthday {name}! :partying_face: :birthday_cake: :party_popper: :confetti_ball: :balloon:")
                        contact = line['phone']
                        send_message(contact,message)
                except:
                        print(f"Birthday for {name} was invalid")
    except FileNotFoundError:
        print(f"Unable to open {filename}")

if __name__ == '__main__':
   start()