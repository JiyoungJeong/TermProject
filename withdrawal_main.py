from withdrawal import *

test_case = int(input()) # 입력 첫 줄의 테스트 케이스 수 저장
while test_case <= 50: # 테스트 케이스 수(test_case<=50)만큼 반복
    T = input().split() # 테스트 케이스 수 만큼의 리스트 T 생성, 리스트는 split()으로 공백 구분함
    n = int(T[0]) # T[0]에 n값 저장
    k = int(T[1]) # T[1]에 k값 저장
    rc = input().split() # 테스트 케이스 수 만큼의 리스트 rc 생성, 리스트는 split()으로 공백 구분함
    r = [] # i번째 과목의 등수 리스트 생성
    for i in range(0, len(rc), 2): # rc 리스트의 0번 방부터 누적, rc 길이까지, step2 -> ex) i[0], i[2], i[4]에 차례대로 i번째 과목의 등수가 저장됨
         r.append(int(rc[i]))
    c = [] # i번째 과목의 수강생 수 리스트 생성
    for i in range(1, len(rc), 2): # rc 리스트의 1번 방부터 누적, rc 길이까지, step2 -> ex) i[1], i[3], i[5]에 차례대로 i번째 과목의 수강생 수가 저장됨
         c.append(int(rc[i]))
    print(optimization(r, c, n, k)) # 최적화 결정 함수(optimization) 호출