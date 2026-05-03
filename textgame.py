import os

condition="배고프다"
time="11시"
hp=100
money=50000
bag=[]
history=[]

campus=[
    ["","","","","새천년관", "이윤재관"],
    ["백양관", "백양로5", "대강당", "음악관", "알렌관", "ABMRC"],
    ["중앙도서관", "독수리상", "학생회관", "루스채플", "재활병원", "치과대학"],
    ["체육관", "백양로3", "공터2", "광혜원", "어린이병원", "세브란스병원"],
    ["공학관", "백양로2", "백주년기념관", "안과병원", "제중관",""],
    ["공학원", "백양로1", "공터1", "암병원", "의과대학",""],
    ["연대앞 버스정류장", "정문", "스타벅스", "세브란스병원 버스정류장","",""]]

row=6
col=0

print("현재 위치:",campus[row][col])
print("현재 상태:",condition)
print("현재 시각:",time)

level=input("난이도 선택(쉬움,보통,어려움):")

settings={
    "난이도": level
    }

while True:
    direction=input("입력 매뉴> 이동(동,서,남,북)/상태/가방/저장/불러오기:")

    if direction=="저장":
        f=open("저장.txt","w")
        f.write(str(row)+"\n")
        f.write(str(col)+"\n")
        f.write(condition+"\n")
        f.write(time+"\n")
        f.write(level+"\n")
        f.close()
        print("저장되었습니다.")
        continue

    elif direction=="불러오기":
        files = [f for f in os.listdir() if os.path.isfile(f)]
        print("현재 폴더의 파일 목록:")
        for i, f in enumerate(files):
            print(f"{i+1}: {f}")
        
        file_input = input("불러올 파일 번호 또는 경로 입력: ")
        
        if file_input.isdigit() and 1 <= int(file_input) <= len(files):
            file_path = files[int(file_input)-1]
        else:
            file_path = file_input
            
        try:
            f = open(file_path, "r")
            row = int(f.readline().strip())
            col = int(f.readline().strip())
            condition = f.readline().strip()
            time = f.readline().strip()
            level = f.readline().strip()
            f.close()
            print("성공적으로 불러왔습니다.")
            print("현재 위치:", campus[row][col])
        except Exception as e:
            print("파일을 불러오는 데 실패했습니다:", e)
        continue

    if direction== "상태":
        print("계좌의 잔액:",money)
        print("HP:",hp)
        continue

    elif direction=="가방":
        print("가방:",bag)
        
        if len(bag)==0:
            print("물건 없음")
            continue

        for i in range(len(bag)):
            print(i+1, ":", bag[i])

        item=input("사용할 물건 번호or이름:")

        if item.isdigit():
            index=int(item) -1

            if 0 <= index < len(bag):
                item=bag[index]
            else:
                print("잘못된 입력입니다.")
                continue
        
        if item=="두쫀쿠":
            if "두쫀쿠" in bag:
                hp+=25
                bag.remove("두쫀쿠")
            else:
                print("두쫀쿠가 없습니다.")
            continue

        elif item=="카페라떼":
            if "카페라떼" in bag:
                hp+=25
                bag.remove("카페라떼")
            else:
                print("카페라떼가 없습니다.")
            continue
        
        continue

    elif direction =="동":
        if col+1 >= len(campus[row]) or campus[row][col+1] == "":
            print("그 방향은 막혔어")
        else:
            col=col+1
            hp-=1

    elif direction =="서":
        if col-1 < 0 or campus[row][col-1] == "":
            print("그 방향은 막혔어")
        else:
            col=col-1
            hp-=1

    elif direction =="남":
        if row+1 >= len(campus) or campus[row+1][col] == "":
            print("그 방향은 막혔어")
        else:
            row=row+1
            hp-=1

    elif direction =="북":
        if row-1 < 0 or campus[row-1][col] == "":
            print("그 방향은 막혔어")
        else:
            row=row-1
            hp-=1
         
    print("현재 위치:",campus[row][col])
    if campus[row][col]=="학생회관":
        print("1: 두쫀쿠(5000원)")
        print("2: 카페라떼(2500원)")
        print("3: 구매 안함")
        buy=input("구매할 음식 번호:")

        if buy=="1":
            money-=5000
            bag.append("두쫀쿠")
            print("두쫀쿠를 구매했습니다.")

        elif buy=="2":
            money-=2500
            bag.append("카페라떼")
            print("카페라떼를 구매했습니다.")
        
        elif buy=="3":
            print("아무거도 구매하지 않았습니다.")