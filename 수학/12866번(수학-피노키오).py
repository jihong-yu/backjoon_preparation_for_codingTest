L = int(input())
S = input()
pinokio = ['A', 'C', 'G', 'T']

count = 1
for i in pinokio:
    count *= S.count(i)  # 문자가 있는 개수만큼 계속 곱해준다.

print(count % 1000000007)
