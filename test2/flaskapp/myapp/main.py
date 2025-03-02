import numpy as np
from sklearn.linear_model import LinearRegression
import psycopg2

from flask import Flask, request, jsonify

app = Flask(__name__)

# 학습
np.random.seed(0)
X = np.random.rand(10, 1)
y = 2 * X + 1 + 0.1 * np.random.randn(10, 1)

model = LinearRegression()
model.fit(X, y)

@app.route('/')
def welcome():
    return 'HELLO, ML API SERVER'



@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    new_X = data['input']
    new_X_val = float(new_X[0])
    input_X = np.array(new_X_val).reshape(1, -1)
    y_pred = model.predict(input_X)
    y_pred_list = y_pred.tolist()
    y_pred_val = round(y_pred_list[0][0], 5)

    conn = psycopg2.connect(dbname='ml', user='postgres', password='postgres', host='127.0.0.1', port=5432)
    cur = conn.cursor()
    query = "INSERT INTO pred_result (input, output) VALUES (%s, %s)"
    values = (new_X_val, y_pred_val)
    cur.execute(query, values)
    conn.commit()
    cur.close()
    conn.close()

    res = jsonify({'input': new_X_val, 'predicted_output': y_pred_val})
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

