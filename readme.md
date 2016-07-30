
# Dynamically location simulate in google map (browser)

OSX, iOS and Xcode, using debug mode can simulate location in iOS, using GPX file to control the route, but the routing is fixed in GPX file. This tool setup a Flask web site on OSX localhost (of course, you can share it in intranet and control it by other device), the web page provide Google map to move to next location by click.

## Installation

1. download as folder
2. Make sure your `brew` installed and *updated*.
3. Install `pip`, you are refer https://pip.pypa.io/en/stable/installing/.
4. run `sudo pip install flask`.
5. run `sudo pip install apscheduler`.
6. run `export FLASK_APP=\{your wolfberry folder path}\app.py`
7. run `flask run`
8. open browser in `http://127.0.0.1:5000/`
9. of course, in xcode debug mode, and add `IorP.gpx` file into the simulate list.
10. have fun.

## Hints

* Remember turn off Wifi.
* If you would stay in certain location over 2 mins, please change the time period in app.py - update_location.
* Please register a free Google Map API token:https://developers.google.com/maps/documentation/javascript/. And chang it in map.html => https://maps.googleapis.com/maps/api/js?key={your_token}.
* Using `brew update` before run the flask web site.
* Install python package by `pip`
* Please consider your speed, the map also include the scale. Superman mostly is not allow in real world.



---------

讓我們宅宅佔領全世界吧!

*I choose a lazy person to do a hard job. Because a lazy person will find an easy way to do it.*
― Bill Gates
