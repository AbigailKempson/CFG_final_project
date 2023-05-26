# CFG Final Project
Final project for Code First Girls Data Engineering Nano Degree:

"What have the environmental impacts been from SpaceX rocket launches, and how could SpaceX minimise their impact moving forward?"


This README outlines the details of collaborating on our project. 

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](https://desktop.github.com/)
* [Jupyter Notebook](https://jupyter.org/install)
* Python Virtual Environment e.g. [miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Installation

* `git clone <repository-url>` this repository
* Jupyter notebook > Kernell > Run & Restart ALL

## Python Libraries Required

* pandas `pip install pandas`
* numpy `pip install numpy`
* matplotlib `pip install matplotlib`
* seaborn `pip install seaborn`
* requests `pip install requests`
* missingno `pip install missingno`
* from sklearn.model_selection import train_test_split
* from sklearn.linear_model import LinearRegression

Note: It's generally recommended to create a virtual environment for your Python projects to keep the dependencies isolated.
You can create a virtual environment using tools like virtualenv or conda and activate it before installing the libraries. 
This helps manage the project dependencies and prevents conflicts between different projects.

## Data Sources 

**API**
[Space X API](https://r4yan.gitbook.io/spacexdb/)

**Data files:**
1. [Rocket atmospheric impact - Emissions Inventory and Results.](https://rdr.ucl.ac.uk/articles/dataset/Rocket_atmospheric_impact_-_Emissions_Inventory_and_Results/17032349?file=35128729)
This is an Excel Spreadsheet containing details of 2019 rocket launch emissions at the different launch stages; including geolocation information of re-entries of ‘space junk’, reusable rocket components and discarded launch parts. 
2. [A database on ‘flying objects’ that are currently within the Earth’s orbit, including satellites and rocket launch debris](https://www.kaggle.com/datasets/kandhalkhandeka/satellites-and-debris-in-earths-orbit)

## Further Reading / Useful Links

*[Space debris: is it time to start taking care of the cosmos?](https://www.iberdrola.com/sustainability/space-debris)
*[SpaceX-Reusable Rockets](https://www.spacex.com/reusability/)
*[5 Most Important Parts Of A Rocket](https://www.rankred.com/parts-of-a-rocket/)
