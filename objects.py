import pygame
import numpy as np
import random


class objects:

    def __init__(self):

        # Shark is here
        self.shark_s = 3
        self.shark_img = []
        self.shark_X = (np.random.choice(range(0, 8), size=(1, self.shark_s), replace=False)).astype('f') * 100
        self.shark_Y = (np.random.randint(-2, 3, (1, self.shark_s))).astype('f') * 150
        self.shark_X_speed = 0.22
        self.shark_Y_speed = 0.25
        for i in range(self.shark_s):
            self.shark_img.append(pygame.image.load('shark_1.png'))

        # Object Formation
        self.object_s = 3
        self.object_img = []
        # self.object_img_format = np.random.randint(0, self.object_s, (1, self.object_s))
        self.object_X = (np.random.choice(range(0, 7), size=(1, self.object_s), replace=False)).astype('f') * 100
        self.object_Y = (np.random.randint(-3, 2, (1, self.object_s))).astype('f') * 150
        # self.object_X_speed = []
        self.object_Y_speed = 0.18

        # Image list for objects
        self.object_images = []

        self.object_images.append(pygame.image.load('boat_1.png'))
        self.object_images.append(pygame.image.load('boat_2.png'))
        self.object_images.append(pygame.image.load('rip_00.png'))
        self.object_images.append(pygame.image.load('buoy_1.png'))

        for i in range(self.object_s):
            self.object_img.append(random.choice(self.object_images))
            # self.object_X_speed.append(0)

    def object_movement(self):
        for j in range(self.object_s):
            if self.object_Y[0][j] >= 764:
                self.object_img[j] = random.choice(self.object_images)
                self.object_X[0][j] = float(random.randint(1, 7)) * 100
                self.object_Y[0][j] = float(random.randint(-3, 0)) * 150
            else:
                self.object_Y += self.object_Y_speed
                # self.object_X -= self.object_X_speed
        # print(self.object_Y)

    def shark_movement(self):
        # self.shark_X -= self.shark_X_speed
        # self.shark_Y += self.shark_Y_speed
        for j in range(self.shark_s):
            if self.shark_X[0][j] <= -60:
                self.shark_X[0][j] = float(random.randint(5, 8)) * 100
                self.shark_Y[0][j] = float(random.randint(-1, 3)) * 100
            elif self.shark_Y[0][j] >= 764:
                self.shark_X[0][j] = float(random.randint(5, 8)) * 100
                self.shark_Y[0][j] = float(random.randint(-1, 3)) * 100
            else:
                self.shark_X[0][j] -= self.shark_X_speed
                self.shark_Y[0][j] += self.shark_Y_speed

# o1 = objects()
# o1.object_movement()
