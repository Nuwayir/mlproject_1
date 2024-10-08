# using flask : 
# copy of app file for deployment purposess
import pickle
from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomeData,Predict_pipline
# flask need to know about it :
# entery point to executed 
application=Flask(__name__)

app=application
# Route to a home page 

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():# call this method in home.html
    if request.method=='GET':
        return render_template('home.html')# contain simple data to be provided to get the predictions 
    else: # post need more work as we have done in other files ....
        data=CustomeData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )      # --> in predict_pipline file 

        pred_df=data.get_data_as_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=Predict_pipline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    
# beacuse i had an issue beacuse of the prot it 
# says 5000 port is in use so that's way i change it to this 
if __name__ == "__main__":
    app.run(port=5001)  # Change to a different port
    
#remove debuge while doing hte deployment !! part 9  

# Make sure you're accessing the correct URL in the browser:
# http://127.0.0.1:5001
#http://127.0.0.1:5001/predictdata
# i had issue with this path 'artifacts\model.pkl' so the solution is to replace it with this -> 'artifacts/model.pkl'
# notice / the solution 
