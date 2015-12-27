#!/usr/bin/env python
import sys


prev_show          = "  "                #initialize previous word  to blank string
curr_show_total_cnt = 0;
line_cnt           = 0  #count input lines
abc_shows = []
shows_count = []

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list

    #note: for simple debugging use print statements, ie:
    curr_show  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    if value_in == '-1':
        abc_shows.append(curr_show)
        shows_count.append(0)

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list

    #note: for simple debugging use print statements, ie:
    curr_show  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    if value_in == '-1':
        continue

    if key_value in abc_shows:
        index = abc_shows.index(key_value)
        if (value_in.isdigit()):
            shows_count[index] += shows_count[index] + int(value_in)
loop = 0
for show in abc_shows:
    print('%s\t%s' % (show, shows_count[loop]))
    loop += 1;