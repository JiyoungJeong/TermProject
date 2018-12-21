# Term Project : 알고리즘
# 문제명 : 수강 철회(WITHDRAWAL)
# 2017053281 정지영

'''
<변수명 정의>
r : i번째 과목의 등수
c : i번째 과목의 수강생 수
n : 백준이가 수강하는 과목의 수
k : 백준이가 남겨둬야 할 과목의 수
'''

def accumulate(rank, r, c, n, k): # 누적등수 계산하는 함수
    list = [] # 추정 누적등수가 저장 될 빈 리스트 생성
    for i in range(n): # 수강하는 과목 수 만큼 반복함
        list.append((rank * c[i] - r[i])) # rank(추정 등수) * i번째 과목의 수강생수 - 백준이의 실제 등수
    list.sort() # 추정 누적등수 오름차순으로 정렬 ex) [-1.5, -1, 1]

    sum = 0
    for i in range(n-k,n):
        sum+= list[i] # 추정 누적등수 리스트 중 상위 k개의 합 ex) -1+1 = 0
    return sum>=0 # 상위 k개의 합이 0이상이 되는지 여부 (0에 가까울 수록 등수가 가장 높다는 것을 의미, 1은 등수가 가장 낮음을 의미)

def optimization(r, c, n, k): # 최적화 결정 함수
    min = 0 # 누적 등수는 0~1 범위의 실수 (최소값은 0)
    max = 1 # 누적 등수는 0~1 범위의 실수 (최대값은 1)
    for i in range(100): # 정확한 값 도출을 위해 대략 100번 정도 반복함
        mid = (min + max) / 2.0 # 최초 추정 등수는 0과 1사이의 중간 값인 0.5로 지정
        if accumulate(mid, r, c, n, k): # 누적등수 계산 함수(accumulate) 호출
            max = mid # sum>=0
        else:
            min = mid # sum<0
    return min # 최소 누적등수 반환 -> 결과값 도출