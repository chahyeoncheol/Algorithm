'''# 라이브 풀이
#순열1
def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N):  # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            f(i + 1, N)
            A[i], A[j] = A[j], A[i]


A = [1,2,3]
f(0, 3)

# 출력값
# [1, 2, 3] 0 0 1 1 2 2
# [1, 3, 2] 1 2
# [2, 1, 3] 0 1
# [2, 3, 1] 0 1 1 2
# [3, 2, 1] 0 2
# [3, 1, 2] 0 2 1 2
 # 라이브 풀이
'''

'''# 교재 풀이
def construct_candidates(data, idx, max_num, unused_num):
    # 포함된 숫자의 확인을 위해 리스트 생성
    in_perm = [False] * NMAX

    # now가 1인 경우는 아직 아무 숫자도 사용되지 않았기 때문에 사용한 숫자를 찾을 필요가 없음
    for i in range(1, idx):
        in_perm[data[i]] = True

    # 후보의 갯수 / 0부터 시작
    ncandidates = 0

    # 1부터 최고 숫자까지 반복
    for i in range(1, max_num + 1):  # 1 ~ 3
        # i 자리의 숫자가 수열에 이미 사용되지 않았다면,
        if in_perm[i] == False:
            # 사용되지 않은 숫자들 중 작은 숫자부터 0번 인덱스에 차례로 포함시킨다.
            unused_num[ncandidates] = i
            # 인덱스 다음으로 이동 +1
            ncandidates += 1

    # 최종적으로 ncandidates, 즉 포함되지 않은 숫자의 개수 리턴
    # bit에는 아직 포함되지 않은 작은 숫자부터 기록된다.
    return ncandidates


def backtrack(data, idx, max_num):
    global MAXCANDIDATES  # MAXCANDIDATES = 3
    # 최고숫자만큼 포함되지 않은 숫자들을 저장할 리스트 생성 / 미포함 리스트
    unused_num = [0] * MAXCANDIDATES

    # 3까지 포함시켰다면, 즉 모든 단계를 진행했다면
    if idx == max_num:
        # 1부터 마지막 숫자까지 반복하며, 포함되는 해당 원소 출력
        for i in range(1, idx + 1):
            print(data[i], end=' ')
        print()

    # 단계가 부족하다면
    else:
        # 단계 +1
        idx += 1

        # 남은 자리에 추가 가능한 숫자 구하기
        # construct_candidates 함수를 통해 이전 단계에서 사용되지 않은 숫자를 구하고 그 개수를 리턴받는다.
        ncandidates = construct_candidates(data, idx, max_num, unused_num)

        # 포함되지 않은 숫자 개수만큼 반복
        for i in range(ncandidates):
            # 집합의 현재 자리에 미포함 리스트에 저장됐던 숫자 저장
            data[idx] = unused_num[i]
            # 추가된 집합을 적용한 백트래킹 함수 호출
            backtrack(data, idx, max_num)


# 후보가 될 수 있는 자리
MAXCANDIDATES = 3

# 0부터 시작하는 모든자리
NMAX = 4

# 부분집합(수열)을 담을 리스트 생성
data = [0] * NMAX

# 순열, 현재자리 or 현재단계(0부터 시작), 최고숫자를 제공하는 백트래킹 호출
backtrack(data, 0, MAXCANDIDATES)
'''# 교재 풀이