def find(n):
    if boss[n] == 0: # 가르키는 보스가 없으면
        return n # 최종 보스다

    result = find(boss[n]) # 재귀호출
    boss[n] = result # 경로압축!!!(이 코드를 추가함으로써 더 효율적이게 된다)
    return result

def union(t1, t2):
    a = find(t1) # a는 t1의 보스
    b = find(t2) # b는 t2의 보스
    if a == b: return # 보스가 같으면 : 탈락
    boss[b] = a # b의 보스가 a다

boss = [0] * 100

N = int(input())
visited = []
for _ in range(N):
    a, b = map(ord, input().split())
    union(a, b)
    for i in range(100):
        if boss[i] == b: boss[i] = boss[b]
    if a not in visited: visited.append(a)
    if b not in visited: visited.append(b)

boss = set(boss)
print(len(boss)-1)
print(26-len(visited))

# # 강사님 코드
# # 알파벳이 26개
# boss = [0] * 27
# # 조직에 속해있다(그룹이 구성되어있다)
# hasTeam = [0] * 27
#
# def find_set(n):
#     if boss[n] == 0: return n # 값이 0이면 최종 보스다
#     boss[n] = find_set(boss[n]) # 경로압축, 재귀호출
#     return boss[n]
#
# def union_set(t1, t2):
#     a = find_set(t1) # t1의 보스는 a
#     b = find_set(t2) # t2의 보스는 b
#     if a == b: return # 이미 같은 그룹이면 탈락
#     boss[b] = a # b가 a밑으로 들어간다
#
# # 관계의 수
# n = int(input())
# for i in range(n):
#     a, b = input().split()
#     aA = ord(a) - ord('A') + 1 # 'A'부터 'Z'를 1부터 26까지
#     bB = ord(b) - ord('A') + 1
#     union_set(aA, bB) # 두 연주자를 같은 그룹으로
#     hasTeam[aA] = 1
#     hasTeam[bB] = 1
#
# # 조직의 수를 계산 - 보스의 수 - 보스가 중복되는경우(중복을 제거 set)
# teams = set()
# for i in range(1, 27):
#     if hasTeam[i] == 1:
#         teams.add(find_set(i)) # 보스를 찾아서 set에 추가
#
# # 조직에 속하지 않은 연주자들
# solo = 0
# for i in range(1, 27):
#     if hasTeam[i] == 0:
#         solo += 1
#
# print(len(teams))
# print(solo)