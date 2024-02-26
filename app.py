from tkinter import *
from time import *
import os
from Universe import Universe
from Sun import Sun
from Planet import Planet

WIDTH = 1200
HEIGHT = 800
xCenter = WIDTH / 2
yCenter = HEIGHT / 2

window = Tk()
window.title("Solar System")
window.state("zoomed")

canvas = Canvas(
    master=window,
    width=WIDTH,
    height=HEIGHT,
)
canvas.pack()

# background
bg_path = os.getcwd() + "\\images\\universe.png"
universe = PhotoImage(file=bg_path)
Universe(canvas=canvas, x=0, y=0, image=universe, anchor=NW)

# sun
sun_path = os.getcwd() + "\\images\\sun.png"
sun = PhotoImage(file=sun_path)
Sun(canvas=canvas, xCenter=xCenter, yCenter=yCenter, image=sun, anchor=NW)

# planets
mercury_path = os.getcwd() + "\\images\\mercury.png"
mercury_img = PhotoImage(file=mercury_path)
mercury = Planet(
    canvas=canvas,
    xCenter=xCenter,
    yCenter=yCenter,
    image=mercury_img,
    anchor=NW,
    sun_distance=60.5,
    step=2.3,
)

venus_path = os.getcwd() + "\\images\\venus.png"
venus_img = PhotoImage(file=venus_path)
venus = Planet(
    canvas=canvas,
    xCenter=xCenter,
    yCenter=yCenter,
    image=venus_img,
    anchor=NW,
    sun_distance=86,
    step=1.9,
)

earth_path = os.getcwd() + "\\images\\earth.png"
earth_img = PhotoImage(file=earth_path)
earth = Planet(
    canvas=canvas,
    xCenter=xCenter,
    yCenter=yCenter,
    image=earth_img,
    anchor=NW,
    sun_distance=121.5,
    step=1.7,
)

mars_path = os.getcwd() + "\\images\\mars.png"
mars_img = PhotoImage(file=mars_path)
mars = Planet(
    canvas=canvas,
    xCenter=xCenter,
    yCenter=yCenter,
    image=mars_img,
    anchor=NW,
    sun_distance=157,
    step=1.3,
)

jupiter_path = os.getcwd() + "\\images\\jupiter.png"
jupiter_img = PhotoImage(file=jupiter_path)
jupiter = Planet(
    canvas=canvas,
    xCenter=xCenter,
    yCenter=yCenter,
    image=jupiter_img,
    anchor=NW,
    sun_distance=207.5,
    step=1.1,
)

saturn_path = os.getcwd() + "\\images\\saturn.png"
saturn_img = PhotoImage(file=saturn_path)
saturn = Planet(
    canvas=canvas,
    xCenter=xCenter,
    yCenter=yCenter,
    image=saturn_img,
    anchor=NW,
    sun_distance=268,
    step=0.7,
)

uranus_path = os.getcwd() + "\\images\\uranus.png"
uranus_img = PhotoImage(file=uranus_path)
uranus = Planet(
    canvas=canvas,
    xCenter=xCenter,
    yCenter=yCenter,
    image=uranus_img,
    anchor=NW,
    sun_distance=318.5,
    step=0.5,
)

neptun_path = os.getcwd() + "\\images\\neptun.png"
neptun_img = PhotoImage(file=neptun_path)
neptun = Planet(
    canvas=canvas,
    xCenter=xCenter,
    yCenter=yCenter,
    image=neptun_img,
    anchor=NW,
    sun_distance=364,
    step=0.3,
)

pluto_path = os.getcwd() + "\\images\\pluto.png"
pluto_img = PhotoImage(file=pluto_path)
pluto = Planet(
    canvas=canvas,
    xCenter=xCenter,
    yCenter=yCenter,
    image=pluto_img,
    anchor=NW,
    sun_distance=394.5,
    step=0.1,
)

while True:
    try:
        mercury.spin()
        venus.spin()
        earth.spin()
        mars.spin()
        jupiter.spin()
        saturn.spin()
        uranus.spin()
        neptun.spin()
        pluto.spin()
        window.update()
        sleep(0.01)
    except TclError:  # avoid errors when closing the application
        pass
