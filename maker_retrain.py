#!usr/bin/python

import os

origopts = open("maker_opts.ctl",'r')
newopts = open("maker_opts2.ctl",'w')


for line in origopts:
	if(line.find("snaphmm=") >-1):
		newopts.write("snaphmm=snap/snap.hmm\n")
	else:
		newopts.write(line)


os.rename("maker_opts.ctl","maker_opts.ctl.old")
os.rename("maker_opts2.ctl","maker_opts.ctl")
