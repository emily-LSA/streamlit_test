# app.py
import streamlit as st

st.set_page_config(layout="wide")
st.title('Set Title!!!')

# input_user_name = st.text_input(label="User Name", value="")
# input_password = st.text_input(label="Password", value="")

# 상단 로그인
con_id, con_pw, con_button = st.columns([0.2, 0.2, 0.6])

with con_id:
    input_user_name = st.text_input(label="User Name", value="")
with con_pw:
    input_password = st.text_input(label="Password", value="")
with con_button:
    confirm_button = st.button("Confirm")

if (input_password == "mezzo"):
    con = st.container()
    con.write(f"안녕하세요, {str(input_user_name)}님.")
    
    tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

    with tab1:
      #tab A 를 누르면 표시될 내용
      st.write('hello')

    with tab2:
      #tab B를 누르면 표시될 내용 
      st.write('hi')

else:
    con = st.container()
    con.write("비밀번호가 틀렸습니다. 확인 후 다시 입력해주세요.")
    
    
    
    
