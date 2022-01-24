omok = []
for _ in range(19):
    omok.append(list(map(int, input().split())))

result = []


def solution():
    global result

    for i in range(len(omok)):
        for j in range(len(omok[i])):
            # 만약 바둑이 있다면
            if omok[i][j] != 0:
                # 1st. 가로로 오목 이상일 때
                if j != len(omok[i]) - 1 and omok[i][j] == omok[i][j + 1]:
                    if j != 0 and omok[i][j - 1] != omok[i][j]:
                        for k in range(j, len(omok) - 1):
                            if omok[i][k] == omok[i][k + 1]:
                                result.append((i, k))
                            else:
                                break
                    elif j == 0:
                        for k in range(j, len(omok) - 1):
                            if omok[i][k] == omok[i][k + 1]:
                                result.append((i, k))
                            else:
                                break

                    if len(result) == 4:
                        return omok[i][j]
                    else:
                        result = []

                # 2nd. 세로로 오목 이상일 때
                if i != len(omok) - 1 and omok[i][j] == omok[i + 1][j]:
                    if i != 0 and omok[i - 1][j] != omok[i][j]:
                        for k in range(i, len(omok) - 1):
                            if omok[k][j] == omok[k + 1][j]:
                                result.append((k, j))
                            else:
                                break
                    elif i == 0:
                        for k in range(i, len(omok) - 1):
                            if omok[k][j] == omok[k + 1][j]:
                                result.append((k, j))
                            else:
                                break

                    if len(result) == 4:
                        return omok[i][j]

                    else:
                        result = []

                # 3th. 오른쪽하단으로 오목 이상일 때
                if i != len(omok) - 1 and j != len(omok[i]) - 1 and omok[i][j] == omok[i + 1][j + 1]:
                    if i != 0 and j != 0 and omok[i - 1][j - 1] != omok[i][j]:
                        h = j
                        for k in range(i, len(omok) - 1):
                            if omok[k][h] == omok[k + 1][h + 1]:
                                result.append((k, h))
                                h += 1
                                if h >= len(omok[i]) - 1:
                                    break
                            else:
                                break

                    elif i == 0 or j == 0:
                        h = j
                        for k in range(i, len(omok) - 1):
                            if omok[k][h] == omok[k + 1][h + 1]:
                                result.append((k, h))
                                h += 1
                                if h >= len(omok[i]) - 1:
                                    break
                            else:
                                break

                    if len(result) == 4:
                        return omok[i][j]

                    else:
                        result = []

                # 4th. 왼쪽하단으로 오목이상일때
                if j != 0 and i != len(omok) - 1 and omok[i][j] == omok[i + 1][j - 1]:
                    if i != 0 and j != len(omok[i]) - 1 and omok[i - 1][j + 1] != omok[i][j]:
                        h = j
                        for k in range(i, len(omok) - 1):
                            if omok[k][h] == omok[k + 1][h - 1]:
                                result.append((k, h))
                                h -= 1
                                if h <= 0:
                                    break

                            else:
                                break
                    elif i == 0 or j == len(omok) - 1:
                        h = j
                        for k in range(i, len(omok) - 1):
                            if omok[k][h] == omok[k + 1][h - 1]:
                                result.append((k, h))
                                h -= 1
                                if h <= 0:
                                    break

                            else:
                                break

                    if len(result) == 4:
                        result.append((result[3][0] + 1, result[3][1] - 1))
                        result.reverse()
                        return omok[i][j]

                    else:
                        result = []


color = solution()
if color is None and len(result) == 0:
    print(0)
else:
    print(color)
    print(result[0][0] + 1, result[0][1] + 1)
