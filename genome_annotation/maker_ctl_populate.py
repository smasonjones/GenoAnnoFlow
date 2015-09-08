#!usr/bin/python

import shutil
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('masterfile')
parser.add_argument('--cpus',default='1')
parser.add_argument('--alt_peptide', default='C')
parser.add_argument('--max_dna_length',default='100000')
parser.add_argument('--mincontig',default='1')
parser.add_argument('--predlength',default='200')
parser.add_argument('--predstats',default='0')
parser.add_argument('--AEDThreshold',default='1')
parser.add_argument('--minprotein',default='0')
parser.add_argument('--altsplice',default='0')
parser.add_argument('--always_complete',default='0')
parser.add_argument('--map_forward',default='0')
parser.add_argument('--keep_preds',default='0')
parser.add_argument('--split_hit',default='10000')
parser.add_argument('--single_exon',default='0')
parser.add_argument('--single_length',default='250')
parser.add_argument('--correct_est_fusion',default='0')
parser.add_argument('--tries',default='2')
parser.add_argument('--clean_try',default='0')
parser.add_argument('--clean_up',default='0')
parser.add_argument('--organism_type',default='eukaryotic')
parser.add_argument('--model_org', default=' ')
parser.add_argument('--TMP',default=' ')
args = parser.parse_args(sys.argv[1:])

masterfile = open(sys.argv[1],'r')
line = masterfile.readline()
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
		elif(line.find("cpus") > -1):
			new_opts.write("cpus=" + args.cpus + "\n")
		elif(line.find("alt_peptide") > -1):
			new_opts.write("alt_peptide=" + args.alt_peptide + "\n")
		elif(line.find("max_dna_length") > -1):
                        new_opts.write("max_dna_length=" + args.max_dna_length + "\n")
		elif(line.find("mincontig") > -1):
                        new_opts.write("mincontig=" + args.mincontig + "\n")
		elif(line.find("predlength") > -1):
                        new_opts.write("predlength=" + args.predlength + "\n")
		elif(line.find("predstats") > -1):
                        new_opts.write("predstats=" + args.predstats + "\n")
		elif(line.find("AEDThreshold") > -1):
                        new_opts.write("AEDThreshold=" + args.AEDThreshold + "\n")
		elif(line.find("minprotein") > -1):
                        new_opts.write("minprotein=" + args.minprotein + "\n")
		elif(line.find("altsplice") > -1):
                        new_opts.write("altsplice=" + args.altsplice + "\n")
		elif(line.find("always_complete") > -1):
                        new_opts.write("always_complete=" + args.always_complete + "\n")
		elif(line.find("map_forward") > -1):
                        new_opts.write("map_forward=" + args.map_forward + "\n")
		elif(line.find("keep_preds") > -1):
                        new_opts.write("keep_preds=" + args.keep_preds + "\n")
		elif(line.find("split_hit") > -1):
                        new_opts.write("split_hit=" + args.split_hit + "\n")
		elif(line.find("single_exon") > -1):
                        new_opts.write("single_exon=" + args.single_exon + "\n")
		elif(line.find("single_length") > -1):
                        new_opts.write("single_length=" + args.single_length + "\n")
		elif(line.find("correct_est_fusion") > -1):
                        new_opts.write("correct_est_fusion=" + args.correct_est_fusion + "\n")
		elif(line.find("tries") > -1):
                        new_opts.write("tries=" + args.tries + "\n")
                elif(line.find("clean_try") > -1):
                        new_opts.write("clean_try=" + args.clean_try + "\n")
		elif(line.find("clean_up") > -1):
                        new_opts.write("clean_up=" + args.clean_up + "\n")
		elif(line.find("TMP") > -1):
                        new_opts.write("TMP=" + args.TMP + "\n")
		elif(line.find("organism_type") > -1):
		        new_opts.write("organism_type=" + args.organism_type + "\n")
                elif(line.find("model_org") > -1):
                        new_opts.write("model_org=" + args.model_org + "\n")

		else:
			new_opts.write(line)

