#!/bin/bash
#PBS -l nodes=1:ppn=2,walltime=24:00:00,mem=16gb
#PBS -N MAKER.Hw -j oe
cd ~/bigdata/MAKER
N=$PBS_ARRAYID
if [ ! $N ]; then
 N=$1
fi
if [ ! $N ]; then
 echo "Must provide a number for indexing into, with -t in qsub or on cmdline (eg tophat.arrayjob.sh 2)"
 exit;
fi

PREF=`head -n $N files | tail -n 1`
cd $PREF
ln -s ../../../genome_annotation/ scripts
cd *.maker.output
bash ../scripts/get_gff_fasta.sh
bash ../scripts/make_mapids.sh
bash ../scripts/map_ids.sh
bash ../scripts/run_swissprot_blast.sh
bash ../scripts/add_functional.sh
bash ../scripts/rename_contigs.sh

