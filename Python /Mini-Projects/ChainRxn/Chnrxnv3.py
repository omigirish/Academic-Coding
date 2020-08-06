import pygame
import sys
import time
from math import *

# Initialization of Pygame
pygame.init()

# Block = Size of each block
blocks = 55
# Order of the matrix
sqFactor = int(input("Grid size??"))
noPlayers = int(input("How many players?"))
mode=int(input("Select Mode: Eliminating(1) or non-eliminating(0)?"))
width = blocks * sqFactor
height = blocks * sqFactor
display = pygame.display.set_mode((width, height))

# Sets the title of the game screen.
pygame.display.set_caption("Chain Reaction %dP Mode" % noPlayers)

# Define the clock.
clock = pygame.time.Clock()

# Define a standard font
font = pygame.font.SysFont("Calibri", 30)

# Predefine all Colors
background = (21, 67, 96)
border = (208, 211, 212)
red = (231, 76, 60)
white = (244, 246, 247)
violet = (255, 0, 255)
yellow = (204, 204, 0)
green = (88, 214, 141)
orange = (255, 153, 0)
darkBlue = (26, 26, 255)
lnm_green = (102, 255, 51)
blue = (102, 204, 255)

# List storing colours of different players
playerColor = [red, green, violet, yellow, orange, darkBlue, lnm_green, blue]

# List storing scores of all players.
score = []
for i in range(noPlayers):
    # Initialise all scores to 0
    score.append(0)

# List storing the colour of players playing the game
players = []
for i in range(noPlayers):
    # Assign colours to each player
    players.append(playerColor[i])

d = blocks / 2 - 2

# Calculating the number rows and columns based on height and width / block length
cols = int(width / blocks)
rows = int(height / blocks)

# Quit or Close the Game Window
def close():
    pygame.quit()
    sys.exit()


# Class for Each Spot in Grid
class Spot():
    def __init__(self):
        self.color = border
        # List of  neighbours
        self.neighbors = []
        # List of atoms
        self.noAtoms = 0

    def addNeighbors(self, i, j):
        if i > 0:
            self.neighbors.append(grid[i - 1][j])
        if i < rows - 1:
            self.neighbors.append(grid[i + 1][j])
        if j < cols - 1:
            self.neighbors.append(grid[i][j + 1])
        if j > 0:
            self.neighbors.append(grid[i][j - 1])


