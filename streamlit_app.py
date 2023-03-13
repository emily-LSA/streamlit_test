# app.py
import streamlit as st

st.title('streamlit test!')

input_user_name = st.text_input(label="User Name", value="default value")
input_password = st.text_input(label="Password", value="default value")

if (st.button("Confirm")) & (input_password != "mezzo"):
    con = st.container()
    con.write("비밀번호가 틀렸습니다. 확인 후 다시 입력해주세요.")

elif (st.button("Confirm")) & (input_password == "mezzo"):
    con = st.container()
    con.caption("Result")
    con.write(f"Hello~ {str(input_user_name)}")

#     tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

#     with tab1:
#       #tab A 를 누르면 표시될 내용
#       st.write('hello')

#     with tab2:
#       #tab B를 누르면 표시될 내용 
#       st.write('hi')
