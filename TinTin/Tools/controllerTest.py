import pygame
import socket
import json
from pygame.math import Vector2

host = "localhost"
port = 3333
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

print("STARTING LOOP")

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYAXISMOTION:
                vec = Vector2(0,0)
                if event.axis == 1 or event.axis == 0:
	                vec = Vector2(j.get_axis(0), j.get_axis(1))
                if event.axis == 4 or event.axis == 3:
	                vec = Vector2(j.get_axis(3), j.get_axis(4))
                radius, angle = vec.as_polar()
                data = str.encode("=j= " + str(event.axis) + " " + str(event.value) + " "+str(radius)+ " " + str(angle) + "\n")
                s.send(data)
                print("RADIUS : " + str(radius) + " ANGLE: " + str(angle))
                print(event.dict, event.joy, event.axis, event.value)
            elif event.type == pygame.JOYBUTTONDOWN:
                data = str.encode("=j= "+ str(event.button) + " " + str(1) + "\n")
                s.send(data)
                print(event.dict, event.joy, event.button, 'pressed')
            elif event.type == pygame.JOYBUTTONUP:
                data = str.encode("=j= "+ str(event.button) + " " + str(0) + "\n")
                s.send(data)
                print(event.dict, event.joy, event.button, 'released')

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
