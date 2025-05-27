import streamlit as st

st.title("💻 간단한 코딩 실력 테스트")

st.write("아래 문제에 맞는 답을 입력해 보세요. 숫자나 단어 형태의 정답을 입력하면 됩니다.")

questions = [
    {
        "question": "1. Python에서 리스트를 만드는 방법 중 올바른 것은? (보기: a) [1,2,3], b) (1,2,3), c) {1,2,3})",
        "answer": "a"
    },
    {
        "question": "2. 변수 x에 5를 더하는 코드는?",
        "answer": "x = x + 5"
    },
    {
        "question": "3. 'Hello World'를 출력하는 Python 함수 이름은?",
        "answer": "print"
    }
]

if 'score' not in st.session_state:
    st.session_state.score = 0

if 'current_q' not in st.session_state:
    st.session_state.current_q = 0

def check_answer(user_ans, correct_ans):
    return user_ans.strip().lower() == correct_ans.strip().lower()

if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    st.write(q["question"])
    user_input = st.text_input("답을 입력하세요:")

    if st.button("제출"):
        if check_answer(user_input, q["answer"]):
            st.success("정답입니다!")
            st.session_state.score += 1
        else:
            st.error(f"틀렸습니다. 정답은 '{q['answer']}' 입니다.")
        st.session_state.current_q += 1
        st.experimental_rerun()
else:
    st.write(f"테스트 종료! 총 점수는 {st.session_state.score} / {len(questions)} 점 입니다.")
    if st.button("처음부터 다시하기"):
        st.session_state.score = 0
        st.session_state.current_q = 0
        st.experimental_rerun()
