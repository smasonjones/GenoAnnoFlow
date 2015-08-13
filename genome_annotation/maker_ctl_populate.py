#!usr/bin/python

import shutil
import os
import sys

masterfile = open(sys.argv[1],'r')

for line in masterfile:
	files = line.split()
	root = files[0].split('.')
	root = root[0]
	family = files[1].split('.')
	family = family[0]
	completedir = 'genomes/' + family + '/' + root + '/'
	orig_opts =  open("maker_opts.ctl",'r')
	new_opts =  open(completedir + "maker_opts.ctl",'w+')
	shutil.copy('maker_bopts.ctl',completedir + 'maker_bopts.ctl')
	shutil.copy('maker_exe.ctl',completedir + 'maker_exe.ctl')
	for line in orig_opts:
		if(line.find("augustus_species=")> -1):
			new_opts.write("augustus_species=" + files[2] + "\n")
		elif(line.find("snaphmm=") >-1 and files[3] != '0'):
			new_opts.write("snaphmm=" + files[3] + "\n")
		elif(line.find("altest_gff=") > -1 and files[7] != '0'):
                        new_opts.write("altest=" + files[7] + "\n")
		elif(line.find("altest=") > -1 and files[6] != '0'):
			new_opts.write("altest=" + files[6] + "\n")
		elif(line.find("altest_pass=0") > -1 and files[6] != '0'):
                        new_opts.write("altest_pass=1\n")
                elif(line.find("est_gff=") > -1 and files[5] != '0'):
                        new_opts.write("est_gff=" + files[5] + '\n')
		elif(line.find("est=") and files[4] != '0'):
                        new_opts.write("est=" + files[4] + '\n')
                elif(line.find("est_pass=0") > -1 and files[4] != '0'):
                        new_opts.write("est_pass=1\n")
		elif(line.find("est2genome=") > -1 and (files[4] != '0' or files[6] != '0' or files[5] != '0' or files[7] != '0')):
                        new_opts.write("est2genome=1\n")
		elif(line.find("protein2genome=") > -1 and (files[8] != '0' or files[9] != '0')):
                        new_opts.write("protein2genome=1\n")
		elif(line.find("genome=")> -1):
			new_opts.write("genome=" + files[0] + "\n")
		elif(line.find("protein=") > -1 and files[8] != '0' and line.find('repeat') == -1):
                        new_opts.write("protein= " + files[8] + '\n')
		elif(line.find("protein_gff=") > -1 and files[9] != '0'):
                        new_opts.write("protein_gff=" + files[9] + '\n')
		elif(line.find("rmlib=") > -1 and files[10] != '0'):
                        new_opts.write("rmlib=" + files[10] + '\n')
                elif(line.find("rm_gff=") > -1 and files[11] != '0'):
                        new_opts.write("rm_gff=" + files[11] + '\n')
		elif(line.find("maker_gff=") > -1 and files[12] != '0'):
                        new_opts.write("maker_gff=" + files[12] + '\n')
		elif(line.find("altest_pass=") > -1 and files[12] != '0'):
                        new_opts.write("altest_pass=1\n")
		elif(line.find("est_pass=") > -1 and files[12] != '0'):
                        new_opts.write("est_pass=1\n")
		elif(line.find("protein_pass=") > -1 and files[12] != '0'):
                        new_opts.write("protein_pass=1\n")
		elif(line.find("model_pass=") > -1 and files[12] != '0'):
                        new_opts.write("model_pass=1\n")
		elif(line.find("pred_pass=") > -1 and files[12] != '0'):
                        new_opts.write("pred_pass=1\n")
		elif(line.find("rm_pass=") > -1 and files[12] != '0'):
                        new_opts.write("rm_pass=1\n")
		elif(line.find("other_pass=") > -1 and files[12] != '0'):
                        new_opts.write("other_pass=1\n")
		elif(line.find("snoscan_rrna=") > -1 and files[14] != '0'):
                        new_opts.write("snoscan_rrna=" + files[14] + '\n')
		elif(line.find("other_gff=") > -1 and files[13] != '0'):
                        new_opts.write("other_gff=" + files[13] + '\n')
		
		else:
			new_opts.write(line)

