from twilio.rest import Client
import bs4 as bs
import urllib.request
import datetime
import schedule
import time
from selenium import webdriver
from pygame import mixer # Load the required libraries

account_sid = "your account id here"# To place a call using a rented phone number on twilio
auth_token = "your token number here"
client = Client(account_sid, auth_token)
def call():
    call = client.calls.create(
    to = "your phone number here",
    from_ = "your twilio account's phone number",
    url = "http://demo.twilio.com/docs/voice.xml"
    )


seconds_hms = [3600, 60, 1]
print("Enter the time in minutes that you would like to be woken before")#To get the number of minutes before arrival the user wants to be woken up before
min_before = int(input())


def check():
    sauce = urllib.request.urlopen(url).read()#Request to the particular
    soup = bs.BeautifulSoup(sauce, 'lxml')#create it to bs object

    c = 0
    l = []
    for rows in soup.find_all('td'):
        l.append(rows.text)#Appending soup as list

    for i in range(len(l)):
        if destination in l[i]:#Finding destination in the list
            station_details = l[i: i + 5]
            print(l[i:i+5])# Printing the destination

    eta = ''
    eta_etd = station_details[-1]
    c = 0
    for i in range(len(eta_etd)):
        if eta_etd[i] == ":":
            while c <= 6:
                eta += eta_etd[i + c + 2]
                c += 1
            
    am_pm = eta[-1]
    eta = eta[:-1].strip()# Getting ETA
    eta_hms = [int(t) for t in eta.split(':')]
    if am_pm == 'P' and eta[0] != 12:
        eta_hms[0] += 12#Adding 12 if the time is post 12 noon
    secs_eta = 3600 * eta_hms[0] + 60 * eta_hms[1]
    if secs_eta < 0:
        secs_eta += 86400
    return secs_eta


secs_eta = 0

print("Enter you destination code")#Getting the destination
destination = input()
print("Enter your train number")#Getting the train number
train_no = input()
print("When did you board the train? Was is today or yesterday?")#Asking for day of boarding
day = input()
url = "https://runningstatus.in/status/"+ train_no + '-' + day#url to be called

check()

def ring():
    time_now = datetime.datetime.now()
    current_secs = sum([a * b for a, b in zip([time_now.hour, time_now.minute, time_now.second], seconds_hms)])
    secs_eta = check()
    if secs_eta < current_secs:
        secs_eta += 86400
        
    if (secs_eta - current_secs) <= (min_before* 60):#If the time remaining is less than equal to that desired by the user
        call()#Calls the user
        
schedule.every(50).seconds.do(ring)#Checks for the train's details every 50 seconds
while True:
    schedule.run_pending()
    time.sleep(1)





