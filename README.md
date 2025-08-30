# Simple school bell
### Simple python script to play sounds over the school day on a Raspberry Pi
Credit to https://gist.github.com/BillSimpson/d7a1a531995c8b63492bb47ef8872618 for the orginal idea, code and instructions

## Setup soundcard
May need to do following step to set correct default system soundcard. You can find your desired card with:
> #### cat /proc/asound/cards <br />
and then create /etc/asound.conf with following to set defaults. Replace "1" with the number of your card determined above. <br />
> #### defaults.pcm.card 1 <br />
> #### defaults.ctl.card 1 <br />


## Setup crontab
Open crontab <br />
> #### crontab -e  <br />
Add this line at the bottom (make sure there is a space between the * symbols) to run the program every minute  <br />
> #### * * * * * ./home/pi/schoolbell.py  <br />


## Credit for sound clips:
nextperiod.wav - https://freesound.org/people/Jackalgirl/sounds/683750/ <br />
warn.wav - https://freesound.org/people/Benboncan/sounds/93646/ <br />
sqbell - Squarepusher - Tommib <br />
s1bell - Prince Jazzbo - School <br />
ambell - Amadou & Mariam - La réalité <br />


