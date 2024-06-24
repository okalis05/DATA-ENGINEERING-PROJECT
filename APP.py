
#import sqlalchemy
from flask import Flask , jsonify
import pandas as pd
import sqlite3
#################################################
# Flask Setup
#################################################

app = Flask(__name__)

################################################
# Database Setup
#################################################

#define a function to connect to the database
def connection():
    return
    sqlite3.connect("sqlite:////Users/francoiseelismbazoaokala/Documents/projects/DATA-ENGINEERING-PROJECT/streaming.sqlite")

#defining our flask routes
@app.route("/")
def Welcome():

    print(f"Welcome to our  Presentation!")
    #list of all the routes.
    return(
           f"Available Routes:<br/>"
           f"/api/v1.0/<br/>"
           f"/api/v1.0/netflix<br/>"
           f"/api/v1.0/movie<br/>"
           f"/api/v1.0/title<br/>"
           f"/api/v1.0/director<br/>"
           )

#Defining our netflix route
@app.route("/api/v1.0/netflix" , methods = ["GET"])
def netflix():
    print(f"Starting netflix query session ")
    
    #Establish the connection
    conn = connection()

    #querying all from the netflix table
    df1 = pd.read_sql_query("SELECT*FROM netflix ", conn)


    #close the connection
    conn.close()

    #returning the query results as a json file
    return jsonify(df1.to_dict(orient='records'))

   
    print(f"netflix table query successfully completed!")

#Defining our movie route
@app.route("/api/v1.0/movie" , methods = ["GET"])
def movie():
    print(f"Starting movie query session ")

    #Establish the connection
    conn = connection()

    #querying all from the movie table
    df2 = pd.read_sql_query("SELECT*FROM movie", conn)

    #close the connection
    conn.close()
   
    #returning the query results as a json file
    return jsonify(df2.to_dict(orient='records'))

   
    print(f"End of session!")

#Defining our title route
@app.route("/api/v1.0/title" , methods = ["GET"])
def title():
    print(f"Starting title query session ")

    #Establish the connection
    conn = connection()

     #querying all from the title table
    df3 = pd.read_sql_query("SELECT*FROM title ", conn)

    #close the connection
    conn.close()

    #returning the query results as a json file
    return jsonify(df3.to_dict(orient='records'))
    

    print(f"End of session!")

#Defining our director route
@app.route("/api/v1.0/director" , methods = ["GET"])
def director():
    print(f"Starting director query session ")

    #Establish the connection
    conn = connection()

    #querying all from the director table
    df4 = pd.read_sql_query("SELECT*FROM director ", conn)

    #close the connection
    conn.close()

    #returning the query results as a json file
    return jsonify(df4.to_dict(orient='records'))

   
    print(f"End of session!")
    

if __name__ == "__main__":
    app.run(debug=True)
