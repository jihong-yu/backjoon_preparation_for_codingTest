n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

# 각각의 모든 테트로미노의 모양을 좌표로 저장해놓는다.
tetromino = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
    [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]


# x,y가 바뀔때마다(즉,입력받은 종이의 좌표에 따라서 테트로미노를 적용하여 최댓값을 찾는 함수 구현)
def find(x, y):
    global answer
    for i in range(len(tetromino)):  # 테트로 미노의 행의 길이만큼
        result = 0
        for j in range(len(tetromino[i])):  # 테트로 미노의 열의 길이만큼
            try:
                next_x = x + tetromino[i][j][0]  # 인자의 x좌표만큼 테트로미노의 x 좌표를 옮겨준다.
                next_y = y + tetromino[i][j][1]  # 인자의 y좌표만큼 테트로미노의 y 좌표를 옮겨준다.
                result += board[next_x][next_y]  # 입력받은 좌표의 테트로미노 좌표에 있는 숫자들을 계속더해준다.
            except IndexError:  # indexError가발생하면
                break
        answer = max(answer, result)  # result값의 최댓값을 계속해서 저장


def solve():
    for i in range(n):  # 입력받은 좌표의 행의개수 만큼
        for j in range(m):  # 입력받은 좌표의 열의 개수 만큼
            find(i, j)  # 함수실행


answer = 0
solve()
print(answer)
