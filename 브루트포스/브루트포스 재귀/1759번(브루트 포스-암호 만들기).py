L, C = map(int, input().split())
alphabet = list(map(str, input().split()))
alphabet.sort()
out = []
visited = [False] * (C + 1)
vowel = ['a', 'e', 'i', 'o', 'u']


def solve(depth, idx):
    if depth == L:
        count = 0
        for i in vowel:
            if i in out:
                count += 1
        if 0 < count <= 1 and len(out) == 3:
            print(''.join(out))
        elif 0 < count <= 2 and len(out) == 4:
            print(''.join(out))
        elif 0 < count <= 3 and len(out) == 5:
            print(''.join(out))
        elif 0 < count <= 4 and len(out) == 6:
            print(''.join(out))
        elif 0 < count <= 5 and len(out) == 7:
            print(''.join(out))
        elif 0 < count and len(out) >= 8:
            print(''.join(out))
        return
    for i in range(idx, C):
        if not visited[i]:
            visited[i] = True
            out.append(alphabet[i])
            solve(depth + 1, i + 1)
            visited[i] = False
            out.pop()


solve(0, 0)
