                                    #Import libraries
from pylab import *
from myfunction import shuffle

#!pip install pickle-mixin			#To install pickle
from pickle import dump
from pickle import load
                                    #Use load to feed data to variable
names = load(open('greekgods.pkl', 'rb'))
print(names)
                                    #Store required data using dump
flip = shuffle(names)
dump(flip, open('flipped.pkl', 'wb'))

