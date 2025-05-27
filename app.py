import streamlit as st
import random

st.title("⚾ 간단한 야구 게임")

st.write("컴퓨터가 1부터 9까지 숫자 3개를 랜덤으로 선택합니다. 당신은 10번 안에 숫자와 순서를 맞춰야 합니다.")

# 상태 초기화
if 'target' not in st.session_state:
    st.session_state.target = random.sample(range(1, 10), 3)
    st.session_state.attempts = 0
    st.session_state.max_attempts = 10
    st.session_state.guessed = False
    st.session_state.history = []

user_input = st.text_input("1부터 9까지 숫자 3개를 공백으로 구분해서 입력하세요 (예: 1 5 9)")

def parse_input(text):
    try:
        nums = list(map(int, text.strip().split()))
        if len(nums) != 3:
            return None
        if any(n < 1 or n > 9 for n in nums):
            return None
        if len(set(nums)) != 3:
            return None
        return nums
    except:
        return None

if st.button("제출") and user_input and not st.session_state.guessed:
    guess = parse_input(user_input)
    if guess is None:
        st.error("잘못된 입력입니다. 1부터 9까지 중복 없는 숫자 3개를 입력하세요.")
    else:
        st.session_state.attempts += 1
        target = st.session_state.target
        strike = sum([1 for i in range(3) if guess[i] == target[i]])
        ball = len(set(guess) & set(target)) - strike
        st.session_state.history.append({"guess": guess, "strike": strike, "ball": ball})

        st.write(f"스트라이크: {strike}  볼: {ball}")
        
        remaining = st.session_state.max_attempts - st.session_state.attempts
        st.write(f"남은 기회: {remaining}번")

        if strike == 3:
            st.success(f"축하합니다! {st.session_state.attempts}번 만에 맞히셨습니다! 🎉")
            st.session_state.guessed = True
        elif st.session_state.attempts >= st.session_state.max_attempts:
            st.error(f"기회가 모두 소진되었습니다. 정답은 {target} 입니다.")
            st.session_state.guessed = True

if st.session_state.history:
    st.subheader("지금까지 입력한 숫자와 결과")
    for i, record in enumerate(st.session_state.history, 1):
        guess = record.get('guess', [])
        strike = record.get('strike', 0)
        ball = record.get('ball', 0)
        st.write(f"{i}번째 시도: 숫자 {guess} → 스트라이크: {strike}, 볼: {ball}")

if st.session_state.guessed:
    if st.button("다시 하기"):
        st.session_state.target = random.sample(range(1, 10), 3)
        st.session_state.attempts = 0
        st.session_state.guessed = False
        st.session_state.history = []
