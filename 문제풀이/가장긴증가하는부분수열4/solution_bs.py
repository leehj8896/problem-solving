# O(NlogN)

def 하한선찾기(시작, 끝, 현재값):
    if 시작 > 끝:
        return 시작
    중간 = (시작+끝)//2
    if 증가리스트[중간] >= 현재값:
        return 하한선찾기(시작, 중간-1, 현재값)
    else:
        return 하한선찾기(중간+1, 끝, 현재값)


def 초기화():
    전체길이 = int(input(''))
    수열 = list(map(int, input('').split(' ')))
    return 전체길이, 수열, [], [], []


전체길이, 수열, 증가리스트, 하한선리스트, 경로리스트 = 초기화()
for 현재위치 in range(전체길이):
    현재값 = 수열[현재위치]
    하한선 = 하한선찾기(0, len(증가리스트)-1, 현재값)
    하한선리스트.append(하한선)
    if 하한선 < len(증가리스트):
        증가리스트[하한선] = 수열[현재위치]
    else:
        증가리스트.append(수열[현재위치])
현재길이 = len(증가리스트)-1
현재위치 = 전체길이-1
while 현재위치 >= 0:
    if 하한선리스트[현재위치] == 현재길이:
        경로리스트.append(str(수열[현재위치]))
        현재길이 -= 1
    현재위치 -= 1
print(len(증가리스트))
print(' '.join(reversed(경로리스트)))
