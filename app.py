from flask import request, Flask, render_template
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
import atexit, json, os.path



app = Flask(__name__)
temp_latitude = ''
temp_longtitue = ''
@app.route('/updatelocation')
def update_location():
    if 'latitude' in request.args and 'longitude' in request.args:
        print('--------------------------')
        print('[latitude]=%s' % request.args.get('latitude'))
        print('[longitude]=%s' % request.args.get('longitude'))
        temp_latitude = request.args.get('latitude')
        temp_longtitue = request.args.get('longitude')
        with open("IorP.gpx", "w") as gpx_file:
            gpx_file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx creator="GPS Visualizer http://www.gpsvisualizer.com/" version="1.0"><wpt lat="%s" lon="%s"><time>2016-07-28T01:50:36Z</time></wpt><wpt lat="%s" lon="%s"><time>2016-07-28T01:59:36Z</time></wpt></gpx>' % (temp_latitude,temp_longtitue,temp_latitude,temp_longtitue))
        with open("location_data.json", "w") as json_file:
            json_file.write('{"latitude":%s,"longtitue":%s}' % (temp_latitude,temp_longtitue))
        thecmd = "osascript updategpx.scpt"
        os.system(thecmd)
        return 'success'

@app.route('/')
def map():

    if os.path.isfile("location_data.json"):
        with open("location_data.json", "r") as json_file:
            json_string = json_file.read()
            location = json.loads(json_string)
    else:
        location = {'latitude':40.75349,'longtitue':-73.98089}
    return render_template('map.html',location_latitude=location['latitude'],location_longtitue=location['longtitue'])


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=update_location,
    trigger=IntervalTrigger(seconds=90),
    id='resetlocation_job',
    name='set the location when stall 90 secs',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
