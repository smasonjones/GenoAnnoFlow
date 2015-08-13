Run Genome annotation, training, re-training.
Support for selecting best protein/EST/RNAseq sets

Edit maker_teplate.txt in excel or similar, entering the path for you evidence, genome, or predictor files or a 0 if it doesn't exists. Save as tab delimited.

maker_file_structure.py configfile
maker -CTL
maker_ctl_populate.py configfile
qsub -t 1-10 maker_job.sh 
