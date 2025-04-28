
# NOTE: Click "Raw" on the right side to see README.md properly

# NBA Prediction Analysis

**Author:** Burak Baltali (TU Wien)  
**Date:** 2025-04-26  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)


## Project overview

We build multi-output Random Forest models to predict NBA “box-score” stats (points, rebounds, steals, turnovers, 3-pt attempts, field-goal attempts).  

- **Use case**: Forecast end-of-season and playoff performance for all players and teams (demo for the Los Angeles Lakers).  
- A top-10-scorer split was also tried, but performance collapsed (negative R²) due to insufficient data.  

### Prerequisites 
In this case following things will be needed

Python 3.12+
pandas
numpy
scikit-learn
matplotlib
dbrepo
requests
jupyterlab
ipykernel

## Repository structure



nba-prediction-analysis/
├── metadata/
│     ├── codemeta.json
│     ├── fair4ml_metadata.jsonld
├── models/
│     ├── nba_model.pkl
├── notebooks/
│   ├── .ipynb_checkpoints/
│   │   └── Analysis-checkpoint.ipynb
│   └── Analysis.ipynb
├── processed/
│   ├── regular_train.csv
│   ├── regular_test.csv
│   ├── playoff_train.csv
│   └── playoff_test.csv
├── raw/
│   ├── Regular_Season.csv
│   ├── Playoffs_edited.csv
│   ├── regularprocessed.py
│   ├── playoffprocessed.py
│   └── nba.csv
├── README.md
└── requirements.txt


### Notebook

Analysis.ipynb : Notebook of the data 
nba_model.pkl
### Raw Data 

* The source of the raw data comes from Kaggle (Link: https://www.kaggle.com/datasets/shivamkumar121215/nba-stats-dataset-for-last-10-years/data)
* RegularSeason.csv: Raw data of Regular Seasons.
* Playoffs_edited.csv: Raw data of Playoffs. In the beginning, the first column is named so that no error occurs during the upload of the data into dbrepo. 
* playoffprocessed.py: Processing the raw Playoff data into more readable processed data. This was very helpful especially splitting the seasons from String to numerical part and adding an extra
column for representing season_end.
* regularprocessed.py: Similar as the playoffprocessed.py, the code takes the raw RegularSeason.csv and converted into more readable data type so that it can be easily imported into dbrepo. 
* Furthermore there was nba.csv data, which is the aggregate of both the statistics of Playoffs and RegularSeason in the Kaggle. 
* Even though nba.csv, which is the aggregate of both Regular_Season and playoffs_edited was not used for this assignment, it was put in here. 



## Data sources:  
Testing and training data were created by using subset in the dbrepo. 

	
* regular_train.csv:  For training purposes, the seasons 2012-2013 through 2021-2022 were selected as training purpose (DBRepo PID: 4421e56c-4cd3-4ec1-a566-a89d7ec0bced)
* regular_test.csv: For testing purpose the 2022-2023  season was selected. (DBRepo PID: f9d84d5e-db01-4475-b7d1-80cfe9fe0e61)
* playoff_train.csv: For training purposes, the seasons 2012-2013 through 2022-2023 were selected (DBRepo PID: bcb3cf2b-27df-48cc-8b76-9e49254783d0) 
* playoff_test.csv: For testing purpose the 2023-2024  season was selected. (DBRepo PID: de37d568-e97f-4cb9-bc05-2e600cc97102)

* These csv data were added notebook, so that any user can read it directly and can be automatically run once you go to Analysis.ipynb

## Others

* README.md: Gives an information about the package
* requirements.txt: Contains all the python packages to run the project flawlessly
* In the metadata folder necessary files have been added
## Installation 

Platform : Pycharm


1) Open the terminal 
2) clone the repo https://github.com/bubaltali/nba-prediction-analysis.git
2) install dependencies pip install -r requirements.txt. 
3) Launch the notebook
4) Cell-0 shouldn't be run since all the data from the repo has been downloaded in there
5) In the first code cell (Cell-1) of Analysis.ipynb you’ll find the csv data, which are stored locally. (DBRepo is not put in here due to security reasons) Run it, entering your DBRepo password when prompted; it will populate the processed/ folder.
6) You can start running the data (Cell 0 shouldn't be run. This was used for personal use)
7) Last cells have been used for creating models and png files for exporting the results as png format.