import pygame, sys
from pygame.locals import *
import eventHandling
from eventHandling import *
import GlobalConstants
from GlobalConstants import *
import display
from display import *
import CharacterClasses
from CharacterClasses import *





def main():

	#initialization of all my stuff!
	pygame.init()
	curEvents = []

	eventHandler = EventHandling()
	
	myGame = GameState()
	mydisplay = GiveDisplay(myGame)

	while True: # main game loop


		#pull in events
		curEvents = eventHandler.getEvents();

		#update game state
		for event in curEvents:
			if event == Actions.Quit:
				pygame.quit();
				sys.exit();
			if event == Actions.UpdateCharacters:
				
				#check win state
				if (not myGame.IsFinished):
					for climber in myGame.ClimberList:
						if (climber.Score.CurCount >= myGame.WinningScore):
							myGame.IsFinished = True
							myGame.WinnersName = climber.Name
							break
							
				myGame.UpdateClimbers = True
				print "finish Update characters"

			if (not myGame.IsFinished):
				if event == Actions.IncreasePoints:
					myGame.ClimberList[myGame.CurFocus].Score.increaseCount(100)
					myGame.UpdateDisplay = True
					myGame.DirtySprites.add(myGame.ClimberList[myGame.CurFocus])
					print myGame.ClimberList[myGame.CurFocus].Name + " now has " + str(myGame.ClimberList[myGame.CurFocus].Score.CurCount)

				if event == Actions.DecreasePoints:
					myGame.ClimberList[myGame.CurFocus].Score.decreaseCount(100)
					myGame.UpdateDisplay = True
					myGame.DirtySprites.add(myGame.ClimberList[myGame.CurFocus])
					print myGame.ClimberList[myGame.CurFocus].Name + " now has " + str(myGame.ClimberList[myGame.CurFocus].Score.CurCount)

				if event == Actions.MoveFocusLeft:
					myGame.CurFocus = (myGame.CurFocus - 1) % len(myGame.ClimberList)
					myGame.UpdateDisplay = True
					print "focus now on " + myGame.ClimberList[myGame.CurFocus].Name

				if event == Actions.MoveFocusRight:
					myGame.CurFocus = (myGame.CurFocus + 1) % len(myGame.ClimberList)
					myGame.UpdateDisplay = True
					print "focus now on " + myGame.ClimberList[myGame.CurFocus].Name

				
			
			



		#display changes
		mydisplay.updateScreen(myGame)

main()