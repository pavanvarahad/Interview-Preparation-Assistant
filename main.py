import streamlit as st
import langchain_helper as lh
import time

st.set_page_config(
    page_title="Software Engineer Interview Preparation",
    page_icon="💻",
    layout="centered",
)

st.title('Software Engineer Interview Preparation Assistant')

topics = [
    "Algorithms",
    "Data Structures",
    "System Design",
    "Database Management",
    "Object-Oriented Programming",
    "Networking",
    "Operating Systems",
    "Software Engineering Principles"
]
selected_topic = st.selectbox("Select a Topic", topics)
difficulty = st.radio("Select Difficulty Level", ("Easy", "Medium", "Hard"))

if selected_topic and difficulty:
    if st.button('Generate Question'):
        with st.spinner('Generating question...'):
            response = lh.generate_interview_preparation(selected_topic, difficulty)
            
            st.session_state.question = response['question']
            st.session_state.answer = response['answer']
            
            st.subheader('Question:')
            st.write(st.session_state.question)
    
    # Button to show answer
    if st.button('Show Answer'):
        if 'question' in st.session_state:
            st.subheader('Question:')
            st.write(st.session_state.question)
        
        st.subheader('Answer:')
        st.write(st.session_state.answer)
