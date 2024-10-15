
import streamlit as st
from PIL import Image

st.write('Hello, *World!* :sunglasses:') # 해당 내용을 수정해서 사이트를 자유롭게 꾸밀 수 있다.

st.title('this is title')
st.header('this is header')
st.subheader('this is subheader')

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

with tab1:
  #tab A 를 누르면 표시될 내용
  st.write('hello')
    
with tab2:
  #tab B를 누르면 표시될 내용 
  st.write('hi')

#PIL 패키지에 이미지 모듈을 통해 이미지 열기 
# Image.open('이미지 경로')
img = Image.open('img.jpg')

col1,col2 = st.columns([2,3])

with col1 :
  # column 1 에 담을 내용
  st.title('column1')
with col2 :
  # column 2 에 담을 내용
  st.title('column2')
  st.checkbox(' 체크박스 ')


# 컬럼2에 불러온 사진 표시하기
col2.image(img)
