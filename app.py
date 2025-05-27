import streamlit as st

# MBTI 설명 데이터\
mbti_descriptions = {
    "INTJ": "INTJ (전략가): 창의적이고 전략적인 사색가로, 항상 더 나은 방법을 찾고 문제를 해결하려 합니다.",
    "INTP": "INTP (논리술사): 혁신적이고 호기심 많은 사색가로, 논리와 분석을 통해 세상을 이해하려고 합니다.",
    "ENTJ": "ENTJ (지휘관): 대담하고 상상력이 풍부하며 의지가 강한 리더로, 어려운 목표도 달성하려 합니다.",
    "ENTP": "ENTP (변론가): 영리하고 호기심 많은 사색가로, 지적으로 도전하는 걸 좋아합니다.",
    "INFJ": "INFJ (옹호자): 조용하고 신비로우며 통찰력이 뛰어난 이상주의자입니다.",
    "INFP": "INFP (중재자): 열정적이고 충성스러운 이상주의자이며, 깊은 감정을 가지고 있습니다.",
    "ENFJ": "ENFJ (선도자): 카리스마 있고 영감을 주며, 다른 사람들을 돕는 데 열정적입니다.",
    "ENFP": "ENFP (활동가): 열정적이고 창의적이며, 자유로운 정신을 가진 낙천주의자입니다.",
    "ISTJ": "ISTJ (현실주의자): 책임감 있고 실용적이며, 사실과 세부사항을 중시합니다.",
    "ISFJ": "ISFJ (수호자): 헌신적이고 따뜻하며, 다른 사람들을 돕는 데 기쁨을 느낍니다.",
    "ESTJ": "ESTJ (경영자): 실용적이고 사실적이며, 사회의 질서를 유지하는 데 능숙합니다.",
    "ESFJ": "ESFJ (집정관): 사교적이고 협조적이며, 다른 사람들의 감정과 욕구를 잘 이해합니다.",
    "ISTP": "ISTP (장인): 호기심 많고 유연하며, 직접 경험을 통해 배우기를 좋아합니다.",
    "ISFP": "ISFP (모험가): 호기심 많고 예술적인 성향을 가지며, 감각을 즐깁니다.",
    "ESTP": "ESTP (사업가): 에너지 넘치고 솔직하며, 도전을 즐기는 성격입니다.",
    "ESFP": "ESFP (연예인): 사교적이고 재밌으며, 사람들과 함께 즐거운 시간을 보내는 걸 좋아합니다."
}

st.title("MBTI 성격 유형 설명 앱")

# 사용자에게 MBTI 선택 받기
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_descriptions.keys()))

# 선택된 MBTI에 대한 설명 보여주기
if selected_mbti:
    st.subheader(f"{selected_mbti} 유형 설명")
    st.write(mbti_descriptions[selected_mbti])

import streamlit as st

st.title("🔐 탈출 게임")

# 게임 상태 초기화
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# 스테이지 1
def stage1():
    st.subheader("1단계: 방 안에서 깨어났다")
    st.write("당신은 작은 방 안에 있습니다. 문은 잠겨 있고, 책상이 하나 보입니다.")
    choice = st.radio("무엇을 할까요?", ["책상 조사하기", "문 열어보기", "창문 살펴보기"])
    
    if choice == "책상 조사하기":
        st.write("책상 서랍 안에서 열쇠를 찾았습니다!")
        st.session_state.stage = 2
    elif choice == "문 열어보기":
        st.write("문은 잠겨 있습니다. 다른 걸 찾아봐야겠어요.")
    else:
        st.write("창문은 너무 높아서 열 수 없습니다.")

# 스테이지 2
def stage2():
    st.subheader("2단계: 잠긴 문")
    st.write("열쇠를 들고 문 앞에 섰습니다. 열쇠로 문을 열까요?")
    if st.button("열쇠로 문 열기"):
        st.session_state.stage = 3
    else:
        st.write("아직 준비가 안 되셨나요?")

# 스테이지 3
def stage3():
    st.subheader("3단계: 복도")
    st.write("문을 열고 나가니 긴 복도가 있습니다. 왼쪽에는 계단, 오른쪽에는 또 다른 문이 있습니다.")
    choice = st.radio("어디로 갈까요?", ["계단 내려가기", "오른쪽 문 들어가기"])
    
    if choice == "계단 내려가기":
        st.write("계단 아래로 내려가 탈출에 성공했습니다! 🎉")
        st.session_state.stage = 4
    else:
        st.write("문 안에는 아무것도 없네요. 돌아갑니다.")

# 스테이지 4 (게임 클리어)
def stage4():
    st.success("축하합니다! 게임을 클리어했습니다.")
    if st.button("처음부터 다시 하기"):
        st.session_state.stage = 1

# 게임 진행
if st.session_state.stage == 1:
    stage1()
elif st.session_state.stage == 2:
    stage2()
elif st.session_state.stage == 3:
    stage3()
elif st.session_state.stage == 4:
    stage4()
