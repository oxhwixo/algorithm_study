# 조건에 맞는 구조물인지 확인
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥
            # 바닥 위 혹은 보의 한쪽 끝 부분 위 혹은 다른 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1: # 보
            # 한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []

    for frame in build_frame: 
        x, y, stuff, operate = frame

        if operate == 0: # 삭제
            answer.remove([x, y, stuff]) # 일단 삭제
            if not possible(answer): # 조건 확인
                answer.append([x, y, stuff]) # 조건에 안맞으면 다시 설치

        if operate == 1: # 설치
            answer.append([x, y, stuff]) # 일단 설치
            if not possible(answer): # 조건 확인
                answer.remove([x, y, stuff]) # 조건에 안맞으면 다시 제거

    return sorted(answer)