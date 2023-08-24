N, K = map(int, input().split())    # N = 인원수, K = 제한 인원
SY = [list(map(int, input().split())) for _ in range(N)]     # S = 성별 ( 여 0 남 1 ), Y = 학년 ( 1 ~ 6 학년 )

gender_0 = []
gender_1 = []
count = 0

for i in SY:
    if i[0] == 1:
        gender_1.append(i)    # 남성들 모으기
    elif i[0] == 0:
        gender_0.append(i)    # 여성들 모으기

boy = [0] * 6
for i in gender_1:    # 남자
    if i[1] == 1:     # 1학년 인원
        boy[0] += 1
    elif i[1] == 2:   # 2학년 인원
        boy[1] += 1
    elif i[1] == 3:   # 3학년 인원
        boy[2] += 1
    elif i[1] == 4:   # 4학년 인원
        boy[3] += 1
    elif i[1] == 5:   # 5학년 인원
        boy[4] += 1
    elif i[1] == 6:   # 6학년 인원
        boy[5] += 1

girl = [0] * 6
for i in gender_0:    # 남자
    if i[1] == 1:     # 1학년 인원
        girl[0] += 1
    elif i[1] == 2:   # 2학년 인원
        girl[1] += 1
    elif i[1] == 3:   # 3학년 인원
        girl[2] += 1
    elif i[1] == 4:   # 4학년 인원
        girl[3] += 1
    elif i[1] == 5:   # 5학년 인원
        girl[4] += 1
    elif i[1] == 6:   # 6학년 인원
        girl[5] += 1

for i in range(6):
    if 0 < girl[i]:
        count += (girl[i] + K - 1) // K

for i in range(6):
    if 0 < boy[i]:
        count += (boy[i] + K - 1) // K

print(count)