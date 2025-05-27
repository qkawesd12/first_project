import streamlit as st
import random

st.title("🎲 숫자 맞히기 게임")

# 초기 상태 설정
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0

st.write("1부터 100 사이의 숫자를 맞혀보세요!")

# 사용자 입력
guess = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1)

if st.button("제출"):
    st.session_state.attempts += 1
    if guess < st.session_state.target:
        st.info("너무 작아요! 더 큰 숫자를 시도해보세요.")
    elif guess > st.session_state.target:
        st.info("너무 커요! 더 작은 숫자를 시도해보세요.")
    else:
        st.success(f"축하합니다! {st.session_state.attempts}번 만에 정답을 맞혔습니다 🎉")
        if st.button("처음부터 다시하기"):
            st.session_state.target = random.randint(1, 100)
            st.session_state.attempts = 0
