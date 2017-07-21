import pygame, sys
from pygame.locals import *
import GlobalConstants
from GlobalConstants import *


class Climber(pygame.sprite.Sprite):

	def __init__(self, name, fileName, startCount, startX, startY, startCounterX, startCounterY):
		# Call the sprite initialiser
		pygame.sprite.Sprite.__init__(self)
		self.Name = name
		#load in image
		self.image = pygame.image.load('SpriteImages/' + fileName)
		self.rect = self.image.get_rect()
		self.rect.x = startX
		self.rect.y = startY
		self.Score = Counter(startCount, startCounterX, startCounterY)
		print "loaded a climber"

	def UpdateY(self, newY):
		self.rect.y = newY
		print "updated rect y to: " + str(newY)



class Counter():
	

	def __init__(self, startCount, startX, startY):
		self.CurCount = startCount
		self.PrevCount = startCount
		self.HasChanged = False
		self.X = startX
		self.Y = startY
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



class GameState:
	WinningScore = 1000

	def __init__(self):
		self.CurFocus = 0

		climberSpace = SCREEN_WIDTH / 3

		self.ClimberList = [Climber("Team SPIE", "cat.png", 0, 100, SCREEN_HEIGHT-GAMEBORDER_BOTTOM, 100, SCREEN_HEIGHT-(GAMEBORDER_BOTTOM/2)), Climber("Team ERS", "cat.png", 0, 100 + climberSpace,  SCREEN_HEIGHT-GAMEBORDER_BOTTOM, 100 + climberSpace,  SCREEN_HEIGHT-(GAMEBORDER_BOTTOM/2)), Climber("Team Kool Kidz", "cat.png", 0, 100 + climberSpace * 2,  SCREEN_HEIGHT-GAMEBORDER_BOTTOM, 100 + climberSpace * 2,  SCREEN_HEIGHT-(GAMEBORDER_BOTTOM/2))]
		self.ClimberGroup = pygame.sprite.Group()
		self.ClimberGroup.add(self.ClimberList)
		self.UpdateDisplay = False
		self.UpdateClimbers = False
		self.IsFinished = False
		self.WinnersName = ""
		self.DirtySprites = pygame.sprite.Group()
		print "loaded game state"



#testing stuff

#test = GameState()
#print test.UpdateClimbers