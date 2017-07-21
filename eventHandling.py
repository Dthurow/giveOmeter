import pygame, sys
from pygame.locals import *
import GlobalConstants
from GlobalConstants import *


class EventHandling:

	def __init__(self):
		print("loaded")

	def getEvents(self):
		returnList = []

		for event in pygame.event.get():
			if event.type == QUIT:
				returnList.append(Actions.Quit)
			if event.type == KEYDOWN:
				if event.key == K_RIGHT:
					returnList.append(Actions.MoveFocusRight)
				if event.key == K_LEFT:
					returnList.append(Actions.MoveFocusLeft)
				if event.key == K_UP:
					returnList.append(Actions.IncreasePoints)
				if event.key == K_DOWN:
					returnList.append(Actions.DecreasePoints)
				if event.key == K_RETURN:
					returnList.append(Actions.UpdateCharacters)
				if event.key == K_ESCAPE:
					returnList.append(Actions.Quit)

		return returnList

