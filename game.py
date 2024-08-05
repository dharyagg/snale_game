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

class Player:
	def __init__(self, game, x, y, direction = 4):
		self.x = x
		self.y = y
		self.food = 1
		self.eaten = False
		self.image = pygame.image.load('images/snake.png')
		self.rect = self.image.get_rect()
		self.width = 20
		self.height = 20
		self.delta = 20
		self.delta_x = self.delta
		self.delta_y = 0
		# up = 1, down = 2, left = 3, right = 4
		self.direction = direction
	# detect collistion between player head and food
	def detect_collision(self, food):
		if (self.x < food.x + food.width and \
			self.x + self.width > food.x and \
			 self.y < food.y + food.height and \
			 self.y + self.height > food.y):
			game.score += 1
			game.increase_length = True
			food.update()
	def move(self, food):
		self.detect_collision(food);
		if self.direction == 1:
			self.delta_x = 0
			self.delta_y = -self.delta
		elif self.direction == 2:
			self.delta_x = 0
			self.delta_y = self.delta
		elif self.direction == 3:
			self.delta_x = -self.delta
			self.delta_y = 0
		elif self.direction == 4:
			self.delta_x = self.delta
			self.delta_y = 0
		self.x += self.delta_x
		self.y += self.delta_y
		if self.x < 22 or self.y < 20 or self.x > game.window_width - 60 or self.y > game.window_height - 82:
			game.game_over = True

	def update(self, x, y):
		self.x = x
		self.y = y
		
class Food(pygame.sprite.Sprite):
	def __init__(self, game):
		super().__init__()
		self.x = random.randint(40, game.window_width-60)
		self.y = random.randint(40, game.window_height-100)
		self.image = pygame.image.load('images/food.png')
		self.rect = self.image.get_rect()
		self.width = 20
		self.height = 20
	def update(self):
		self.x = random.randint(40, window_width-60)
		self.y = random.randint(40, window_height-100)
