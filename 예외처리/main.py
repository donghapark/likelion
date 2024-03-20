try:
    # 시도할 코드 블록
    number = int(input("정수를 입력하세요: "))
    print(f"입력한 숫자는 {number}입니다.")
except :
    # 예외가 발생했을 때 실행할 코드 블록
    print("잘못된 값을 입력했습니다. 정수만 입력해주세요.")
