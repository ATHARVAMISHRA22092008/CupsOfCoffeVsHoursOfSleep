import plotly.express as px
import csv
import numpy as np
def getdatasource(datapath):
    coffecups=[]
    sleephours=[]
    with open(datapath)as csvfile:
        csvreader=csv.DictReader(csvfile)
        for row in csvreader:
            coffeecups.append(float(row["week"])) 
            sleephours.append(float(row["week"])) 
    return{"x":coffecups, "y": sleephours}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"], datasource["y"])
    print("correlation between the amount of coffe you drink and how much sleep you get: ", correlation[0,1])
def setup():
    datapath="coffee.csv"
    datasource=getdatasource(datapath)
    findcorrelation(datasource)
setup()











