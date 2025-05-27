import streamlit as st

st.title("🧑‍💻 심화 코딩 실력 테스트")

st.write("""
여러 유형의 문제를 풀면서 코딩 기초부터 실전 감각까지 키워보세요!
""")

# 문제 리스트: type='mcq'는 객관식, 'text'는 단답형
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

# 세션 상태 초기화
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = None

q = questions[st.session_state.current_q]

st.subheader(q["question"])

user_ans = None

if q["type"] == "mcq":
    # 객관식 문제
    user_ans = st.radio("정답을 선택하세요:", q["options"])
elif q["type"] == "text":
    user_ans = st.text_input("정답을 입력하세요:")

def normalize_answer(ans):
    # 객관식 선택지에서 'a) ' 같은 접두어 제거
    if isinstance(ans, str):
        if ') ' in ans:
            return ans.split(') ')[0].strip().lower()
        return ans.strip().lower()
    return ans

if st.button("제출") and not st.session_state.answered:
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
    if st.session_state.current_q + 1 < len(questions):
        if st.button("다음 문제"):
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.session_state.user_answer = None
            st.experimental_rerun()
    else:
        st.info(f"모든 문제를 완료했습니다! 최종 점수: {st.session_state.score} / {len(questions)}")
        if st.button("처음부터 다시하기"):
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.experimental_rerun()
