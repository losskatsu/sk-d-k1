import psycopg2
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# PostgresSQL 연결 정보
DB_CONFIG = {
    "dbname": "ml",
    "user": "postgres",
    "password": "postgres",
    "host": "postgres",
    "port": "5432"
}

def save_to_db(mbti, best_num, nick):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        query = """
        INSERT INTO user_nick (DT, MBTI, BEST_NUM, REC_NICK) 
        VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (datetime.now(), mbti, best_num, nick))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"DB 저장 오류: {e}")

@app.route('/')
def welcome():
    return 'THIS IS API SERVER'

@app.route('/rec_nick', methods=['POST'])
def rec_nick():
    data = request.json
    mbti_val = data['mbti'][0]
    best_num_val = int(data['best_num'][0])
    nick_val = mbti_val + str(best_num_val)

    save_to_db(mbti_val, best_num_val, nick_val)
    
    res = jsonify({'mbti': mbti_val, 'best_num': best_num_val, 'nick': nick_val})
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



