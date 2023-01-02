# CHAPTER > 03 : 그리디

# <1> 당장 좋은 것만 선택하는 그리디
# 그리디 알고리즘은 단순하지만 강력한 문제 해결 방법이다.
# 이 알고리즘 유형은 .... -->> '탐욕법'으로 소개된다.
# 이름에서 알 수 있듯이 -->> "어떠한 문제가 있을 때 단순 무식하게, 탐욕적으로 문제를 푸는 알고리즘이다."
# 여기서 탐욕적이라는 말은 -->> '현재 상황에서 지금 당장 좋은 것만 고르는 방법'을 의미한다.
# 그리디 알고리즘을 이용하면 -->> 매 순간 가장 좋아 보이는 것을 선택하며, 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않는다.
# .... 반면 이후에 공부할 정렬, 최단 경로 등의 알고리즘 유형은 이미 그 알고리즘의 사용 방법을 정확히 알고 있어야만 해결 가능한 경우가 많다.
# .... 또 다른 예시로 최단 경로를 빠르게 찾아야 하는 문제는 -->> 플로이드 워셜(Floyd-Warshall) 혹은 다익스트라(Dihkstra)알고리즘과 같은 특정 알고리즘을 미리 알고 있거나
# 팀 노트를 통해 준비해야 풀 수 있다.
# 참고로 -->> "다익스트라 알고리즘은 엄밀히 말하면 그리디 알고리즘으로 분류되므로", 그리디 알고리즘이면서도 '암기'가 필요한 알고리즘이기도 하다.
# 다만, 그리디 알고리즘 자체가 문제 출체의 폭이 매우 넓기 때문에, 다익스트라 알고리즘과 같은 특이 케이스를 제외하고는 단순 암기를 통해 모든 문제를 대처하기 어렵다는 점을 이해하자.
# .... 많은 유형을 접해보고 문제를 풀어보며 훈련을 해야 한다. 향후 등장할 문제를 풀어보면 이해할 수 있을 것이다.
# 보통 코딩 테스트에서 출제되는 그리디 알고리즘 유형의 문제는 -->> 창의력, 즉 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구한다.
# 다시 말해 특정한 문제를 만났을 때 단순히 현재 상황에서 가장 좋아 보이는 것만을 선택해도 문제를 풀 수 있을지를 파악할 수 있어야 한다.
# 그리디 알고리즘은 기준에 따라 좋은 것을 선택하는 알고리즘이므로 문제에서 '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 알게 모르게 제시해준다.
# 대체로 이 기준은 정렬 알고리즘을 사용했을 때 만족시킬 수 있으므로, 그리디 알고리즘 문제는 자주 정렬 알고리즘과 짝을 이뤄 출제된다.
# 이제 '거스름돈' 문제를 예로 그리디 알고리즘을 설명하겠다. '거스름돈' 문제는 그리디 알고리즘을 대표하는 문제이다.

# [예제 3-1] 거스름돈
# .... 거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬뤄 줘야 할 돈은 N은 항상 10의 배수이다.

# 문제 해설
# 이 문제는 그리디 알고리즘을 이용해 풀 수 있는 대표적인 문제로 간단한 아이디어만 떠올릴 수 있으면 문제를 해결할 수 있다.
# 그것은 바로 -->> "'가장 큰 화폐 단위부터' 돈을 거슬러 주는 것"이다.
# ....
# 3-1.py 답안 예시
"""
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
"""
# 코드를 보면 화폐의 종류만큼 반복을 수행해야 한다. 따라서 화폐의 종류가 K개라고 할 때 위 소스 코드의 시간 복잡도는 O(K)이다.

