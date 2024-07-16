#Importing libraries
import numpy as np
import matplotlib
import os 
import math 

#printing the Image
myHero = matplotlib.image.imread("warier.jpeg")
matplotlib.pyplot.imshow(myHero)
print(type(myHero))

#red componenet of image
myHeroRed = myHero.copy()
myHeroRed.setflags(write= True)
myHeroRed[:,:,1]=0 #Green as zero
myHeroRed[:,:,2]=0 #Blue as zero
matplotlib.pyplot.imshow(myHeroRed)

#green componenet of image
myHeroGreen = myHero.copy()
myHeroGreen.setflags(write= True)
myHeroGreen[:,:,0]=0 #Red as zero
myHeroGreen[:,:,2]=0 #Blue as zero
matplotlib.pyplot.imshow(list(myHeroGreen))

#blue componenet of image
myHeroBlue = myHero.copy()
myHeroBlue.setflags(write= True)
myHeroBlue[:,:,0]=0 #Red as zero
myHeroBlue[:,:,1]=0 #Green as zero 
matplotlib.pyplot.imshow(list(myHeroBlue))
