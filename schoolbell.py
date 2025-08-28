#!/usr/bin/python3

# Simple python script to play sounds over the school day
# Credit to https://gist.github.com/BillSimpson/d7a1a531995c8b63492bb47ef8872618

belltones = {
    'warn' : 'warn.wav',
    'start' : 'sqbell.wav',
    'back' : 's1bell.wav'
}

bellschedule = {   
    '08:49' : 'warn',
    '08:50' : 'back',   
    '09:39' : 'warn',
    '09:40' : 'start',
    '10:29' : 'warn',
    '10:30' : 'start',
    '10:44' : 'warn',
    '10:45' : 'back',    
    '11:34' : 'warn',
    '11:35' : 'start',
    '12:24' : 'warn',
    '12:25' : 'start',
    '13:14' : 'warn',
    '13:15' : 'start',
    '14:09' : 'warn',
    '14:10' : 'back',
    '14:59' : 'warn',
    '15:00' : 'start',
    '15:49' : 'warn',
    '15:50' : 'start',
}

holidays = {
    '2020-09-07',
    '2020-09-25',
}

import os
import datetime
import sys
from time import sleep
from pygame import mixer

# Remove stuttering effect (see pygame.mixer.Sound.play issue #322
mixer.pre_init(buffer=2048)
# Initialise mixer
mixer.init()

# find filepath where script is running to assure bell files are here
path, runfile = os.path.split(os.path.abspath(sys.argv[0]))

try:
    try:  # check if a time is being passed and parse it
        force_dt = datetime.datetime.strptime(sys.argv[1],'%H:%M')
        filename = None
    except:  # for testing: if you pass a filename, the code will chime it
        force_dt = None
        filename = sys.argv[1]
except:
    filename = None

if force_dt:
    dt = force_dt
else:
    dt = datetime.datetime.now()

timestr = dt.strftime('%H:%M')
datestr = dt.strftime('%Y-%m-%d')

if dt.weekday() < 5 and datestr not in holidays:  
    # it is a weekday not a holiday, do chimes
    print('It is a schoolday, checking time '+timestr)

    if timestr in bellschedule:
        filename = belltones[bellschedule[timestr]]
        print(filename)

else:
    print('It is a weekend or holiday -- enjoy!')

if filename:
    
# Commented out as seems to be a bug with mpg321
#     filepath = os.path.join(path,filename)
#     command = 'mpg321 -a hw:1,0 '+filepath
#     os.system(command)
    print("Ring bell")
    
    # Load in sound
    mixer.music.load(filename)
    # Play sound
    mixer.music.play()
    # Sleep 10 seconds to allow sounds to play
    # Note - No sound played without sleep command!
    sleep(10)