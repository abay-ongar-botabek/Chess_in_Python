"""
This is our main driver file. It will be responsible for handling user input and
displaying the current GameState object
"""

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512 #400 is another option
DIMENSION = 8 #dimension of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animaitons later on
IMAGES = {}

"""
Initialize a global dictionary of images. 
This will be called exactly once in main
"""

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying 'IMAGES['wp']'
        
"""
The main driver for our code. This will handle user input and updating the graphics
"""

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        clock.tick(MAX_FPS)
        p.display.flip()

if __name__ == "__main__":
    main()