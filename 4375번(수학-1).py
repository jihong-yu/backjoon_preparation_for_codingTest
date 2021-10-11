while True: #무한 입력
    try: #무한 입력이기 때문에 파일의 끝 에러 EOF에러를 잡아주기 위한 try,catch 구문 작성
        n = int(input())
        abs = '1'
        while True:
            if int(abs) % n == 0: #만약 1,11,111,1111... 이 입력한 n으로 나누어 떨어진다면
                print(len(abs)) #그 1로된 수의 자리수를 출력
                break #그리고 반복문 탈출
            abs += '1' #1,11,111,1111.... 형식으로 증가시키기 위해 문자1에 1을 더해준다.
    except EOFError: #파일의 끝에러 EOFError를 처리한다.
        break