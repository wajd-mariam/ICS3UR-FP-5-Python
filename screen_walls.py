#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program makes boundaries  to the edges

import ugame
import stage

import constants

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
# a list of sprites that will be updated every frame
sprites = []


def game_scene():
    # this function is a scene

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # create a sprite
    # parameters (image_bank, image # in bank, x, y)
    # alien = stage.Sprite(image_bank_1, 9, 64, 56)
    # sprites.append(alien)
    ship = stage.Sprite(image_bank_1, 5, int(constants.SCREEN_X / 2 -
                        constants.SPRITE_SIZE / 2),
                        int(constants.SCREEN_Y - constants.SPRITE_SIZE +
                        constants.SPRITE_SIZE / 2))
    sprites.insert(0, ship)  # insert at the top of sprite list

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # print(keys)

        # update game logic
        if keys & ugame.K_RIGHT != 0:
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + 1, ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()
