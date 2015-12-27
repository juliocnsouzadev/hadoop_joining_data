#!/usr/bin/env python
import sys


for line in sys.stdin:

    line       = line.strip()       #strip out carriage return
    key_value  = line.split(",")    #split line, into key and value, returns a list
    key_in     = key_value[0]       #key is first item in list
    value_in   = key_value[1]       #value is 2nd item



    #print key_in
    if key_value == 'ABC':  #if its a show from ABC
        show = key_in       #getTheShowName
        flag = -1           #this marks the show as an ABC show
        print('%s\t%s' % (show, flag))  #print a string, tab, and string
    if key_value.isdigit(): #if its a digit we just print
        show = key_in
        value = value_in
        print('%s\t%s' % (show, value))  #print a string, tab, and string

#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value