# 그리디 알고리즘의 정당성
# 그리디 알고리즘을 모든 알고리즘 문제에 적용할 수 있는 것은 아니다. 대부분의 문제는 그리디 알고리즘을 이용했을 때 '최적의 해'를 찾을 수 없는 가능성이 다분하다.
# 하지만 거스름돈 문제는 '가장 큰 화폐 단위부터' 돈을 거슬러 주는 것과 같이, 탐욕적으로 문제에 접근했을 때 정확한 답을 찾을 수 있다는 보장이 있을 때는 매우 효과적이고 직관적이다.
# 그리디 알고리즘을 문제의 해법을 찾았을 때는 그 해법이 정당한지 검토해야 한다. 거스름돈 문제를 그리디 알고리즘으로 해결할 수 있는 이유는 "가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문이다."
# 예를 들어 800원을 거슬러 줘야 하는데, 화폐 단위가 500원, 400원, 100원인 경우를 생각해보자. 이 경우에 그리디 알고리즘으로는 4개의 동전(500원 + 100원 + 100원 + 100원)을 거슬러 줘야 한다고 나오는데,
# 최적의 해는 2개의 동전(400원 + 400원)을 거슬러 주는 것이다. 다시 말해 이 문제에서는 큰 단위가 작은 단위의 배수 형태이므로, '가장 큰 단위의 화폐부터 가장 작은 단위의 화폐까지 차례대로 확인하여 거슬러 주는 작업만을 수행하면 된다'는 아이디어는 정당하다.
# "대부분의 그리디 알고리즘 문제에서는 이처럼 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 답을 도출할 수 있다."
# 어떤 코딩 테스트 문제를 만났을 때, 바로 문제 유형을 파악하기 어렵다면 -->> 그리디 알고리즘을 의심하고, 문제를 해결할 수 있는 탐욕적인 해결법이 존재하는지 
# 고민해보자.
# 만약 오랜 시간을 고민해도 그리디 알고리즘으로 해결 방법을 찾을 수 없다면, -->> 그때는 이후의 장에서 다루게 될 '다이나믹 프로그래밍'이나 '그래프 알고리즘' 등으로
# 문제를 해결할 수 있는지를 재차 고민해보는 것도 한 방법이다.
# 처음에 문제를 만났을 때는 이것저것 다양한 아이디어를 고려해야 한다.
# ....
# ....
# 실제로 거스름돈 문제에서 동전(화폐)의 단위가 서로 배수 형태가 아니라, 무작위로 주어진 경우에는 그리디 알고리즘으로는 해결할 수 없다. 화폐의 단위가 무작위로 주어진 문제는 2부에서 배울 '다이나믹 프로그래밍'으로 '해결'할 수 있으며
# 해당 문제 또한 책에서 다루고 있다.(8장 '효율적인 화폐 구성')
# 지금까지 그리디 알고리즘의 기본 원리에 대해서 알아보았으므로 이제부터 그리디 알고리즘의 실전 예제를 더 풀어보자.
# 지금부터 설명할 문제는 알고리즘 대회 및 코딩 테스트에 출제되었던 문제를 다듬은 것이다.
# -->> "기업의 코딩 테스트를 안정적으로 통과하려면 다음에 소개되는 문제 각각에 대해 문제별 아이디어를 떠올리고 코드로 작성하기까지 시간이 30분 이내로 소요되어야 한다."
# 난이도는 모두 '하'에 해당하며 총 3문제를 준비하였다.

# <2> 큰 수의 법칙

# my solution
"""
N, M, K = map(int, input().split())
array = list(map(int, input().split()))
# print(array)

total_count = 0
answer = 0
count = 0
array.sort(reverse = True) # 입력받은 배열 array를 내림차순으로 정렬..!!
# (ex) array = [2, 4, 5, 4, 6] -->> array = [6, 5, 4, 4, 2]

while total_count < M:
    total_count += 1 # 이 변수는 총 반복횟수를 의미하는 변수입니다..!!
    count += 1 # count : 1 --> 2 --> 3 --> 4 --> 5.... # 여기서 count 변수의 의미는 가장 큰 수를 연속으로 더한 횟수를 임시로 저장해주는 변수입니다..!!
    if count <= K:
        answer += array[0]
    else: # 즉, count > K 인 경우일 때는 그 다음으로 큰 수를 더해줘서 가장 큰 수가 K번 초과로 더해지는 것을 방지해줍니다.
        answer += array[1]
        count = 0 # 다시 count를 0으로 초기화해줍시다..!!

print(answer)
"""

# 문제 해설
# 이 문제는 전형적인 그리디 알고리즘 문제로, 문제 해결을 위한 아이디어를 떠올리는 것은 어렵지 않은 편이다. -->> 다만, 문제 해결을 위한 아이디어를 떠올렸어도 
# 구현 실수로 인해 오답 처리를 받는 경우가 많은 문제이므로 꼭 직접 코드를 작성해보는 것을 권장한다.
# 이 문제를 해결하려면 일단 입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
# 연속으로 더할 수 있는 횟수는 최대 K번이므로 '가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산'을 반복하면 된다.
# 이를 소스코드로 표현하면 다음과 같다.

# 단순하게 푸는 답안 예시
"""
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N 개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result) # 최종 답안 출력
"""
# 이 문제는 M이 10000 이하이므로 이 방식으로도 문제를 해결할 수 있지만, M의 크기가 100억 이상처럼 커진다면 시간 초과 판정을 받을 것이다.
# "간단한 수학적 아이디어를 이용해" -->> "더 효율적으로 문제를 해결해보자."
# 예를 들어 N이 5이고 입력값이 다음과 같이 주어졌다고 가정하자.
# [2, 4, 5, 4, 6]
# 이때 가장 큰 수와 두 번째로 큰 수를 선택하면 다음과 같다.
# * 가장 큰 수 : 6
# * 두 번째로 큰 수 : 5
# 이때 M이 8이고, K이가 3이라면 다음과 같이 더했을 때 합을 최대로 할 수 있다. 다시 말해 (6 + 6 + 6 + 5) + (6 + 6 + 6 + 5)로 정답은 46이 된다.
# 이 문제를 풀려면 가장 먼저 "반복되는 수열에 대해서 파악"해야 한다. 가장 큰 수와 가장 두 번째로 큰 수가 더해질 때는 특정한 수열 형태로 일정하게 반복
# 해서 더해지는 특징이 있다. 위의 예시에서는 수열 {6, 6, 6, 5}가 반복된다.
# 그렇다면 반복되는 수열의 길이는 어떻게 될까?
# 바로 (K + 1)로 위의 예시에서는 4가 된다. 따라서 M을 (K + 1)로 나눈 몫이 수열이 반복되는 횟수가 된다. 다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.
# 이때 M이 (K + 1)로 나누어떨어지지 않는 경우도 고려해야 한다. 그럴 때는 M을 (K + 1)로 나눈 나머지만큼 가장 큰 수가 추가로 더해지므로 이를 고려해주어야 한다.
# 즉 '가장 큰 수가 더해지는 횟수'는 다음과 같다.
# -->> "(M // (K + 1)) * K + M % (K + 1)"
# 결과적을 위의 식을 이용하여 가장 큰 수가 더해지는 횟수를 구한 다음, 이를 이용해 두 번째로 큰 수가 더해지는 횟수까지 구할 수 있는 것이다.
# 이를 토댈 파이썬을 이용해 답안을 작성하면 다음과 같다.

