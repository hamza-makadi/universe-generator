from ursina import *
from camera import CameraMovment
import random

random.seed(1)
app = Ursina()

player = CameraMovement(y=50, gravity=0)


app.run()
