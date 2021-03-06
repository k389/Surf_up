#%%
# Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Import SQLalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import extract

# Import Flask Dependencies
from flask import Flask, jsonify


# Set up database engine
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create classes
measurement = Base.classes.measurement
station = Base.classes.station
session = Session(engine)

# Create Flask connection
app = Flask(__name__)

#%%
# Route to the data
@app.route("/")


def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/june
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    /api/v1.0/june
    /api/v1.0/december
    ''')

# route to precipitation data
@app.route("/api/v1.0/precipitation")

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# route to station data
@app.route("/api/v1.0/stations")
# http://127.0.0.1:5000/api/v1.0/stations
def stations():
    results = session.query(station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations)

# route to tempreture data
@app.route("/api/v1.0/tobs")
# http://127.0.0.1:5000/api/v1.0/tobs
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(measurement.tobs).\
    filter(measurement.station == 'USC00519281').\
    filter(measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

# Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):

    sel = [func.min(measurement.tobs), func.avg(measurement.tobs),              func.max(measurement.tobs)]
    if not end:
        results = session.query(*sel).\
            filter(measurement.date >= start).\
            filter(measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    results = session.query(*sel).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

#%%
# route to june data (min, max and average temperature)
@app.route("/api/v1.0/june")
#http://127.0.0.1:5000/api/v1.0/june
def june():
    june_sel = [func.min(measurement.tobs), func.avg(measurement.tobs),              func.max(measurement.tobs)]
    june_results = session.query(*june_sel).filter(extract('month', measurement.date)==6).all()
    june_data = list(np.ravel(june_results))
    return jsonify(june_data)
    

# %%
# route to december data (min, max and average temperature)
@app.route("/api/v1.0/december")
#http://127.0.0.1:5000/api/v1.0/december
def december():
    dec_sel = [func.min(measurement.tobs), func.avg(measurement.tobs),              func.max(measurement.tobs)]
    december_results = session.query(*dec_sel).filter(extract('month', measurement.date)==12).all()
    #december = session.query(measurement.date, measurement.prcp, measurement.tobs).filter(extract('month', measurement.date)==12).all()
    december_data = list(np.ravel(december_results))
    return jsonify(december_data)
