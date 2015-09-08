#!/bin/bash
#PBS -l nodes=1:ppn=2,walltime=300:00:00,mem=16gb 
#PBS -N MAKER.Hw -j oe

cd ~/bigdata/MAKER
module load perl
module load stajichlab
module load maker/2.31.8
module load snap
module load augustus/2.7
module load RepeatMasker
module load ncbi-blast
module load tRNAscan
which augustus

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
maker
mkdir snap
cp *maker.output/*.datastore/*/*/*/*gff snap/
cd snap/
maker2zff *.gff
fathom -categorize 1000 genome.ann genome.dna
fathom -export 1000 -plus uni.ann uni.dna
forge export.ann export.dna
hmm-assembler.pl pyu . > snap.hmm
cd ..
python scripts/maker_retrain.py
maker
cd *.maker.output
bash ../scripts/get_gff_fasta.sh
bash ../scripts/make_map_ids.sh
bash ../scripts/map_ids.sh
bash ../scripts/run_swissprot_blast.sh
bash ../scripts/add_functional.sh
bash ../scripts/rename_contigs.sh
