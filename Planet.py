from math import *
from random import *


class Planet:
    def __init__(self, canvas, xCenter, yCenter, image, anchor, sun_distance, step):
        self.canvas = canvas
        self.xCenter = xCenter
        self.yCenter = yCenter
        self.image = image
        self.anchor = anchor
        self.r = sun_distance

        # picks a random and orientation of the given step, clockwiese or counterclockwise, when the application starts
        self.step = radians(step * choice([-1, 1]))

        # picks a random angle position around the sun, at a distance of sun_distance, when the application starts
        self.angle = radians(randint(0, 360))

        # knowing the radius (hypotenuse) and the angle we can find x and y
        # y is the opposite and x is the adjacent
        # sin(angle) = y / r => y = sin(angle) * r
        # cos(angle) = x / r => x = cos(angle) * r
        self.canvas_object = self.canvas.create_image(
            xCenter + sun_distance * cos(self.angle) - image.width() / 2,
            yCenter + sun_distance * sin(self.angle) - image.height() / 2,
            image=image,
            anchor=anchor,
        )

    # updates the planet's angle by a step
    def spin(self):
        self.angle = (self.step + self.angle) % (2 * pi)
        dx = self.r * cos(self.angle)
        dy = self.r * sin(self.angle)
        self.canvas.delete(self.canvas_object)
        self.canvas_object = self.canvas.create_image(
            self.xCenter + dx - self.image.width() / 2,
            self.yCenter - dy - self.image.height() / 2,
            image=self.image,
            anchor=self.anchor,
        )
