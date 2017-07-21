import pygame, sys
from pygame.locals import *
import GlobalConstants
from GlobalConstants import *



FPS = 30 # frames per second setting


class GiveDisplay:


	def __init__(self, curGameState):
		self.SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption('Give-O-Meter')
		self.fpsClock = pygame.time.Clock()
		self.SCREEN.fill(WHITE)
		self.MyFont = pygame.font.SysFont(None, 56)

		for climber in curGameState.ClimberList:
			counterText = self.MyFont.render(str(climber.Score.CurCount), 1, BLACK)
			self.SCREEN.blit(counterText, (climber.Score.X, climber.Score.Y))

		print "initialized display"

	def updateScreen(self, curGameState):

		self.SCREEN.fill(WHITE)

		#move the climbing sprites to the correct place
		if (curGameState.UpdateClimbers):
			for climber in curGameState.DirtySprites:
				pointChange = climber.Score.getChange()
				print "height: " + str(SCREEN_HEIGHT) + " winning score " + str(curGameState.WinningScore) + " point change " + str(pointChange)
				heightChange =  (float(SCREEN_HEIGHT- (GAMEBORDER_BOTTOM + GAMEBORDER_TOP)) / curGameState.WinningScore) * pointChange
				print "add to y: " + str(heightChange)
				self.moveClimberUp(heightChange, climber)

					
		curGameState.ClimberGroup.draw(self.SCREEN)

		#update the scores and the focus
		for climber in curGameState.ClimberList:
			textColor = BLACK
			if (climber.Name == curGameState.ClimberList[curGameState.CurFocus].Name):
				textColor = BLUE

			counterText = self.MyFont.render(str(climber.Score.CurCount), 1, textColor)
			climberName = self.MyFont.render(str(climber.Name), 1, textColor)
			self.SCREEN.blit(counterText, (climber.Score.X, climber.Score.Y))
			self.SCREEN.blit(climberName, (climber.Score.X - 15, climber.Score.Y + 32))
					


		#check for win condition
		if (curGameState.IsFinished):
			winText = self.MyFont.render(curGameState.WinnersName + " HAS WON!!!", 1, GREEN)
			self.SCREEN.blit(winText, ((SCREEN_WIDTH / 2)-100, SCREEN_HEIGHT / 2))

		curGameState.UpdateClimbers = False
		curGameState.UpdateDisplay = False
		pygame.display.update()
		
		self.fpsClock.tick(FPS)

	def moveClimberUp(self, heightChange, climber):
		

		while (heightChange > 0):
			blotterRect = Rect(climber.rect.left, climber.rect.top, climber.rect.width, climber.rect.height)
			affectedblotterRect = pygame.draw.rect(self.SCREEN, WHITE, blotterRect)
			pygame.display.update(affectedblotterRect)
			if (heightChange >= 5):
				climber.UpdateY(climber.rect.y - 5)
				heightChange -= 5
			else:
				climber.UpdateY(climber.rect.y - heightChange)
				heightChange = 0
			affectedRect = self.SCREEN.blit(climber.image, (climber.rect.x, climber.rect.y))
			print "position it at " + str(climber.rect.x) + "," + str(climber.rect.y)
			pygame.display.update(affectedRect)
			print "heightChange is at: " + str(heightChange)
			self.fpsClock.tick(FPS)
