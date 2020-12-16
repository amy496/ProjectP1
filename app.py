# 
# IMPORTS
# 
# you might have to import additional things you need

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

#
# SETUP/CONFIG
#
# change the classname to reflect the name of your table
# change the columns to reflect the columns you need
# each row of your data will be an instance of this class

app = Flask(__name__)

app.config["ENV"] = 'development'
app.config["SECRET_KEY"]=b'_5#y2L"F4Q8z\n\xec]/'

# change the following .db file name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-ell.db'
# this line is to prevent SQLAlchemy from throwing a warning
# if you don't get one with out it, feel free to remove
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#
# DB SETUP
# 

# this set's up our db connection to our flask application
db = SQLAlchemy(app)

# this is our model (aka table)
class ELLTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location=db.Column(db.String(255), nullable=False)
    number_2000=db.Column(db.String(255), nullable=False)
    number_2005=db.Column(db.String(255), nullable=False)
    number_2010=db.Column(db.String(255), nullable=False)
    number_2014=db.Column(db.String(255), nullable=False)
    number_2015=db.Column(db.String(255), nullable=False)
    number_2016=db.Column(db.String(255), nullable=False)
    number_2017=db.Column(db.String(255), nullable=False)
    percent_2000=db.Column(db.String(255), nullable=False)
    percent_2005=db.Column(db.String(255), nullable=False)
    percent_2010=db.Column(db.String(255), nullable=False)
    percent_2014=db.Column(db.String(255), nullable=False)
    percent_2015=db.Column(db.String(255), nullable=False)
    percent_2016=db.Column(db.String(255), nullable=False)
    percent_2017=db.Column(db.String(255), nullable=False)
#
# VIEWS 
#


# set up your index view to show your "home" page
# it should include:
# links to any pages you have
# information about your data
# information about how to access your data
# you can choose to output data on this page

@app.route('/', methods=['GET'])
def index():
    table = ELLTable.query.all()
    d=[]
    return render_template('index.html', data=d)


# set up the following views to allow users to make
# GET requests to get your data in json
# POST requests to store/update some data
# DELETE requests to delete some data

# change this to return your data
@app.route('/api', methods=['GET'])
def get_data():
    table = ELLTable.query.all()
    d=[]
    for row in table:
        row_as_dict={ 
            "location":row.location,
            "number_2000":row.number_2000,
            "number_2005":row.number_2005,
            "number_2015":row.number_2015,
            "number_2015":row.number_2015,
            "number_2016":row.number_2016,
            "number_2010":row.number_2010,
            "number_2017":row.number_2017,
            "percent_2000":row.percent_2000,
            "percent_2005":row.percent_2005,
            "percent_2010":row.percent_2010,
            "number_2014":row.number_2014,
            "percent_2014":row.percent_2014,
            "percent_2015":row.percent_2015,
            "percent_2016":row.percent_2016,
            "percent_2017":row.percent_2017 
        }
        d.append(row_as_dict)
    return jsonify(d)


#
# CODE TO BE EXECUTED WHEN RAN AS SCRIPT
#

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
