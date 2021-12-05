# CSC 466 Final Project - Music Recommender

## Group Members
1. Aidan Barbieux - abarbieu@calpoly.edu
1. Matthew Jaojocco - mjaojoco@calpoly.edu
1. Taylor Bedrosian - tbedrosi@calpoly.edu
1. Zachary Krogman - zkrogman@calpoly.edu

## Instructions 

### pageRank.ipynb
    contains code for pageRank.py in blocks for easy data manipulation and code needed to create graphics
    
### pageRank_analysis.ipynb
    uses pageRank.py to analyse runtime and create more graphics

### pageRank.py
    Usage1 python3 pageRank.py <datafile.>[csv/txt] <dataformat>[SNAP/SMALL] <d>[0-1] <epsilon>[~0.00001]

    positional arguments:
    datafile                .csv or .txt file with data in SNAP or SMALL format given by lab spec
    dataformat                
    optional arguments:
    --output OUTPUT     file name for output; default is out.csv
    --k K               k value for KNN; default is 10
    --m {okapi,cosine}  similarity metric to be used, default is okapi
    