Simple python script to play sounds over the school day

May need to do following step to set correct default system soundcard.

Find your desired card with:

cat /proc/asound/cards
and then create /etc/asound.conf with following:
defaults.pcm.card 1
defaults.ctl.card 1
Replace "1" with the number of your card determined above.

Credit for sound clips:

nextperiod.wav <br />
https://freesound.org/people/Jackalgirl/sounds/683750/ <br />
warn.wav <br />
https://freesound.org/people/Benboncan/sounds/93646/ <br />
sqbell <br />
Squarepusher - Tommib <br />
s1bell <br />
Prince Jazzbo - School <br />
ambell <br />
Amadou & Mariam - La réalité <br />
