import streamlit as st

st.title("💻 나에게 맞는 IT 진로 추천 앱")

st.write("""
안녕하세요! 몇 가지 질문에 답하면 당신에게 어울리는 IT 분야 직업을 추천해드립니다.
""")

# 질문 1: 관심 분야
interest = st.selectbox(
    "1. 가장 관심 있는 분야는 무엇인가요?",
    ["프로그래밍 / 소프트웨어 개발", "데이터 분석 / 인공지능", "네트워크 / 보안", "디자인 / UI/UX", "IT 컨설팅 / 기획"]
)

# 질문 2: 업무 스타일
style = st.radio(
    "2. 어떤 업무 스타일을 선호하시나요?",
    ["문제를 논리적으로 해결하는 것", "데이터와 숫자를 다루는 것", "시스템을 설계하고 관리하는 것", "창의적이고 시각적인 작업", "사람들과 협업하고 조율하는 것"]
)

# 질문 3: 선호하는 근무 환경
environment = st.selectbox(
    "3. 선호하는 근무 환경은?",
    ["팀과 협력하며 일하기", "혼자 집중해서 일하기", "현장에서 시스템을 직접 관리하기", "프로젝트를 기획하고 조율하기", "새로운 기술 연구 및 적용하기"]
)

def recommend_job(interest, style, environment):
    # 간단한 추천 로직 (예시)
    if interest == "프로그래밍 / 소프트웨어 개발":
        if style == "문제를 논리적으로 해결하는 것":
            return "소프트웨어 개발자 / 백엔드 개발자"
        elif style == "창의적이고 시각적인 작업":
            return "프론트엔드 개발자 / UI 개발자"
        else:
            return "풀스택 개발자"

    elif interest == "데이터 분석 / 인공지능":
        if style == "데이터와 숫자를 다루는 것":
            return "데이터 분석가 / 데이터 사이언티스트"
        elif environment == "새로운 기술 연구 및 적용하기":
            return "AI 연구원 / 머신러닝 엔지니어"
        else:
            return "빅데이터 엔지니어"

    elif interest == "네트워크 / 보안":
        if environment == "현장에서 시스템을 직접 관리하기":
            return "네트워크 엔지니어 / 시스템 관리자"
        else:
            return "정보보안 전문가"

    elif interest == "디자인 / UI/UX":
        return "UI/UX 디자이너 / 웹 디자이너"

    elif interest == "IT 컨설팅 / 기획":
        if style == "사람들과 협업하고 조율하는 것":
            return "IT 프로젝트 매니저 / IT 컨설턴트"
        else:
            return "비즈니스 애널리스트"

    return "다양한 IT 직무를 탐색해 보세요!"

if st.button("진로 추천 받기"):
    job = recommend_job(interest, style, environment)
    st.success(f"👉 추천 IT 직무: {job}")

