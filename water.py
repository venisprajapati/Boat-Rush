import pygame
import numpy as np


class Water:

    def __init__(self):

        # Waves Formation
        # self.W_wave_img_format = np.random.randint(0, 2, (14, 14))
        self.wave_len = 16
        self.wave_wid = 14
        self.wave_diff_X = 64
        self.wave_diff_Y = 50

        self.wave_speed_X = 0.0055
        self.wave_speed_Y = 0.0055

        self.W_wave_img = []

        for i in range(self.wave_len):
            self.W_wave_img_X = []
            for j in range(self.wave_wid):
                self.W_wave_img_X.append(pygame.image.load('wave12.png'))
            self.W_wave_img.append(self.W_wave_img_X)

        self.wave_tmp_X = np.arange(-self.wave_diff_X, (self.wave_wid - 1) * self.wave_diff_X, self.wave_diff_X)

        self.wave_tmp_Y = np.arange(-self.wave_diff_Y, (self.wave_len - 1) * self.wave_diff_Y, self.wave_diff_Y)

        # self.W_wave_X = np.zeros((self.wave_len, self.wave_wid))
        # self.W_wave_Y = np.zeros((self.wave_len, self.wave_wid))

        self.W_wave_X = (np.vstack([self.wave_tmp_X] * self.wave_len)).astype('f')
        self.W_wave_Y = ((np.vstack([self.wave_tmp_Y] * self.wave_wid)).astype('f')).T

    def wave_move(self):

        if self.W_wave_X[0][0] >= 0:
            self.W_wave_X -= self.wave_diff_X
        else:
            self.W_wave_X += self.wave_speed_X

        if self.W_wave_Y[0][0] >= 0:
            self.W_wave_Y -= self.wave_diff_Y
        else:
            self.W_wave_Y += self.wave_speed_Y


w = Water()
w.wave_move()
