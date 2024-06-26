
import numpy as np
import pandas as pd
import sqlalchemy

#import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask , jsonify



#################################################
# Database Setup
#################################################
engine = create_engine('sqlite:///Documents/project3/DATA-ENGINEERING-PROJECT/streaming1.sqlite')
conn = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
tab1 = Base.classes.netflix
tab2 = Base.classes.movie
tab3 = Base.classes.title
tab4 = Base.classes.director

# Create our session (link) from Python to the DB

#session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
#defining our flask routes
@app.route("/")
def welcome():

    print(f"Welcome to our Presentation")
    #List of all the available routes.
    return (
           f"Available Routes:<br/>"
           f"/api/v1.0/netflix<br/>"
           f"/api/v1.0/movie<br/>"
           f"/api/v1.0/title<br/>"
           f"/api/v1.0/director"
           )


#defining our netflix route
@app.route("/api/v1.0/netflix")
def netflix():

    session = Session(bind=engine)
    print(f"Starting the netflix query session.")
   
    #querying our netflix table
    data1_df =  session.query(tab1.Show_ID , tab1.Type , tab1.Title , tab1.Category , tab1.Date.Added , tab1.Rating , tab1.Director , Description ).all()

    #converting the results of our query to a dictionary
    #declaring a variable to hold our list 
    data1 = []
  
    #iterating through the rows 
    for   Show_ID , Type , Title , Category , Date_Added , Rating ,Director , Description  in data1_df:

        # declaring a variable to hold our dictionary
        data1_dict = {}

        #appending values to list of dictionaries.
        data1_dict["show_id"] = Show_ID
        data1_dict["Type"] = Type
        data1_dict["Title"]= Title
        data1_dict["Category"]= Category
        data1_dict["Date_Added"] = Date_Added
        data1_dict["Rating"] = Rating
        data1_dict["Director"] = Director
        data1_dict["Description"] = Description

       
        data1.append(data1_dict)

        #returning the list of dictionaries in a json format
        return jsonify(data1)

        print(f"Netflix query session completed ")

#defining our movie route
@app.route("/api/v1.0/movie")
def movie():

    session = Session(bind=engine)
    print(f" Starting the movie query session.")
    
    #querying the movie table
    data2_df = session.query(tab2.Title_ID , tab2.Title , tab2.Type  , tab2.Category , tab2.Date.Added , tab2.Rating , tab2.Description ).all()

      
    #declaring a variable to hold our list 
    data2 = []
  
    #iterating through the rows 
    for   Title_ID ,  Title , Type  , Category , Date_Added , Rating , Description  in data2_df:

        # declaring a variable to hold our dictionary
        data2_dict = {}

            #appending values to list of dictionaries.
        data2_dict["Title_id"] =  Title_ID
        data2_dict["Type"] = Type
        data2_dict["Title"]= Title
        data2_dict["Category"]= Category
        data2_dict["Date_Added"] = Date_Added
        data2_dict["Rating"] = Rating
        data2_dict["Description"] = Description

       
        data2.append(data2_dict)

        #returning the list of dictionaries in a json format
        return jsonify(data2)

        print(f"movie query session completed ")

# defining our title route
@app.route("/api/v1.0/title")
def title():

    print(f" Starting the title query session.")
    session = Session(bind=engine)
    #querying the title table
    data3_df = session.query(tab3.Show_ID , tab3.Title_ID , tab3.Title , tab3.Type ).all()

      
    #declaring a variable to hold our list 
    data3 = []
  
    #iterating through the rows 
    for   Show_ID , Title_ID ,  Title , Type   in data3_df:

        # declaring a variable to hold our dictionary
        data3_dict = {}

        #appending values to list of dictionaries.
        data3_dict["Show_ID"]= Show_ID
        data3_dict["Title_id"] = Title_ID
        data3_dict["Type"] = Type
        data3_dict["Title"]= Title
    
        data3.append(data3_dict)

        #returning the list of dictionaries in a json format
        return jsonify(data3)

        print(f"title query session completed ")

#defining our director route          
@app.route("/api/v1.0/director")
def director():

    session = Session(bind=engine)
 #querying the director
    data4_df =  session.query(tab4.Show_ID  , tab4.Title , tab4.Date_Added , tab4.Rating , tab4.IDs , tab4.First_Name , tab4.Last_Name ).all()

    #converting the results of our query to a dictionary
    #declaring a variable to hold our list 
    data4 = []
  
    #iterating through the rows 
    for   Show_ID ,  Title , Date_Added , Rating ,IDs, First_Name , Last_Name  in data4_df:

        # declaring a variable to hold our dictionary
        data4_dict = {}

        #appending values to list of dictionaries.
        data4_dict["show_id"] = Show_ID
        data4_dict["Title"]= Title
        data4_dict["Date_Added"] = Date_Added
        data4_dict["Rating"] = Rating
        data4_dict["IDs"] = IDs
        data4_dict["First_Name"] = First_Name
        data4_dict["Last_Name"] = Last_Name

        
        data4.append(data4_dict)

        #returning the list of dictionaries in a json format
    return jsonify(data4)

print(f"Netflix query session completed ")

print(f"session completed successfully.")
print(f"End of session!") 


if __name__ == "__main__":
    app.run(debug=True)

# --------------------------------------------------------------------------------


