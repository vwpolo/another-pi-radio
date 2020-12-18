#!/usr/bin/env python



import time
import subprocess
import sys
from gpiozero import Button

def function_botones():
    NEXT_BTN=Button(23)
    NEXT_BTN.when_pressed=function_next

    VOL_UP=Button(22)
    VOL_UP.when_pressed=volume_up

    VOL_DOWN=Button(24)
    VOL_DOWN.when_pressed=volume_down




def function_init():
#switch off mic
    cmd='amixer cset numid=7 off'
    subprocess.call(cmd,shell=True)

#set init volume 20%

    cmd='mpc volume 20'
    subprocess.call(cmd,shell=True)


    cmd='mpc clear'
    subprocess.call(cmd,shell=True)

    cmd='mpc load ' + my_playlist
    subprocess.call(cmd,shell=True)

    cmd='espeak -v an ' + radio_names[index-1] + '  2>/dev/null'
    subprocess.call(cmd,shell=True)

    cmd='mpc play ' + str(index)
    subprocess.call(cmd,shell=True)



def volume_up(canal):
    cmd="mpc volume +10"
    subprocess.call(cmd,shell=True)

def volume_down(canal):
    cmd="mpc volume -10"
    subprocess.call(cmd,shell=True)


def function_next(canal):
    global index
    index+= 1

    if index > len(radio_names):
       index=1

    cmd='mpc stop'
    subprocess.call(cmd,shell=True)


    cmd='espeak -v an ' + radio_names[index-1] + '  2>/dev/null'
    subprocess.call(cmd,shell=True)

    cmd='mpc play ' + str(index)
    subprocess.call(cmd,shell=True)


### main ###



# edit file and add  <stream> to playlist

my_playlist='radio_list'

#folder='/var/lib/mpd/playlists'

# add text-to-speack here
# mismo orden que la playlist file: /var/lib/mpd/playlists/radio_list.m3u
# OJO: el indice de la lista empieza por 0

radio_names=["fip_radio", "Classic_and_jazz", "radio_clasica"]

#emisora inicial
index=1

#volumen inicial
#volume=20



function_botones()
function_init()


while True:
    pass
#wait for events