# 3-2.py 답안 예시
"""
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int,input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = (m // (k + 1))* k + m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력
"""

# <3> 숫자 카드 게임

# my solution
"""
n, m = map(int, input().split())

answer_list = [] # <<-- 각 행의 최솟 값을 담을 배열(리스트)..!!

for i in range(n):
    array = list(map(int, input().split())) # 각 행마다 -->> 총 m개의 데이터를 입력하도록 한다.
    answer_list.append(min(array))

# print(answer_list) # 출력 결과 Ex : [1, 1, 2]

max_of_mins = answer_list[0] # value
answer = 0 # index

for i, v in enumerate(answer_list):
    if max_of_mins < v:
        max_of_mins = v
        answer = i

print(max_of_mins)
"""

# 문제 해설 
# 그리디 알고리즘 유형의 문제는 문제 해결을 위한 아이디어를 떠올렸다면 정답을 찾을 수 있다.
# 이 문제를 푸는 아이디어는 바로 '각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수'를 찾는 것이다.
# 이 문제는 문제 설명이 길어서 지문 이해에 시간이 많이 소요될 수 있지만, 문제의 아이디어를 떠올리는 것은 쉬운 문제에 속한다.
# .... 다만, 이 문제를 해결하기 위해서는 리스트에서 가장 작은 원소를 찾아주는 min()함수를 이용할 수 있거나, 2중 반복문 구조를 이용할 수 있어야 한다.

# 3-3.py min()함수를 이용하는 답안 예시
"""
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0 # 참고> 문제의 조건 中 -->> .... 각 숫자는 1부터 10,000이하의 자연수이다.
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력
"""

# 3-4.py 2중 반복문 구조를 이용하는 답안 예시
"""
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
"""

# <4> 1이 될 때까지
"""
# my solution
n, k = map(int, input().split())
count = 0

while n != 1: # 즉, n이 1이 된다는 것은 1번 연산과 2번 연산을 할 필요가 없다는 뜻 즉, 모든 과정을 끝냈다는 의미입니다..!!
    while n % k == 0 and n > 1:
        n = n // k
        count += 1
    if n % k != 0 and n > 1: # 참고> 연산 횟수의 최솟값을 구해야하므로 되도록이면 두 번째 과정의 횟수를 최소한으로 만들어줘야 합니다..!!
        n -= 1
        count += 1

print(count)
"""

# 문제 해설
# 이 문제 또한 문제 해결을 위한 아이디어를 떠올릴 수 있으면 어렵지 않게 해결할 수 있다. 주어진 N에 대하여 '최대한 많이 나누기'를 수행하면 된다.
# 왜냐하면 어떠한 수가 있을 때, '2이상의 수로 나누는 것'이 '1을 빼는 것'보다 숫자를 훨씬 많이 줄일 수 있기 때문이다.
# 문제에서는 K가 2이상의 자연수이므로, 가능하면 나누는 것이 항상 더 숫자를 빠르게 줄이는 방법이 된다.
# ....
# 다시 말해 K가 2 이상이기만 하면 K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N의 값을 줄일 수 있으며, N이 결국 1에 도달한다는 것을 알 수 있다.
# 그러므로 K로 최대한 많이 나눌 수 있도록 하는 것이 최적의 해를 보장하는 것이다.
# 파이썬을 이용해 작성한 예시는 다음과 같다.

# 3-5.py 단순하게 푸는 답안 예시
"""
# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
"""
# 문제에서는 N의 범위가 10만 이하이므로, 이처럼 일일이 1씩 빼도 문제를 해결할 수 있다.
# 하지만 N이 100억 이상의 큰 수가 되는 경우를 가정했을 때에도 빠르게 동작하려면,
# -->> "N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 소스코드를 작성할 수 있다.""

# 3-6.py 답안 예시

# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    # ('N' == 'K로 나누어 떨어지는 수')가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

