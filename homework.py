menu = ["치즈버거 세트", "불고기버거 세트", "치킨버거 세트", "종료"]
for i, item in enumerate(menu):
    print(f"{i+1}. {item}")
a = int(input("메뉴를 선택하세요: "))

if a > len(menu):
    print("없는 메뉴입니다")
else:
    if a == 4:
        print("종료합니다.")
    else:
        print(f"{a} 번 메뉴를 선택했습니다.")
