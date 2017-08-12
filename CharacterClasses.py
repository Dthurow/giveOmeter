import pygame, sys
from pygame.locals import *
import GlobalConstants
from GlobalConstants import *
import os
import json


class Climber(pygame.sprite.Sprite):

	def __init__(self, name, fileName, startCount, startX, startY, startCounterX, startCounterY):
		# Call the sprite initialiser
		pygame.sprite.Sprite.__init__(self)
		self.Name = name
		#load in image
		self.FileName = fileName
		self.ImageList = []
		for dirname, dirnames, filenames in os.walk('SpriteImages/' + fileName):
			for file in filenames:
				print "Loading " + file
				self.ImageList.append(pygame.image.load('SpriteImages/' + fileName + '/' + file))

		self.CurImage = 0
		self.image = self.ImageList[self.CurImage]
		self.rect = self.image.get_rect()
		self.rect.x = startX
		self.rect.y = startY
		self.Score = Counter(startCount, startCounterX, startCounterY, self.Name)
		print "loaded a climber"

	def UpdateY(self, newY):
		self.rect.y = newY
		print "updated rect y to: " + str(newY)
		self.update()

	def UpdateX(self, newX):
		self.rect.x = newX
		print "updated rect x to: " + str(newX)
		self.update()

	def update(self, *args):
		self.CurImage = (self.CurImage + 1) % len(self.ImageList)
		self.image = self.ImageList[self.CurImage]



class Counter(pygame.sprite.Sprite):
	

	def __init__(self, startCount, startX, startY, displayName):
		# Call the sprite initialiser
		pygame.sprite.Sprite.__init__(self)
		self.MyFont = pygame.font.SysFont(None, FONT_SIZE)
		self.CurCount = startCount
		self.PrevCount = startCount
		self.HasChanged = False
		self.IsFocused = False
		self.image = self.MyFont.render(str(startCount), 1, BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = startX
		self.rect.y = startY
		self.DisplayName = displayName
		print "loaded a counter"

	def increaseCount(self, newCount):
		self.CurCount = self.CurCount + newCount
		self.HasChanged = True
		#print "new current count is " + str(self.CurCount)

	def decreaseCount(self, newCount):
		self.CurCount = self.CurCount - newCount
		self.HasChanged = True
		#print "new current count is " + str(self.CurCount)

	def getChange(self):
		returnVal = self.CurCount - self.PrevCount
		self.HasChanged = False
		self.PrevCount = self.CurCount
		return returnVal

	def update(self, *args):
		if self.IsFocused:
			self.image = self.MyFont.render(self.DisplayName + ": " + str(self.CurCount), 1, GREEN)
		else:
			self.image = self.MyFont.render(self.DisplayName + ": " + str(self.CurCount), 1, WHITE)



class GameState:
	WinningScore = 5000

	def __init__(self, fileName):
		self.CurFocus = 0


		f = open(fileName, 'r')
		fileJson = json.load(f)		

		self.WinningScore = fileJson['WinningScore']


		self.ClimberGroup = pygame.sprite.Group()
		self.ClimberList = []
		self.CounterGroup = pygame.sprite.Group()

		prevClimberTextY = - SPRITE_HEIGHT

		for climberJSON in fileJson['Climbers']:
			curTextY = prevClimberTextY + TEXT_HEIGHT + SPRITE_HEIGHT
			curClimberY = curTextY + TEXT_HEIGHT
			prevClimberTextY = curTextY

			newClimber = Climber(climberJSON[0], climberJSON[1], climberJSON[2], GAMEBORDER_LEFT, curClimberY, GAMEBORDER_LEFT, curTextY)
			self.ClimberList.append(newClimber)
			self.ClimberGroup.add(newClimber)
			self.CounterGroup.add(newClimber.Score)
		
					

		self.UpdateDisplay = False
		self.UpdateClimbers = False
		self.IsFinished = False
		self.WinnersName = ""
		self.DirtySprites = pygame.sprite.Group()

		print "loaded game state"

	def saveToFile(self, fileName):
		fileJson = {'WinningScore': self.WinningScore, 'Climbers': []  }

		for climber in self.ClimberList:
			fileJson['Climbers'].append((climber.Name, climber.FileName, climber.Score.CurCount, climber.rect.x, climber.rect.y, climber.Score.rect.x, climber.Score.rect.y ))

		json.dump(fileJson, open(fileName, 'w'))