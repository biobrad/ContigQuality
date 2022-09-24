# ContigQuality
Short Script to Generate read depth of contigs from assembled microbial genomes in tormes output folders

### samscript

Script to extract read depth from samtools
usage: place samscript and meanlengthanddepth.py in tormes/bin
after activating the tormes conda environment, enter: samscript <tormes output folder path> <cpus>

### meanlengthanddepth.py

Can be run after running samscript to generate visualisations of contig quality data
needs a separate environment at this stage due to incompatibility with current tormes build.
conda create -n datapane -c bioconda datapane
conda create -n datapane -c conda-forge datapane=0.14.0 plotly
conda activate datapane
run this file with an argument of tormes output directory
example: meanlengthanddepth.py /home/jblogs/tormesoutputdirectory
