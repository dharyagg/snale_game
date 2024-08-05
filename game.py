from keras.utils import to_categorical
import pygame
import random
import time
from DQN import DQNAgent
import numpy as np

pygame.init()
pygame.font.init()
pygame.display.set_caption('Snake Game')
window_width = 440
window_height = 480
clock = pygame.time.Clock()
max_score = 0
num_games = 0
game_speed = 10
epsilon = 1
agent = DQNAgent()

class Game:
	def __init__(self, window_width, window_height):
		self.window_width = 440
		self.window_height = 480
		self.screen = pygame.display.set_mode((window_width, window_height))
		self.background_image = pygame.image.load("images/background.png")
		self.score = 0
		self.increase_length = False
		self.game_over = False

