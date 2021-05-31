import numpy as np
from flask import Flask, request, jsonify, render_template
import pandas as pd
from numpy import genfromtxt
import ast


app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():
    
    def helper():
        no_neighbor = 0
        user_merch = pd.read_csv("user_merch.csv", index_col = None)
        df4U = pd.read_csv('df4U.csv')
        users_train = genfromtxt('users_train.csv', delimiter=',')
        users_train = [int(i) for i in users_train]


        #user = [int(x) for x in request.form.values()]
        #user = user[0]
        user = 92267
        user_merch.columns = [int(i) for i in user_merch.columns]
        for col in user_merch.columns:
            user_merch[col] = ast.literal_eval(user_merch[col][0])[0]

        if user in users_train:
            if user in user_merch.keys():
                predictions = user_merch[user][0]
                return predictions
            else:
                if user in df4U['user_id'].unique():
                    nearest_user = get_nearest_user(user,df4U)
                    c3 +=1
                    while nearest_user:
                        u = nearest_user.pop(0)
                        if u in user_merch.keys():
                            predictions =user_merch[u][0] 
                            return predictions
                else:
                    predictions = most_frequent_merchant
                    return predictions
        else:
            predictions = most_frequent_merchant
            return predictions
    
    output = str(helper())
    return render_template('index.html', prediction_text='Predicted Merchant {}'.format(str(output)))


    




if __name__ == "__main__":
    app.run(debug=True)
    