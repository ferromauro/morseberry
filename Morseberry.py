#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:06:04 2018

@author: Mauro Ferro conctact me at postmaster@ferromauro.it
"""
import sys
#from gpiozero import LED
from time import sleep

unity=0.4
dot=1*unity
dash=2*unity
sbp=1*unity # space between parts
sbl=2*unity # space between letters
sbw=6*unity # space between words

code= {'a':[dot,dash],
       'b':[dash,dot,dot,dot],
       'c':[dash,dot,dash,dot],
       'd':[dash,dot,dot],
       'e':[dot],
       'f':[dot,dot,dash,dot],
       'g':[dash,dash,dot],
       'h':[dot,dot,dot,dot],
       'i':[dot,dot],
       'j':[dot,dash,dash,dash],
       'k':[dash,dot,dash],
       'l':[dot,dash,dot,dot],
       'm':[dash,dash],
       'n':[dash,dot],
       'o':[dash,dash,dash],
       'p':[dot,dash,dash,dot],
       'q':[dash,dash,dot,dash],
       'r':[dot,dash,dot],
       's':[dot,dot,dot],
       't':[dash],
       'u':[dot,dot,dash],
       'v':[dot,dot,dot,dash],
       'w':[dot,dash,dash],
       'x':[dash,dot,dot,dash],
       'y':[dash,dot,dash,dash],
       'z':[dash,dash,dot,dot]
       }
 
def main():
    text = raw_input('Please insert yout text: ')

    if all(x.isalpha() or x.isspace() for x in text):
        text = text.lower()
        for x in text:
            if x == " ":
                print
                sleep(sbw)
            else:
                sys.stdout.write(x + ': ')
                sys.stdout.flush()
                for y in code[x]:
                    if y == dot:
                        sys.stdout.write('. ')
                        sys.stdout.flush()
                    else:
                        sys.stdout.write('_ ')
                        sys.stdout.flush()
                    sleep(sbp)
                print
                sleep(sbl)
    else:
        print('Please only letters and spaces...')

if __name__ =="__main__":
    main()
