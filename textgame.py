condition="배고프다"
time="11시"

campus=[["공학관","백양로1","백주년기념관"],["공학원","백양로1","공터1"],["연대앞 버스정류장","정문","세븐란스병원 버스정류장"]]

row=2
col=0

print("현재 위치:",campus[row][col])
print("현재 상태:",condition)
print("현재 시각:",time)

level = input("난이도 선택(쉬움,보통,어려움):")

settings = {
    "난이도": level
    }

while True:
    direction=input("이동 방향 선택(동,서,남,북):")

    if direction =="동":
        if col+1 >= 3:
            print("그 방향은 막혔어")
        else:
            col=col+1

    elif direction =="서":
        if col-1 < 0:
            print("그 방향은 막혔어")
        else:
            col=col-1

    elif direction =="남":
        if row+1 >= 3:
            print("그 방향은 막혔어")
        else:
                row=row+1

    elif direction =="북":
        if row-1 < 0:
            print("그 방향은 막혔어")
        else:
            row=row-1
         
    print("현재 위치:",campus[row][col])
