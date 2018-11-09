# -*- coding: utf-8 -*-
import math

'''Class Str_flip takes raw input and returns it as a reversed string'''
class Str_flip:
    def __init__(self, input):
        self.input = input
        a= input.split() # split on whitespace
        print a
        b=a[::-1] # create a list with reversed order of list a
        c = ' '.join(b) #convert output list to s string separated by whitespace
        print c

#######################
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        area= int(length) * int(width)
        print ("Rectangle Area equals" + " " +  str(area))

b1=Rectangle(4,3)

#########################

class Circle:

    def __init__(self, radius):
        self.radius = radius
        area= math.pi*(int(radius)**2)
        peri= math.pi*2*int(radius)
        print ("Circle Area equals" + " " +  str(area))
	print ("Circle perimeter equals" + " " +  str(peri))

c1=Circle(5)

#######################

##NOTE: I am unable to finish this class because of the question I wrote ##below.
############################

class Deal_strings:
    def __init__(self):
        print " Hello, Please enter some text "


    def get_string(self, input):
        self.input= input
        #print input
        return input

    def print_string(self, get_string): # not working, see below.
        self.get_string = get_string
        #self.input= input
        #a= ' '.join.input.upper()
        #print a
        print list(get_string)

##Q how can on e function receive the output from the previous funciton?
