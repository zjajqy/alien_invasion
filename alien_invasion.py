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

import sys

import pygame

from pygame.sprite import Group

from settings import Settings

from ship import Ship

from alien import Alien

import game_function as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption = ("alien_invasion")

    ship = Ship(ai_settings, screen)

    bullets = Group()

    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    

    alien = Alien(ai_settings,screen)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings, screen, ship, aliens,bullets)


run_game()