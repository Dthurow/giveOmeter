import pygame, sys
from pygame.locals import *
import GlobalConstants
from GlobalConstants import *



FPS = 12 # frames per second setting


class GiveDisplay:


	def __init__(self, curGameState):
		self.SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

		SCREEN_HEIGHT = self.SCREEN.get_height()
		SCREEN_WIDTH = self.SCREEN.get_width()	

		self.BACKGROUND = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.BACKGROUND.fill(BLUE)
		#pygame.display.set_caption('Give-O-Meter')
		self.fpsClock = pygame.time.Clock()
		self.SCREEN.fill(BLUE)
		self.MyFont = pygame.font.SysFont(None, FONT_SIZE)
		curGameState.ClimberList[curGameState.CurFocus].Score.IsFocused = True

		curGameState.CounterGroup.update()
		curGameState.CounterGroup.clear(self.SCREEN, self.BACKGROUND)
		curGameState.CounterGroup.draw(self.SCREEN)

		
		pygame.display.update()
		print "initialized display"

	def updateScreen(self, curGameState):

		#self.SCREEN.fill(BLUE)

		#move the climbing sprites to the correct place
		if (curGameState.UpdateClimbers):
			for climber in curGameState.DirtySprites:
				pointChange = climber.Score.getChange()
				#print "height: " + str(SCREEN_HEIGHT) + " winning score " + str(curGameState.WinningScore) + " point change " + str(pointChange)
				leftChange =  (float(SCREEN_WIDTH - (GAMEBORDER_BOTTOM + GAMEBORDER_TOP)) / curGameState.WinningScore) * pointChange
				print "add to x: " + str(leftChange)
				self.moveClimberRight(leftChange, climber, curGameState)


		curGameState.ClimberGroup.update()
		curGameState.ClimberGroup.clear(self.SCREEN, self.BACKGROUND)
		curGameState.ClimberGroup.draw(self.SCREEN)

		#update the scores and the focus
		
		curGameState.CounterGroup.update()
		curGameState.CounterGroup.clear(self.SCREEN, self.BACKGROUND)
		curGameState.CounterGroup.draw(self.SCREEN)



		#check for win condition
		if (curGameState.IsFinished):
			winText = self.MyFont.render(curGameState.WinnersName + " HAS WON!!!", 1, GREEN)
			self.SCREEN.blit(winText, ((SCREEN_WIDTH / 2)-100, SCREEN_HEIGHT / 2))

		curGameState.UpdateClimbers = False
		curGameState.UpdateDisplay = False
		pygame.display.update()
		
		self.fpsClock.tick(FPS)

	def moveClimberUp(self, heightChange, climber, curGameState):
		speedChange = 10

		while (heightChange > 0):
			
			if (heightChange >= speedChange):
				climber.UpdateY(climber.rect.y - speedChange)
				heightChange -= speedChange
			else:
				climber.UpdateY(climber.rect.y - heightChange)
				heightChange = 0

			curGameState.ClimberGroup.update()
			curGameState.ClimberGroup.clear(self.SCREEN, self.BACKGROUND)
			curGameState.ClimberGroup.draw(self.SCREEN)

			
			#update the scores and the focus
			
			curGameState.CounterGroup.update()
			curGameState.CounterGroup.clear(self.SCREEN, self.BACKGROUND)
			curGameState.CounterGroup.draw(self.SCREEN)


			pygame.display.update()
			print "heightChange is at: " + str(heightChange)
			self.fpsClock.tick(FPS)

	def moveClimberRight(self, leftChange, climber, curGameState):
		speedChange = 10

		while (leftChange > 0):
			
			if (leftChange >= speedChange):
				climber.UpdateX(climber.rect.x + speedChange)
				leftChange -= speedChange
			else:
				climber.UpdateX(climber.rect.x + leftChange)
				leftChange = 0

			curGameState.ClimberGroup.update()
			curGameState.ClimberGroup.clear(self.SCREEN, self.BACKGROUND)
			curGameState.ClimberGroup.draw(self.SCREEN)

			
			#update the scores and the focus
			
			curGameState.CounterGroup.update()
			curGameState.CounterGroup.clear(self.SCREEN, self.BACKGROUND)
			curGameState.CounterGroup.draw(self.SCREEN)


			pygame.display.update()
			print "leftChange is at: " + str(leftChange)
			self.fpsClock.tick(FPS)
