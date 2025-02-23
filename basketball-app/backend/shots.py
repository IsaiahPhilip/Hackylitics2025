from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
import uuid
from sqlalchemy import String, Integer, Float 
from sqlalchemy.sql.expression import func
from webscraping import get_player_info
import pandas as pd 
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basketball_loc.db'
db = SQLAlchemy(app)

CORS(app) #Enable CORS for all routes 

#Read csv
csv_filename = "2024shotpct.csv"
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
data_dir = os.path.join(parent_dir, "data")
shot_pct = os.path.join(data_dir,csv_filename)

df = pd.read_csv(shot_pct)


class LocBasketball(db.Model):
    id = db.Column(String(36), primary_key = True, default = lambda:str (uuid.uuid4())) # main distinguishing factor
    year  = db.Column(Integer, nullable = False)
    loc_x = db.Column(Integer,nullable = False)
    loc_y = db.Column(Integer, nullable = False)
    percentage = db.Column(Float,default=0)
    
    def __repr__(self):
        return f"<User {str(self.id)}"
        
with app.app_context(): 
   db.create_all() #Create tables if they do not exist 
   
   #Iterate over df and add each row to db
   for index,row in df.iterrows(): 
       new_record = LocBasketball(year=row["SEASON_1"], loc_x=row["LOC_X"],loc_y=row["LOC_Y"],percentage=row["SHOT_PCT"])
       db.session.add(new_record)
   db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def get_data(): 
    if request.method == 'POST':
        data2 = request.get_json()
        x = round(25 - round(data2.get('y')) / 10)
        y = round(round(data2.get('x')) / 10)
        print(f"Received position: x={x}, y={y}")
        return jsonify({"message": "Position received successfully", "x": x, "y": y})

    elif request.method == 'GET':
        x_param = request.args.get('x')
        y_param = request.args.get('y')
        if x_param is not None and y_param is not None: 
            x = int(round(25 - round(float(y_param)) / 10))
            y = int(round(round(float(x_param)) / 10))
            if x is not None and y is not None:
                basketball_record = LocBasketball.query.filter_by(loc_x=x, loc_y=y).first()
                if basketball_record:
                    data = {
                        "id": basketball_record.id,
                        "year": basketball_record.year,
                        "loc_x": basketball_record.loc_x,
                        "loc_y": basketball_record.loc_y,
                        "percentage": f"{round(basketball_record.percentage * 100,0)}%"
                    }
                    return jsonify(data)
                else:
                    return jsonify({"percentage": "?"}), 404
        else:
            return jsonify({"message": "x and y parameters are required"}), 400

    return jsonify({"message": "Invalid request method"}), 405

if __name__ == '__main__':
    app.run(debug = True)