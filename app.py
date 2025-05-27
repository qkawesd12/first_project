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
import numpy as np
import time

# 미로 맵 설정 (0: 길, 1: 벽, 2: 출발, 3: 탈출)
maze = np.array([
    [1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 1, 3, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
])

# 현재 위치 찾기
def find_position(value):
    pos = np.where(maze == value)
    return pos[0][0], pos[1][0]

# 초기 위치
if 'player_pos' not in st.session_state:
    st.session_state.player_pos = find_position(2)

# 이동 함수
def move_player(direction):
    row, col = st.session_state.player_pos
    if direction == '위': row -= 1
    elif direction == '아래': row += 1
    elif direction == '왼쪽': col -= 1
    elif direction == '오른쪽': col += 1

    if maze[row, col] != 1:
        st.session_state.player_pos = (row, col)

# 미로 출력
def render_maze():
    display = ''
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            if (i, j) == st.session_state.player_pos:
                display += '🧍 '
            elif maze[i, j] == 1:
                display += '⬛ '
            elif maze[i, j] == 0:
                display += '⬜ '
            elif maze[i, j] == 2:
                display += '🚪 '
            elif maze[i, j] == 3:
                display += '🏁 '
        display += '\n'
    st.text(display)

st.title("🌀 미로 탈출 게임")
render_maze()

# 방향 버튼
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('⬆️ 위'):
        move_player('위')
with col2:
    pass
with col3:
    if st.button('⬇️ 아래'):
        move_player('아래')

col4, col5, col6 = st.columns([1,1,1])
with col4:
    if st.button('⬅️ 왼쪽'):
        move_player('왼쪽')
with col5:
    pass
with col6:
    if st.button('➡️ 오른쪽'):
        move_player('오른쪽')

# 탈출 성공 여부 확인
if maze[st.session_state.player_pos] == 3:
    st.success("축하합니다! 미로를 탈출했습니다! 🎉")
    if st.button("처음부터 다시하기"):
        st.session_state.player_pos = find_position(2)
