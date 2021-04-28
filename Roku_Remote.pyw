#Import And Setup Stuff

import tkinter
from roku import Roku
roku = Roku('***.***.*.*')

#Code For The Window
top = tkinter.Tk()
top.title('Roku Remote')
top.geometry('325x500')
top.configure(bg='#595854')

#Define All Button Codes

def ok():
    roku.select()
def back():
    roku.back()
def on():
    roku.poweron()
def off():
    roku.poweroff()
def home():
    roku.home()
def up():
    roku.up()
def down():
    roku.down()
def left():
    roku.left()
def right():
    roku.right()
def volume_up():
    roku.volume_up()
def volume_down():
    roku.volume_down()
def mute():
    roku.volume_mute()

#Create Buttons

OkButton = tkinter.Button(top, text ='OK', command = ok, bg='Purple', fg ='White', height ='3', width ='7', )
BackButton = tkinter.Button(top, text ='BACK', command = back, bg='Purple', fg ='White', height ='3', width ='7')
HomeButton = tkinter.Button(top, text ='HOME', command = home, bg='Purple', fg ='White', height ='3', width ='7')
VolumeUpButton = tkinter.Button(top, text ='VOL UP', command = volume_up, bg='Purple', fg ='White', height ='3', width ='8')
VolumeDownButton = tkinter.Button(top, text ='VOL DOWN', command = volume_down, bg='Purple', fg ='White', height ='3', width ='8')
OnButton = tkinter.Button(top, text ='ON', command = on, bg='Purple', fg ='White', height ='3', width ='7')
OffButton = tkinter.Button(top, text ='OFF', command = off, bg='Purple', fg ='White', height ='3', width ='7')
LeftButton = tkinter.Button(top, text ='LEFT', command = left, bg='Purple', fg ='White', height ='3', width ='7')
RightButton = tkinter.Button(top, text ='RIGHT', command = right, bg='Purple', fg ='White', height ='3', width ='7')
UpButton = tkinter.Button(top, text ='UP', command = up, bg='Purple', fg ='White', height ='3', width ='7')
DownButton = tkinter.Button(top, text ='DOWN', command = down, bg='Purple', fg ='White', height ='3', width ='7')
MuteButton = tkinter.Button(top, text ='MUTE', command = mute, bg='Purple', fg ='White', height ='3', width ='8')

#Position Buttons

OkButton.pack()
BackButton.pack()
HomeButton.pack()
VolumeUpButton.pack()
VolumeDownButton.pack()
MuteButton.pack()
OnButton.pack()
OffButton.pack()
LeftButton.pack()
RightButton.pack()
UpButton.pack()
DownButton.pack()

OkButton.place(x=133,y=220)
VolumeUpButton.place(x=259,y=55)
VolumeDownButton.place(x=259,y=0)
BackButton.place(x=75,y=110)
LeftButton.place(x=75,y=220)
RightButton.place(x=190,y=220)
OffButton.place(x=0,y=52)
OnButton.place(x=0,y=104)
DownButton.place(x=133,y=275)
UpButton.place(x=133,y=165)
HomeButton.place(x=190,y=110)
MuteButton.place(x=259,y=110)
OnButton.place(x=133,y=0)
OffButton.place(x=133,y=55)

top.mainloop()
