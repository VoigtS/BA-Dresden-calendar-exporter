## BA-Dresden calendar exporter
This exporter was created to export the lesson calendar data from the selfservice campus (Campus Dual) and create an .ics file which can be imported into Outlook.

1. Clone this repositroy into a local directory of your choice
2. Execute the command ```pip install -r requirements.txt``` from your terminal to install the currently needed dependencies.
3. Change the ```userid``` and the ```hashcode``` values within the ```exporter.py``` to your corresponding values.
   You can get the hashcode from Campus Dual if you log into the site, view the page source and search for the entry ```hash```.
4. Execute the Script.
5. Double click the resulting ```ba-calendar.ics``` to import it into your Outlook calendar which will be created within the same directory of the exporter.

