#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     20-05-2020
# Copyright:   (c) Administrator 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Settings():

    def __init__(self):

        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3
        self.bullet_color = 60, 60, 60

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
