# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('logistic_regression_model.pkl')

# 2. 모델 설명
st.title('물건 구입 비용과 만족도는 비례하는가')
st.subheader('돈을 많이 쓸수록 만족스러운가')
col1, col2,col3 = st.columns( 3 )
with col1:
 st.subheader('모델 설명')
 st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
 st.write(' - 학습 데이터 출처 : https://www.kaggle.com/datasets/uom190346a/e-commerce-customer-behavior-dataset?resource=download')
 st.write(' - 훈련 데이터 : 245건')
 st.write(' - 테스트 데이터 : 105건')
 st.write(' - 모델 정확도 : 0.62')

# 3. 데이터시각화
with col2:
 st.subheader('데이터시각화1')
 st.image('시각화1.png' )
with col3:
 st.subheader('데이터시각화2')
 st.image('시각화2.png')

# 4. 모델 활용
st.subheader('모델 활용')
st.write('****당신이 사용할 비용을 입력하세. 만족도를 예상해 드립니다')

a = st.number_input('금액입력', value=0.0)

if st.button('만족도분류'):
        input_data = [[ a ]]
        p = model.predict(input_data) 
        if p[0] == 1 :
              st.success('만족')
        if p[0] == 0 :
              st.success('그럭저럭')
        if p[0] == -1:
              st.success('불만족')
