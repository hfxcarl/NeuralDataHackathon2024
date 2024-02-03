# NeuralDataHackathon2024


Grapth Theory - Systems Segregation



### data

The data folder contains both metadata and timeseries data:
 - /clean_healthy_ts/ direcory contains timeseries for 296 participants. Each timeseries is 196x200 matrix. The 196 corresponding to the functional run length (~10mins @TR=3sec) and 200-nodes from Schaefer Parcellation Atlas.
   Note that there are two sessions per subject. Getting started I recommend using ses-1. To add more power in classification accuracy the two sessions can either be concatenated (ie, 392x200) prior to calculating correlation coefficients, or calculate correlation coefficients of both session timeseries and take the average.
- /test_ts/ directory contains a demo timeseries for example/test of matlab and python system_segregation.
- Schaefer2018_200Parcels_7Networks_order_FSLMNI152_1mm_Centroid_RAS.csv (and .xlsx) file contains the 200-node atlas information including x,y,z centroid coordinates and network_membership of each node. 
- network_members.csv (aka: "M.txt") file contains the vector (1x200) labelling the network membership for each of the 200 nodes.
- participants_with_data_296.csv file contains information about each participant, including age, agegroup, yrs_education, cognitive-behaviour test scores, etc.

### tools

The tools folder contains Matlab libraries for BCT and systems-segregation, downloaded and installed from their respective sources.
- [BCT](https://sites.google.com/site/bctnet/)
- [systems-segregation-and-graph-tools]( https://github.com/mychan24/system-segregation-and-graph-tools) 

Python:

Matlab:

