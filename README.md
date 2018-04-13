# SmartAlarm
A smart alarm which helps a passenger travelling by Indian Railways in customizing his/her alarm based on the train's E.T.A. .

A Python based script which asks the user for the minutes before the arrival of their train at their destination they would like to be woken- up before,
the station code and their day of boarding.

After getting the desired time-before-arrival, the station code and the date of journey, the script keeps "calling" a third- party website, 
from this website, the data related to the E.T.A. of the train is scraped every 50 seconds and the number of seconds to arrival are calculated.
The moment the number of seconds remaining are less than or equal to the number of minutes * 60 , the script uses Twilio and places a call on 
the users' phone to wake him/her up.

Libraries used - Twilio, BeautifulSoup, urllib, datetime, schedule, time, pygame.

This script can be further integrated with an android application to get the data from the user without the hassle of entering the data via
laptop/the device running this code.

The SmartAlarm has a huge area of utility and practical use.
