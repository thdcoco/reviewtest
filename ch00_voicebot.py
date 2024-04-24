#API 키: 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


import streamlit as st
from datetime import datetime 
import openai
import numpy as np

###메인함수
def main():
    # 기본 설정
    st.set_page_config(
        page_title="송채빈의 웹개발",
        layout="wide")


    # session state 초기화
    if "chat" not in st.session_state:
        st.session_state["chat"] = []

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "system", "content": "You are a thoughtful assistant. Respond to all input in 25 words and answer in Korean."}]
    
    # 제목
    st.header("송채빈은 시험중")
    # 구분선
    st.markdown("---")
    # 기본 설명
    with st.expander("송채빈의 웹 개발에 대하여", expanded=True):
        st.write(
        """
        -송채빈은 지금 중간고사 중"""
        )

        st.markdown("")
        # 사이드바 생성
        with st.sidebar:
            # Open AI API 키 입력받기
            openai.api_key = st.text_input(label="OPENAI API 키", placeholder="Enter your API Key", value="", type="password")

            st.markdown("---")

            # 모델 선택
            model = st.radio(label="GPT 모델", options=["gpt-4", "gpt-3.5-turbo"])

            st.markdown("---")

            # 리셋 버튼 생성
            if st.button(label="초기화"):
                # 리셋 코드
                st.session_state["chat"] = []
                
        # 기능 구현 공간
        col1, col2 = st.columns(2)
        with col1:
            # 왼쪽 영역 작성
            st.subheader("질문하기")
            question = st.text_input("질문을 입력하세요")
            if st.button("질문"):
                # 질문을 채팅에 추가
                if question:
                    now = datetime.now().strftime("%H:%M")
                    st.session_state["chat"].append(("user", now, question))
                    
        with col2:
            # 오른쪽 영역 작성
            st.subheader("질문/답변")
            # 채팅 표시
            if "message" in st.session_state:  
                response = ask_gpt(st.session_state["message"], model)

            # 답변 얻기
                response = ask_gpt(question, model)
                    # 답변을 채팅에 추가
                now = datetime.now().strftime("%H:%M")
                st.session_state["chat"].append(("bot", now, response))


                # GPT 모델에 넣을 프롬포트를 위해 답변 내용 저장
                st.session_state["messages"] = st.session_state["messages"] + [{"role": "system", "content": response}] 
                
                for sender, time, message in st.session_state["chat"]:
                    if sender == "user":
                        st.write(f'<div style="display:flex;align-items:center;"><div style="background-color:#007AFF;color:white;border-radius:12px;padding:8px 12px;margin-right:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                        st.write("")
                    else:
                        st.write(f'<div style="display:flex;align-items:center;justify-content:flex-end;"><div style="background-color:lightgray;border-radius:12px;padding:8px 12px;margin-left:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                        st.write("")
if __name__ == "__main__":
    main()
