from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
import uuid
from sqlalchemy import String, Integer, Float 
from sqlalchemy.sql.expression import func
from webscraping import get_player_info
#from data import point_shot
import pandas as pd 
import zipfile


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basketball_loc.db'
db = SQLAlchemy(app)

CORS(app) #Enable CORS for all routes 

#Decompressing zip and getting CSV 
# zip_file_path = "basketball-app/data/NBA_2024_Shots 2.csv.zip"
# csv_file_name = "NBA_2024_Shots.csv"

# with zipfile.ZipFile(zip_file_path,'r') as zip_ref: 
#     zip_ref.extractall("basketball-app/data/")


class LocBasketball(db.Model):
    id = db.Column(String(36), primary_key = True, default = lambda:str (uuid.uuid4())) # main distinguishing factor
    year  = db.Column(Integer, nullable = False)
    loc_x = db.Column(Integer,nullable = False)
    loc_y = db.Column(Integer, nullable = False)
    percentage = db.Column(Float)
    
    def __repr__(self):
        return f"<User {str(self.id)}"
        
with app.app_context(): 
   db.create_all() #Create tables if they do not exist 
   new_user = LocBasketball(year=2024, loc_x = 4, loc_y = 35, percentage = 0.28)
   another_user = LocBasketball(year=2024, loc_x = 3, loc_y = 33, percentage = 0.30)
   db.session.add(new_user)
   db.session.add(another_user)
   db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def get_data(): 
    #Modify to return a single random record 
    if request.method == 'GET':
        # Return a single random record
        random_loc = LocBasketball.query.order_by(func.random()).first() 
        data = {
            "id": random_loc.id, 
            "year": random_loc.year, 
            "loc_x": random_loc.loc_x,
            "loc_y": random_loc.loc_y,
            "percentage": random_loc.percentage
        }
        return jsonify(data)

    elif request.method == 'POST':
        data2 = request.get_json()
        print(data2)

        x = round(25 - round(data2.get('y'))/10)
        y = round(round(data2.get('x'))/10)
        print(f"Received position: x={x}, y={y}")
        return jsonify({"message": "Position received successfully"})
if __name__ == '__main__':
    app.run(debug = True)