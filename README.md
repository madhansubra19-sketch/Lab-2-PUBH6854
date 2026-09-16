# Lab 2: Analysis Notebook — PUBH 6854

## Prerequisites 
Requires conda/mamba and R (≥4.x) with RStudio.


## Dataset
The dataset used for Lab 2 was the Mayo Clinic randomized controlled trial of D-penicillamine 
in primary biliary cirrhosis (PBC). The trial had 424 PBC patients meet eligibility criteria for
a randomized placebo of D-penicillamine. 312 were rndomized to D-penicillamine or placebo; 
another 112 declined the trail but were followed for survivial, 6 were lost during followup,
a total of 418 participants.
(T Therneau and P Grambsch (2000), Modeling Survival Data: Extending the Cox Model, Springer-Verlag, New York. ISBN: 0-387-98784-3.)

The Dataset can be downloaded multiple ways.

If you are using python, the data can be downloaded this way:
```python
import pandas as pd

url = "https://vincentarelbundock.github.io/Rdatasets/csv/survival/pbc.csv"
pbc = pd.read_csv(url)
```
A data fetching file called fetch_data.py was used to fetch the data for the python notebook. 

If you are using R it can be downloaded from Base R
```r 
library(survival)
data(pbc)
```
or you can use an url download of the same data:
```r
pbc <- read.csv("https://vincentarelbundock.github.io/Rdatasets/csv/survival/pbc.csv")
```

Also for reference here is the data dictionary for the dataset: https://vincentarelbundock.github.io/Rdatasets/doc/survival/pbc.html

## Data
Based on the Data, there are two interesting questions that can be analyzed:
1. How does bilirubin and albumin vary by histologic stage? 
2. Can bilirubin or albumin be used as a prognostic biomarker? 


## Repo Layout:
notebooks/analysis_python.ipynb, analysis_python.html, analysis_R.Rmd, analysis_R.html
scripts/  fetch_data.py
environment.yml, renv.lock, renv/, .Rprofile
README.md, AI_USAGE.md

## How to re-run

### Python  
To Run and then Re-Run the Python notebook follow these steps:
1.Create the environment: 
```bash
mamba env create -f environment.yml
```
2. Activate the environment 
```bash
conda activate lab2
```
3. Launch JupyterLab from the repo's root:
```bash
jupyter lab
```
4. open 'notebooks/analysis_python.ipynb'
5. Kernel --> Restart Kernel and Run all cells 

The notebook loads data by running `scripts/fetch_data.py`, which reads the PBC dataset 
directly from its URL. No local data file is needed.

### R
To run and then Re-Run r markdown file: analysis_R.Rmd, follow these steps: 
1. Open the repo folder as a project in Rstudio or setwd() to the repo's root
2. Restore the package library
```r
renv::restore()
```
3. Render the Markdown by clicking on Knit

The notebook reads the PBC dataset directly from its URL with `read.csv()`.
Output is written to `notebooks/analysis_R.html`.

## Rendered output
The Rendered HTML output for the python version is called: analysis_python.html 
and the R version is called analysis_R.html.

The comparison between Python and R implementations can be found at the of each respective 
analysis notebook file. 
## AI Usage
To see how AI was used for this Lab please take a look at AI_USAGE.md 

## Mixed Language  analysis Extra credit
The Notebooks for the the mixed language analysis was added under the notebooks directory
notebooks/ analysis_python.ipynb, analysis_python.html, analysis_R.Rmd, analysis_R.html, mixed_language_extra_credit.Rmd,mixed_language_extra_credit.html



