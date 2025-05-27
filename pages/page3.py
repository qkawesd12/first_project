import streamlit as st

st.title("🧑‍💻 심화 코딩 실력 테스트")

questions = [
    {
        "question": "1. Python에서 리스트를 만드는 방법 중 올바른 것은?",
        "type": "mcq",
        "options": ["a) [1, 2, 3]", "b) (1, 2, 3)", "c) {1, 2, 3}"],
        "answer": "a",
        "explanation": "리스트는 대괄호 []를 사용해 만듭니다."
    },
    {
        "question": "2. 변수 x에 5를 더하는 Python 코드를 고르세요.",
        "type": "mcq",
        "options": ["a) x + 5", "b) x = x + 5", "c) add(x,5)"],
        "answer": "b",
        "explanation": "변수에 값을 더하려면 대입 연산자를 사용해야 합니다."
    },
    {
        "question": "3. 'Hello World'를 출력하는 Python 함수 이름은?",
        "type": "text",
        "answer": "print",
        "explanation": "'print' 함수는 화면에 문자열을 출력합니다."
    },
    {
        "question": "4. Python에서 반복문을 시작하는 키워드는?",
        "type": "text",
        "answer": "for",
        "explanation": "반복문은 'for'나 'while'로 시작합니다. 여기서는 'for'가 정답입니다."
    },
    {
        "question": "5. Python의 딕셔너리 생성 방법으로 옳은 것은?",
        "type": "mcq",
        "options": ["a) {'key': 'value'}", "b) ['key', 'value']", "c) ('key', 'value')"],
        "answer": "a",
        "explanation": "딕셔너리는 중괄호와 key:value 쌍으로 만듭니다."
    }
]

# 초기화
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False

q = questions[st.session_state.current_q]

st.subheader(q["question"])

user_ans = None

if q["type"] == "mcq":
    user_ans = st.radio("정답을 선택하세요:", q["options"])
elif q["type"] == "text":
    user_ans = st.text_input("정답을 입력하세요:")

def normalize_answer(ans):
    if isinstance(ans, str):
        if ') ' in ans:
            return ans.split(') ')[0].strip().lower()
        return ans.strip().lower()
    return ans

submit_clicked = st.button("제출")

if submit_clicked and not st.session_state.answered:
    if user_ans is None or (q["type"] == "text" and user_ans.strip() == ""):
        st.warning("답변을 입력하거나 선택해주세요.")
    else:
        st.session_state.answered = True
        correct_ans = q["answer"].lower()
        if q["type"] == "mcq":
            selected = normalize_answer(user_ans)
        else:
            selected = user_ans.strip().lower()

        if selected == correct_ans:
            st.success("정답입니다! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"틀렸습니다. 정답은 '{q['answer']}' 입니다.")
        st.write(f"해설: {q['explanation']}")

if st.session_state.answered:
    # '다음 문제' 버튼과 '처음부터 다시하기' 버튼을 동시에 띄우지 않음
    if st.session_state.current_q < len(questions) - 1:
        next_clicked = st.button("다음 문제")
        if next_clicked:
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.experimental_rerun()
            st.stop()
    else:
        restart_clicked = st.button("처음부터 다시하기")
        if restart_clicked:
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.experimental_rerun()
            st.stop()

if st.session_state.current_q == len(questions):
    st.info(f"모든 문제를 완료했습니다! 최종 점수: {st.session_state.score} / {len(questions)}")
