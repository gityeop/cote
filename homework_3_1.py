sinsun = input("사과의 상태를 입력하시오: ")
if sinsun == "신선":
    price = int(input("사과 1개의 가격을 입력하시오: "))
    if price < 1000:
        print("사과를 10개 산다.")
    else:
        print("사과를 5개 산다.")
else:
    print("사과를 사지 않는다.")
