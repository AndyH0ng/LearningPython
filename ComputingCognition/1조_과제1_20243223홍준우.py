# 1조 과제1 20243223 홍준우
"""
 | 입력 시간에 따라 다르게 배점하는 점수 추가
 |
 |
"""
import random
import time

words = ["오버워치", "배틀그라운드", "배그", "롤", "리그오브레전드", "스타크래프트", "마인크래프트", "발로란트", "피파", "메이플"]

# 변수 n에 1을 저장
n = 1

# 문자열 이름을 입력
name = input("이름을 입력하세요: ")

# 메세지 출력
print("타자 게임 준비되면 Enter")
input()

# 변수 start_time에 현재 시간을 저장
start_time = time.time()

score = 0

while n <= 5:
    print(f"*****라운드 {n}*****")
    current_word = random.choice(words)
    print(f"단어: {current_word}")
    # is an equivalent of...
    # print("단어 <<< ", current_word)
    waiting_time = time.time()

    user_input = input("단어를 입력하세요: ")

    if user_input == current_word:
        corrent_time = time.time()
        print("👏정답👏")
        n += 1
        # is Complex Operator, which is an equivalent of...
        # n = n + 1
        if corrent_time - waiting_time < 1:
            score += 10
        elif corrent_time - waiting_time < 3:
            score += 8
        elif corrent_time - waiting_time < 5:
            score += 6
        elif corrent_time - waiting_time < 7:
            score += 4
        else:
            score += 2
    else:
        print("☠️오타입니다. 다시 도전하세요☠️")
        score -= 1
end_time = time.time()
es_time = end_time - start_time

print(f"{name}님이 걸린 시간은 {es_time:2f}, 점수는 {score}점 입니다.")
# print("&s님이 걸린 시간은 &d, 점수는 &d점 입니다.", name, es_time, score)
# :2f -> 둘째자리 까지
