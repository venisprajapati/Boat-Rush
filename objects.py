import pygame
import numpy as np
import random


class objects:

    def __init__(self):

        # Object Formation
        self.object_s = 6
        self.object_img = []
        self.object_img_format = np.random.randint(0, self.object_s, (1, self.object_s))
        self.object_X = (np.random.randint(0, 7, (1, self.object_s))).astype('f')*100
        self.object_Y = (np.random.randint(-3, 2, (1, self.object_s))).astype('f')*150
        self.object_X_speed = []
        self.object_Y_speed = 0.50
        self.a = []

        for i in range(self.object_s):
            if self.object_img_format[0][i] == 0 or self.object_img_format[0][i] == 2:
                self.object_img.append(pygame.image.load('boat_1.png'))
                self.object_X_speed.append(0)
            elif self.object_img_format[0][i] == 1 or self.object_img_format[0][i] == 3:
                self.object_img.append(pygame.image.load('shark 1.png'))
                self.object_X_speed.append(0.52)
            else:
                self.object_img.append(pygame.image.load('boatt2.png'))
                self.object_X_speed.append(0)

    def object_movement(self):
        self.object_Y += self.object_Y_speed
        self.object_X -= self.object_X_speed
        # print(self.object_Y)

# o1 = objects()
# o1.object_movement()