# Initializing the Grid with "Empty or 0"
def initializeGrid():
    global grid, score, players

    grid = [[] for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            newObj = Spot()
            grid[i].append(newObj)
    for i in range(cols):
        for j in range(rows):
            grid[i][j].addNeighbors(i, j)


# Draw the Grid in Pygame Window
def drawGrid(currentIndex):
    r = 0
    c = 0
    for i in range(int(width / blocks)):
        r += blocks
        c += blocks
        # Line fuction parameters are: window,color,start_cords,end_cords
        pygame.draw.line(display, players[currentIndex], (c, 0), (c, height))
        pygame.draw.line(display, players[currentIndex], (0, r), (width, r))


# Draw the Present Situation of Grid
def showPresentGrid(vibrate=1):
    r = -blocks  # xcoord
    c = -blocks  # ycoord
    padding = 2
    for i in range(cols):
        r += blocks
        c = -blocks
        for j in range(rows):
            c += blocks
            if grid[i][j].noAtoms == 0:
                grid[i][j].color = border
            elif grid[i][j].noAtoms == 1:
                pygame.draw.ellipse(display, grid[i][j].color,
                                    (r + blocks / 2 - d / 2 + vibrate, c + blocks / 2 - d / 2, d, d))
            elif grid[i][j].noAtoms == 2:
                pygame.draw.ellipse(display, grid[i][j].color, (r + 5, c + blocks / 2 - d / 2 - vibrate, d, d))
                pygame.draw.ellipse(display, grid[i][j].color,
                                    (r + d / 2 + blocks / 2 - d / 2 + vibrate, c + blocks / 2 - d / 2, d, d))
            elif grid[i][j].noAtoms == 3:
                angle = 90
                x = r + (d / 2) * cos(radians(angle)) + blocks / 2 - d / 2
                y = c + (d / 2) * sin(radians(angle)) + blocks / 2 - d / 2
                pygame.draw.ellipse(display, grid[i][j].color, (x - vibrate, y, d, d))
                x = r + (d / 2) * cos(radians(angle + 90)) + blocks / 2 - d / 2
                y = c + (d / 2) * sin(radians(angle + 90)) + 5
                pygame.draw.ellipse(display, grid[i][j].color, (x + vibrate, y, d, d))
                x = r + (d / 2) * cos(radians(angle - 90)) + blocks / 2 - d / 2
                y = c + (d / 2) * sin(radians(angle - 90)) + 5
                pygame.draw.ellipse(display, grid[i][j].color, (x - vibrate, y, d, d))

    pygame.display.update()


# Increase the Atom when Clicked
def addAtom(i, j, color):
    grid[i][j].noAtoms += 1
    grid[i][j].color = color


def checkbomb():
    global grid
    global cols
    flag = 0
    for i in range(cols):
        for j in range(rows):
            if grid[i][j].noAtoms >= len(grid[i][j].neighbors):
                flag = 1
                color = grid[i][j].color
                break

    if flag == 0:
        return 0
    else:
        return 1


def cutrecursion(colour):
    global grid
    global cols
    flag = 1
    for i in range(cols):
        for j in range(rows):
            if grid[i][j].color != colour:
                flag = 0
                break

    if flag == 0:
        return 0
    else:
        return 1


def updategrid(color, vibrate):
    global grid
    while checkbomb() == 1 and cutrecursion(color) == 0:
        for i in range(cols):
            for j in range(rows):
                if grid[i][j].noAtoms >= len(grid[i][j].neighbors):
                    grid[i][j].noAtoms = grid[i][j].noAtoms % len(grid[i][j].neighbors)
                    for m in range(len(grid[i][j].neighbors)):
                        grid[i][j].neighbors[m].noAtoms += 1
                        grid[i][j].neighbors[m].color = grid[i][j].color


    # Checking if Any Player has WON!


def isPlayerInGame():
    global score
    playerScore = []
    for i in range(noPlayers):
        playerScore.append(0)
    for i in range(cols):
        for j in range(rows):
            for k in range(noPlayers):
                if grid[i][j].color == players[k]:
                    playerScore[k] += grid[i][j].noAtoms
    score = playerScore[:]

def scorecalc():
    global score
    global noPlayers
    playerScore = []
    for i in range(noPlayers):
        playerScore.append(0)
    for i in range(cols):
        for j in range(rows):
            for k in range(noPlayers):
                if grid[i][j].color == players[k]:
                    playerScore[k] += grid[i][j].noAtoms
    score = playerScore[:]
# GAME OVER
def gameOver(playerIndex):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()

        text = font.render("Player %d Won!" % (playerIndex + 1), True, white)
        text2 = font.render("Press \'r\' to Reset!", True, white)

        display.blit(text, (width / 3, height / 3))
        display.blit(text2, (width / 3, height / 2))

        pygame.display.update()
        clock.tick(60)


def checkWon():
    num = 0
    for i in range(noPlayers):
        if score[i] == 0:
            num += 1
    if num == noPlayers - 1:
        for i in range(noPlayers):
            if score[i]:
                return i

    return 9999


# Main Loop
def gameLoop():
    global noPlayers
    global score
    global mode
    initializeGrid()
    loop = True
    turns = 0

    currentPlayer = 0

    vibrate = 2.0

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                i = int(x / blocks)
                j = int(y / blocks)
                if grid[i][j].color == players[currentPlayer] or grid[i][j].color == border:
                    turns += 1
                    addAtom(i, j, players[currentPlayer])
                    updategrid(players[currentPlayer], vibrate)
                    currentPlayer+=1
                    if currentPlayer==noPlayers:
                        currentPlayer=0
                    if turns>noPlayers:
                        scorecalc()
                        while score[currentPlayer]==0 and mode==1:
                            currentPlayer+=1
                            if currentPlayer == noPlayers:
                                currentPlayer = 0
                if turns >= noPlayers:
                    isPlayerInGame()

        display.fill(background)
        # Vibrate the Atoms in their Cells
        vibrate *= -1

        drawGrid(currentPlayer)
        showPresentGrid(vibrate)

        #pygame.display.update()

        res = checkWon()
        if res < 9999:
            gameOver(res)

        clock.tick(25)


gameLoop()