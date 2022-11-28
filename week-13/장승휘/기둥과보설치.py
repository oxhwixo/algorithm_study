# 현재 설치된 구조물이 가능한 구조물인지 판단
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥인 경우
            # 바닥 위 or 보의 한쪽 끝 부분 위 or 다른 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1: # 보인 경우
            # 한쪽 끝부분이 기둥 위 or 양쪽 끝부분이 다른 보와 동시에 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # frame의 개수 최대 1000
        x, y, stuff, operate = frame
        if operate == 0: # 삭제
            answer.remove([x, y, stuff]) # 일단 삭제
            if not possible(answer): # 가능한지 확인
                answer.append([x, y, stuff]) # 불가능하면 다시 설치
        if operate == 1: # 설치
            answer.append([x, y, stuff]) # 일단 설치
            if not possible(answer): # 가능한지 확인
                answer.remove([x, y, stuff]) # 불가능하면 다시 제거
    return sorted(answer)