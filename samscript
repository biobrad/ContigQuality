#!/bin/bash

### Script to extract read depth from samtools
### usage: place samscript in tormes/bin
### after activating the tormes conda environment, enter: samscript <tormes output folder path> <cpus>

CPUS=${2}
OUTWD=${1}

# extract metadata from report files and create reportfiles folder for later use
tar -f ${OUTWD}/report_files.tgz  -zxv report_files/metadata.txt
mv report_files/ ${OUTWD}
#
METADATA=${OUTWD}/report_files/metadata.txt
#
# create bam file folder
mkdir ${OUTWD}/bams
#
# create list of genomes with read files
#
awk '($2!="GENOME") && ($2!="Read1"){print $1,$2}' ${METADATA} > ${OUTWD}/bams/alignlist.tmp
#
# symlink genomes and reads to folder to create bamfiles
#
while read line ; do
 IFS=" " read -a seq <<< "$line"
 GENOME=${seq[0]}
 READS=$(echo ${seq[1]} | sed 's/_.*//')
 ln -s ${OUTWD}/genomes/${GENOME}.fasta ${OUTWD}/bams/${GENOME}.fasta
 ln -s ${OUTWD}/cleaned_reads/${READS}.ok_{1,2}.fastq.gz ${OUTWD}/bams/
#
# create bam files
#
bwa index ${OUTWD}/bams/${GENOME}.fasta
bwa mem -t ${CPUS} ${OUTWD}/bams/${GENOME}.fasta ${OUTWD}/bams/${READS}.ok_1.fastq.gz ${OUTWD}/bams/${READS}.ok_2.fastq.gz | samtools sort > ${OUTWD}/bams/${GENOME}.bwa.bam
#
# run coverage/depth
#
samtools coverage -o ${OUTWD}/genome_stats/${GENOME}_genome_stats/coverage.report --reference ${OUTWD}/bams/${GENOME}.fasta ${OUTWD}/bams/${GENOME}.bwa.bam
awk -v GENOME="$GENOME" 'BEGIN{OFS=",";} {split($1,a,"_"); sub(/\.[0-9]+/,"",$7); sub(/\.[0-9]+/,"",$9)} {print GENOME,a[2],a[4],$7,$9}' ${OUTWD}/genome_stats/${GENOME}_genome_stats/coverage.report | sed '1s/.*/seq,contig,length,meandepth,meanqual/' > ${OUTWD}/report_files/${GENOME}contlengdepqual.csv

rm -rf ${OUTWD}/bams/${READS}.ok_{1,2}.fastq.gz
rm -rf ${OUTWD}/bams/${GENOME}.fasta*
#
done < ${OUTWD}/bams/alignlist.tmp

rm -rf ${OUTWD}/bams/alignlist.tmp
