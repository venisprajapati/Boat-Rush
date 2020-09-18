import pygame
import numpy as np
import random


# Learning outcome: never use return statement if you don't want to break program.

class objects:

    def __init__(self):

        # Shark is here
        self.shark_s = 3
        self.shark_img = []
        self.shark_X = (np.random.choice(range(0, 8), size=(1, self.shark_s), replace=False)).astype('f') * 100
        self.shark_Y = (np.random.randint(-2, 3, (1, self.shark_s))).astype('f') * 150
        self.shark_X_speed = 0.22
        self.shark_Y_speed = 0.26
        for i in range(self.shark_s):
            self.shark_img.append(pygame.image.load('shark_1.png'))

        # Object Formation
        self.object_s = 3
        self.object_img = []
        # self.object_img_format = np.random.randint(0, self.object_s, (1, self.object_s))
        self.object_X = (np.random.choice(range(0, 7), size=(1, self.object_s), replace=False)).astype('f') * 100
        self.object_Y = (np.random.randint(-3, 2, (1, self.object_s))).astype('f') * 150
        # self.object_X_speed = []
        self.object_Y_speed = 0.12

        # Image list for objects
        self.object_images = []

        self.object_images.append(pygame.image.load('boat_1.png'))
        self.object_images.append(pygame.image.load('boat_2.png'))
        self.object_images.append(pygame.image.load('rip_00.png'))
        self.object_images.append(pygame.image.load('buoy_1.png'))

        for i in range(self.object_s):
            self.object_img.append(random.choice(self.object_images))
            # self.object_X_speed.append(0)

    def is_collision(self, boat_x, boat_y):
        for i in range(self.shark_s):
            if self.shark_Y[0][i] >= 0:
                if abs(int(self.shark_X[0][i]) - int(boat_x)) <= 42 and abs(
                        int(self.shark_Y[0][i]) - int(boat_y)) <= 58:
                    return True

        for j in range(self.object_s):
            if self.object_Y[0][j] >= 0:
                # if int(abs(self.object_X[0][j] - int(boat_x))) <= 52 and int(abs(self.object_Y[0][j] - int(
                # boat_y))) <= 102: return True
                if str(self.object_img[j]) == str(pygame.image.load('boat_1.png')):
                    if abs(int(self.object_X[0][j]) - int(boat_x)) <= 52 and abs(
                            int(self.object_Y[0][j]) - int(boat_y)) <= 142:
                        # print(self.object_img[j], pygame.image.load('boat_1.png'))
                        return True
                    # else:
                    #     return False
                elif str(self.object_img[j]) == str(pygame.image.load('boat_2.png')):
                    if abs(int(self.object_X[0][j]) - int(boat_x)) <= 48 and abs(
                            int(self.object_Y[0][j]) - int(boat_y)) <= 125:
                        # print(self.object_img[j], pygame.image.load('boat_2.png'))
                        return True
                    # else:
                    #     return False
                elif str(self.object_img[j]) == str(pygame.image.load('rip_00.png')):
                    if abs(int(self.object_X[0][j]) - int(boat_x)) + 10 <= 80 and abs(
                            int(self.object_Y[0][j]) - int(boat_y)) + 5 <= 90:
                        # print(self.object_img[j], pygame.image.load('rip_00.png'))
                        return True
                    # else:
                    #     return False
                elif str(self.object_img[j]) == str(pygame.image.load('buoy_1.png')):
                    if abs(int(self.object_X[0][j]) - int(boat_x)) <= 56 and abs(
                            int(self.object_Y[0][j]) - int(boat_y)) <= 101:
                        # print(self.object_img[j], pygame.image.load('buoy_1.png'))
                        return True
                    # else:
                    #     return False

    def object_movement(self, status):
        for j in range(self.object_s):
            if self.object_Y[0][j] >= 764:
                self.object_img[j] = random.choice(self.object_images)
                self.object_X[0][j] = float(random.randint(1, 7)) * 100
                self.object_Y[0][j] = float(random.randint(-3, 0)) * 150
            else:
                if status == 1:
                    self.object_Y_speed = 0.12
                    self.object_Y += self.object_Y_speed
                elif status == 2:
                    self.object_Y_speed = 0.24
                    self.object_Y += self.object_Y_speed
                elif status == 3:
                    self.object_Y_speed = 0.36
                    self.object_Y += self.object_Y_speed
                elif status == 4:
                    self.object_Y_speed = 0.48
                    self.object_Y += self.object_Y_speed
                elif status == 5:
                    self.object_Y_speed = 0.56
                    self.object_Y += self.object_Y_speed
                elif status == 6:
                    self.object_Y_speed = 0.60
                    self.object_Y += self.object_Y_speed
                # else:
                #     self.object_Y_speed = 0.56
                #     self.object_Y += self.object_Y_speed
                # print(self.object_Y_speed)
                # self.object_X -= self.object_X_speed
        # print(self.object_Y)-

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
