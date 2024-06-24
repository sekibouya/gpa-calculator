now=float(input("今のGPA>>>"))
units=float(input("今までに履修したGPA算入科目の総単位数>>>"))
numerator=now*units
li=["S","A+","A","A-","B+","B","B-","C+","C","C-"]
while True:
    try:
        new_units=int(input("今後履修する単位数>>>"))
        goal=float(input("目標のGPA>>>"))
    except:
        print("誤った入力です")
        continue
    gp=3.3
    for i in range(10):
        if i==0:
            if goal>(numerator+4*new_units)/(new_units+units):
                print("到達不可能な目標です")
                break
        else:
            if goal>(numerator+gp*new_units)/(new_units+units):
                for j in range(1,new_units+1):
                    if i==1:
                        sa=0.7
                    else:
                        sa=0.3
                    score=(numerator+gp*(new_units-j)+(gp+sa)*j)/(new_units+units)
                    if score>=goal:
                        print("目標に到達するには",li[i-1],"が",j,"単位、",li[i],"が",new_units-j,"単位必要です")
                        break
                break
            elif i==9:
                print("落単しなければ達成できます。もっと高い目標を持ちましょう。")
            gp-=0.3
    if input("続行:1, 終了:0 >>>")=="0":
        print("プログラム終了")
        break

# print("今後全てSを取ったときのGPA:",(numerator+4*new_units)/(new_units+units))