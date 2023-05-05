import pandas as pd

#note: to view this excel file you have to pip install openpyxl
#to view it properly and clean it, look at it in a Jupyter notebook, you don't get a good view here :)

launch_df = pd.read_excel("C:/Users/chhar/Documents/CFG Degree/DATA/Project/APIs/Rocket Atmospheric Impact/Launch and re-entry database.xlsx", sheet_name="2019 launches")
print(launch_df.head())

reentries_df = pd.read_excel("C:/Users/chhar/Documents/CFG Degree/DATA/Project/APIs/Rocket Atmospheric Impact/Launch and re-entry database.xlsx", sheet_name="2019 re-entries")
print(reentries_df.head())

