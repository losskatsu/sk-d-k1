import streamlit as st
import requests
import json

# API_URL = "http://127.0.0.1:5000/rec_nick" #로컬 테스트
API_URL = "http://flaskapi:5000/rec_nick" #로컬 테스트

def get_nickname(mbti, best_num):
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"mbti": [mbti], "best_num": [best_num]})
    
    try:
        response = requests.post(API_URL, data=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result.get("nick", "닉네임을 가져오는 데 실패했습니다.")
        else:
            return "서버 응답 오류: " + str(response.status_code)
    except requests.exceptions.RequestException as e:
        return "요청 오류: " + str(e)

# Streamlit UI
st.title("닉네임 추천기")

mbti = st.text_input("당신의 MBTI는?")
best_num = st.text_input("당신이 좋아하는 숫자는?")

if st.button("닉네임 추천받기"):
    if mbti and best_num:
        nickname = get_nickname(mbti, best_num)
        st.success(f'추천 닉네임은 "{nickname}"입니다')
    else:
        st.warning("모든 항목을 입력해주세요.")
