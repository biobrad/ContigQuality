
**IMPORTANT: REQUIRES COMPLETED TORMES RUN OUTPUT FOLDER WITH ASSEMBLED FASTQ FILES TO WORK**

# ContigQuality

## samscript

Short Script to Generate read depth of contigs from assembled microbial genomes in tormes output folders

## meanlengthanddepth.py

Run after samscript - requires standalone datapane conda environment

### samscript

Script to align sequences using bwa and then generating coverage stats and quality scores for each contig.

### usage:  
place samscript in miniconda3/tormes/bin  

after activating the tormes conda environment enter:  
samscript \<tormes output folder path\> \<cpus to use\>    
(leave trailing '/' off folder name)  
Example: samscript /home/blogsj/tormesresults 24

### meanlengthanddepth.py

Can be run after running samscript to generate visualisations of contig quality data  
needs a separate environment at this stage due to incompatibility with current tormes dependencies

### Create datapane conda environment:  

conda create -n datapane -c conda-forge datapane=0.14.0 plotly  

conda activate datapane  

run this file with an argument of tormes results output directory after running the tormes pipeline and after running samscript.

example: meanlengthanddepth.py /home/jblogs/tormesoutputdirectory  
(again leave off the trailing folder '/')  

### Output generated:  
### .bam files
Samscript will generate bam files for all sequences with fastqfiles in tormesoutputfolder/bams
output from samscript will create files in tormesoutputfolder/genome_stats/\<sequence>\/coverage.report  

eg:  
#rname	startpos	endpos	numreads	covbases	coverage	meandepth	meanbaseq	meanmapq  
NODE_1_length_98032_cov_38.894921	1	98032	52495	98032	100	80.1366	33.7	60  
NODE_2_length_85910_cov_43.216245	1	85910	50938	85910	100	88.9155	33.7	60  
NODE_3_length_80887_cov_39.732867	1	80887	44227	80887	100	81.8892	33.7	59.9  
NODE_4_length_78948_cov_41.095878	1	78948	44560	78948	100	84.5851	33.7	60  
NODE_5_length_78847_cov_41.004012	1	78847	44415	78847	100	84.3845	33.7	60  
... etc  

samscript will also generate files used by meanlengthanddepth.py to create visualisations of contig number, read depth and quality + DataTable of results for each genome:

## output from meanlengthdepth.py - will be in the tormesoutput/report_files folder:

IE:   

![image](https://user-images.githubusercontent.com/55652506/192102712-ba726e28-ae51-4ea1-aa4a-ae252a35123a.png)
