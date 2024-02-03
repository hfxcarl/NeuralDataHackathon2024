# NeuralDataHackathon2024


Grapth Theory - Systems Segregation


├── README.md
├── data
│   ├── Schaefer2018_200Parcels_7Networks_order_FSLMNI152_1mm_Centroid_RAS.csv
│   ├── Schaefer2018_200Parcels_7Networks_order_FSLMNI152_1mm_Centroid_RAS.xlsx
│   ├── clean_healthy_ts/
│   │   ├── sub-001_ses-1_Schaefer200x7_196v_ts.csv
│   │   ├── sub-001_ses-2_Schaefer200x7_196v_ts.csv
│   │   ├── sub-002_ses-1_Schaefer200x7_196v_ts.csv
│   │   ├── sub-002_ses-2_Schaefer200x7_196v_ts.csv
│   │   ├── sub-003_ses-1_Schaefer200x7_196v_ts.csv
│   │   ├── sub-003_ses-2_Schaefer200x7_196v_ts.csv
...
│   │   ├── sub-300_ses-1_Schaefer200x7_196v_ts.csv
│   │   └── sub-300_ses-2_Schaefer200x7_196v_ts.csv
│   ├── network_members.csv
│   ├── participants_with_data_296.csv
│   └── test_ts/
│       └── sub-001_ses-1_Schaefer200x7_196v_ts.csv
├── run_seg_test.py
├── seg_test_matlab.m
├── segmentation.py
├── systems_seg_example.m
└── tools
    ├── BCT_v20190303/
    └── system-segregation-and-graph-tools/


### data

The data folder contains both metadata and timeseries data:
 - /clean_healthy_ts/ direcory contains timeseries for 296 participants. Each timeseries is 196x200 matrix. The 196 corresponding to the functional run length (~10mins @TR=3sec) and 200-nodes from Schaefer Parcellation Atlas.
   Note that there are two sessions per subject. Getting started I recommend using ses-1. To add more power in classification accuracy the two sessions can either be concatenated (ie, 392x200) prior to calculating correlation coefficients, or calculate correlation coefficients of both session timeseries and take the average.
- /test_ts/ directory contains a demo timeseries for example/test of matlab and python system_segregation.
- Schaefer2018_200Parcels_7Networks_order_FSLMNI152_1mm_Centroid_RAS.csv (and .xlsx) file contains the 200-node atlas information including x,y,z centroid coordinates and network_membership of each node. 
- network_members.csv (aka: "M.txt") file contains the vector (1x200) labelling the network membership for each of the 200 nodes.
- participants_with_data_296.csv file contains information about each participant, including age, agegroup, yrs_education, cognitive-behaviour test scores, etc.



Python:

Matlab:

