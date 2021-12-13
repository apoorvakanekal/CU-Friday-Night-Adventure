# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:34:42 2020
@author: Danielle Vikki Apoorva Caroline
Description: This game takes you through a Friday night at CU Boulder. It is a click game and every decision takes you to a new choice.
Choose your own adventure and click anywhere to start. 
Extra Credit: We catered our code to the deaf because we used visual aspects to potray areas around Boulder. 
"""

import turtle

#class for interactions 
class interactions: 
    def __init__(self):
        "initializing the attributes"
       #setting up the screen, panel, and turtle 
        self.w=600
        self.h=600
        self.panel=turtle.Screen()
        turtle.setup(self.w,self.h)
        
        #beginning screen
        self.event0="start.gif"
        self.panel.addshape(self.event0)
        
        #creating the events with the actual pictures and gifs
        #staying in gifs
        self.stayIn = ["netflixhwk.gif","comp v design.gif", "Selling Sunsets v. Grey's Anatomy.gif","back homework.gif","back netflix.gif"]
       
        #going out gifs
        self.goingOut= ["hill vs pearl.gif","fratvpregame.gif","eatvshop.gif","pasta jay_s v bar taco.gif","shopping go back.gif","back eat.gif",
                   "pong and die go back .gif","big party v small party.gif","die v pong.gif","small party go back.gif"]
    
        
        #adding the screen design to the panel
        #staying in designs
        for i in range(len(self.stayIn)):
            self.panel.addshape(self.stayIn[i])
      
        #going out designs
        for i in range(len(self.goingOut)):
            self.panel.addshape(self.goingOut[i])
        
        #setting up the turtle and the starting event
        self.screen0=turtle.Turtle()
        self.screen0.shape(self.event0)
 
    
    #interactions between the screens
    #staying in interactions 
    def outin(self,x,y):
        "performs the outin decision interaction"
        global screen0
        if x<0:
            self.screen0.shape(self.goingOut[0])
            self.screen0.onclick(self.hillpearl)
            
        else:
            self.screen0.shape(self.stayIn[0])
            self.screen0.onclick(self.hmrknetflix)
        
    
    def hmrknetflix(self,x,y):
        "interaction decision between homework and netflix"
        if x<0:
            self.screen0.shape(self.stayIn[2])
            self.screen0.onclick(self.backhmrk)
        else:
            self.screen0.shape(self.stayIn[1])
            self.screen0.onclick(self.backnetflix)
        
        
    #going out interactions             
    def hillpearl(self,x,y):
        "interaction decision between hill and pearl"
        if x<0:
            self.screen0.shape(self.goingOut[1])
            self.screen0.onclick(self.fratpre)
        else:
            self.screen0.shape(self.goingOut[2])
            self.screen0.onclick(self.eatshop)
            
    def eatshop(self,x,y):
        "interaction decision between eat and shop"
        if x<0:
            self.screen0.shape(self.goingOut[3])
            self.screen0.onclick(self.backeat)
        else:
            self.screen0.shape(self.goingOut[4])
            self.screen0.onclick(self.restart)
            
    def fratpre(self,x,y):
        "interaction decision between frat party and pre-game"
        if x<0:
            self.screen0.shape(self.goingOut[6])
            self.screen0.onclick(self.restart)
        else:
            self.screen0.shape(self.goingOut[7])
            self.screen0.onclick(self.bigsmall)
            
    def bigsmall(self,x,y):
        "interaction decision between a big party and a small party"
        if x<0:
            self.screen0.shape(self.goingOut[9])
            self.screen0.onclick(self.backsmallparty)
        else:
            self.screen0.shape(self.goingOut[8])
            self.screen0.onclick(self.backhill)

        
    #the end screen to the interactions 
            
    def backhmrk(self,x,y):
        "ending picture for homework that will bring user back to the starting screen"
        self.screen0.shape(self.stayIn[4])
        self.screen0.onclick(self.restart)
           
            
    def backnetflix(self,x,y):
        "ending picture for netflix that will bring the user back to the starting screen"
        self.screen0.shape(self.stayIn[3])
        self.screen0.onclick(self.restart)        
            
    def backhill(self,x,y):
        "ending picture for the hill interactions that will bring the user back to the starting screen"
        self.screen0.shape(self.goingOut[6])
        self.screen0.onclick(self.restart)
            
    def backeat(self,x,y):
        "ending picture for the eating interactions that will bring the user back to the starting screen"
        self.screen0.shape(self.goingOut[5])
        self.screen0.onclick(self.restart)
        
    def backsmallparty(self,x,y):
        "ending picture for the party interactions that will bring the uder back to the starting screen"
        self.screen0.shape(self.goingOut[9])
        self.screen0.onclick(self.restart)
    
    #bringing player back to the start of the interaction 
        
    def restart(self,x,y):
        "function that brings user back to the start screen"
        self.screen0.shape(self.event0)
        self.screen0.onclick(self.outin)
    

    #updating panel, calling function, cleanup    
        self.panel.update()

        
#instantiate 
inst=interactions()
inst.screen0.onclick(inst.outin)


turtle.done()
    


