# import necessary libraries
from sqlalchemy import func
import datetime as dt
import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask import Flask, jsonify, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Data Setup
#################################################
# Metadata
wine_data = pd.read_csv("../Data/clean_winemag-data.csv")
wine_df = pd.DataFrame(wine_data)

# # otu_id
# Otu_id = pd.read_csv("DataSets/Belly_Button_Biodiversity_otu_id.csv")
# otu_id_df = pd.DataFrame(Otu_id)

# #samples
# Samples = pd.read_csv("DataSets/Belly_Button_Biodiversity_samples.csv")
# samples_df = pd.DataFrame(Samples)
# # Fill NAN values in 'samples' dataframe with 0
# samples_df = samples_df.fillna(0)

#################################################
# Flask Routes
#################################################
@app.route("/")
# """Return the dashboard homepage."""
def home():
    return render_template("index.html")
    


@app.route('/names')
# """List of wine variety names.
# Returns a list of sample names in the format
# [
    # "Champagne Blend",
    # "Champagne Blend",
    # "Champagne Blend",
    # "Champagne Blend",
    # "Champagne Blend",
    # "Champagne Blend",
    # "Champagne Blend",
    # ...
# ]

# """
def names():
    names = list(wine_df[''])

    return jsonify(names)

@app.route('/price_points/<variety>')
# """List of prices, points and country for a certain wine variety.

# Returns a list of OTU descriptions in the following format

# [
    # 20,
    # 40,
    # 121,
    # 15,
    # 65,
    # ...
# ]
# """
def price_points(variety):
    prices = list(wine_df[wine_df['variety']==variety]['price'])
    points = list(wine_df[wine_df['variety']==variety]['points'])
    countries = list(wine_df[wine_df['variety']==variety]['country'])
    pri_pnt = []
    for i in range(0,len(a)):
        pri_pnt.append([price[i],points[i],countries[i]])
    return jsonify(pri_pnt)
    
@app.route('/metadata/<variety>')
# """MetaData for a given sample.


# Returns a json dictionary of sample metadata in the format

# {
    # Rating_Count: 200,
    # Min_Price: 4,
    # Max_Price: 2000,
    # Highest_Rating: "Winery Name"
    # Lowest_Rating; "Winery Name",
# }
# """
def meta(variety):
    prices = list(wine_df[wine_df['variety']==variety]['price'])
    points = list(wine_df[wine_df['variety']==variety]['points'])
    Rating_Count = len(points)
    Min_Price = min(prices)
    Max_Price = max(prices)
    variety_df = wine_df.loc[wine_df['variety']==variety,['points','winery']]
    Highest_Rating = list(set(variety_df[variety_df['points']==Max_Price]['winery']))
    Lowest_Rating = list(set(variety_df[variety_df['points']==Min_Price]['winery']))
    # all_meta = wine_df[wine_df['SAMPLEID'] == sampleID]
    # age = int(all_meta.AGE)
    # BBTYPE = all_meta.iloc[0]["BBTYPE"]
    # ETHNICITY = all_meta.iloc[0]["ETHNICITY"]
    # gender = all_meta.iloc[0]["GENDER"]
    # location = all_meta.iloc[0]["LOCATION"]
    sample_metadata = {}
    sample_metadata['Rating_Count'] = Rating_Count
    sample_metadata['Min_Price'] = Min_Price
    sample_metadata['Max_Price'] = Max_Price
    sample_metadata['Highest_Rating'] = Highest_Rating[0]
    sample_metadata['Lowest_Rating'] = Lowest_Rating[0]
    return jsonify(sample_metadata)
    
    

if __name__ == "__main__":
    app.run(debug=True)


##############################################################################################################33