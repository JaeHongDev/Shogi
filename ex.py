from tkinter import *
from PIL import Image,ImageTk
global poro_1p, poro_2,king_1p_win,king_2p_win,ori_count_1

king_1p_win = 0
king_2p_win = 0
poro_1p =[]
poro_2p =[]
ori_count_1 = -1
game_count = 0
print("게임시작")
print("(+)위쪽플레이어 순서")
root = Tk()
#------------------------------------------포로 이동 클래스--------------------------#
class team():
    def my_team(self,widget,value):
        global v1
        v1 = value
        widget.bind("<ButtonPress-1>",self.you_myTeam)
    def you_myTeam(self,event):

        global game_count
        a = event.widget.place_info()
        search_x,search_y = int(a['x']),int(a['y'])
        for i in range(0,len(poro_sto),1):
            poro_sto[i].destroy()
        go_poro.place(x =search_x,y=search_y)
        go = go_poro.cget("textvariable")
        print(go)
        for i in range(0, len(poro_1p), 1):
            if (int(poro_1p[i].cget("textvariable")) == v1):
                poro_1p.remove(poro_1p[i])
        for i in range(0, len(poro_1p), 1):
            if (int(poro_2p[i].cget("textvariable")) == v1):
                poro_2p.remove(poro_2p[i])
        for i in range(0,len(shogi_label),1):
            ce = int(shogi_label[i].cget("textvariable"))
            if(ce == go):
                shogi_label[i] = go_poro

        shogi_label[i].config(textvariable = int(go) * -1)
        game_count = game_count + 1
        if (game_count % 2 == 0):
            print("(+)위쪽플레이어의 순서입니다")
        else:
            print("(-)아래쪽플레이어의 순서입니다")
        cm = ClickManager()
        cm.ClickLabel(go_poro)
        board = [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]
        place_board = []
        for i in range(0, 8, 1):
            select = {}
            sear = shogi_label[i].place_info()
            sear_x, sear_y = int(sear['x']), int(sear['y'])
            select["x"], select["y"], select['name'] = sear_x, sear_y, int(shogi_label[i].cget("textvariable"))
            place_board.append(select)
        # print(place_board)
        place_board_y_2 = []
        place_board_y_142 = []
        place_board_y_282 = []
        place_board_y_422 = []
        print_board = []
        check = [2, 142, 282, 422]

        for i in range(0, 8, 1):
            # if(place_board[i]['name'] > 0):
            if (place_board[i]['y'] == 2):
                place_board_y_2.append(place_board[i])
            elif (place_board[i]['y'] == 142):
                place_board_y_142.append(place_board[i])
            elif (place_board[i]['y'] == 282):
                place_board_y_282.append(place_board[i])
            elif (place_board[i]['y'] == 422):
                place_board_y_422.append(place_board[i])
        print_board = [place_board_y_2, place_board_y_142, place_board_y_282, place_board_y_422]

        print(print_board[0][1])
        for i in range(0, len(print_board), 1):
            for j in range(0, len(print_board[i]), 1):
                if (print_board[i][j]['x'] == 2):
                    board[i][0] = print_board[i][j]['name']
                elif (print_board[i][j]['x'] == 142):
                    board[i][1] = print_board[i][j]['name']
                elif (print_board[i][j]['x'] == 282):
                    board[i][2] = print_board[i][j]["name"]

        print("-----------------------------------------")
        print("-", "", board[0][0], "", board[0][1], "", board[0][2], "-")
        print("-", "", board[1][0], "", board[1][1], "", board[1][2], "-")
        print("-", "", board[2][0], "", board[2][1], "", board[2][2], "-")
        print("-", "", board[3][0], "", board[3][1], "", board[3][2], "-")
        print("-----------------------------------------")
        return

#-------------------------------------------포로 클래스------------------------------#
class poro():
    def move_poro(self,widget):
        widget.bind("<ButtonPress-1>",self.my_poro)
    def my_poro(self,event):
        global go_poro,poro_sto
        go_poro = event.widget
        attack_poro = [[2,142],[142,142],[282,142],[2,282],[142,282],[282,282]]
        check_poro = [0,0,0,0,0,0]
        value =event.widget.cget("textvariable")
        poro_sto = []
        count = 0
        for i in range(0,len(attack_poro),1):
            if (value == 1):
                sto = Label(root, image=blur_p_img_1)
            elif (value == -1):
                sto = Label(root, image=blur_p_r_img_1)
            elif (abs(value) == 2):
                sto = Label(root, image=blur_p_img_2)
            elif (abs(value) == 3):
                sto = Label(root, image=blur_p_img_3)
            elif (abs(value) == 4):
                sto = Label(root, image=blur_p_img_4)
            poro_sto.append(sto)
        for i in range(0,8,1):
            check = shogi_label[i].place_info()
            check_x,check_y = int(check['x']),int(check['y'])
            for j in range(0,len(attack_poro)):
                if(check_x == attack_poro[j][0] and check_y == attack_poro[j][1]):
                    check_poro[j] = 1
        Team =team()
        for i in range(0,len(poro_sto),1):
            if (check_poro[i] == 0):
                poro_sto[i].place(x = attack_poro[i][0],y = attack_poro[i][1])
                Team.my_team(poro_sto[i],value)



         
#------------------------------------------------move class--------------------------------#
class Move():
    def Move_label(self,widget):
        widget.bind("<ButtonPress-1>",self.Main)
    def place_check(self,x,y):
        try:
            a = 0
            b = 0
            global poro_1p,poro_2p,king_1p_win,king_2p_win
            for i in range(0, 8, 1):
                search_x, search_y = shogi_label[i].winfo_x(), shogi_label[i].winfo_y()
                # print(search_x,search_y)
                if (search_x == x and search_y ==y):
                    if(game_count%2 == 0):
                        poro_1p.append(shogi_label[i])
                        a = a +1
                        if(shogi_label[i].cget("textvariable")==-3):
                            for i in range(0,len(shogi_label),1):
                                shogi_label[i].destroy()
                            print("(+)위쪽 플레이가 (-)아랫쪽 플레이어의 왕을 잡았습니다")
                            return 0 
                        #print(a)
                    else:
                        poro_2p.append(shogi_label[i])
                        b = b+1
                        if(shogi_label[i].cget("textvariable")==3):
                            for i in range(0,len(shogi_label),1):
                                shogi_label[i].destroy()
                                
                            print("(-)아랫쪽 플레이어가 (+)위쪽 플레이어의 왕을 잡았습니다")
                            return 0 
                          
                set_label.place(x = x, y = y)
                self.des_label(storge)
            if(game_count % 2 ==0):

                for i in range(0,len(poro_1p),1):
                    poro_1p[i].place(x = -140,y = i*140)
                for i in range(0,len(poro_2p),1):
                    poro_2p[i].place(x = 620,y = i*140)
            if (game_count % 2 != 0):

                for i in range(0, len(poro_1p), 1):
                    poro_1p[i].place(x=480, y=i * 140)
                for i in range(0, len(poro_2p), 1):
                    poro_2p[i].place(x=-140, y=i * 140)


            Poro = poro()
            for i in range(0,len(poro_1p),1):
                Poro.move_poro(poro_1p[i])
            for i in range(0,len(poro_2p),1):
                Poro.move_poro(poro_2p[i])
            if(king_1p_win==1):
                for i in range(0,len(shogi_label),1):
                    shogi_label[i].destroy()
                    print("-왕이 상대진영에서 한턴 버텼습니다")
            print(king_2p_win)
            if(king_2p_win==1):
                for i in range(0,len(shogi_label),1):
                    shogi_label[i].destroy()
                    print("+왕이 상대진영에서 한턴 버텼습니다")
        except:
            pass
     # ------------------------------움직이는 라벨 삭제----------------------------------------#
    def des_label(self, array):
        for i in range(0, len(array), 1):
            array[i].destroy()

    #-----------------------------무브클래스메인-----------------------------------------------#
    def Main(self,event):
        global  game_count
        label_info = event.widget.place_info()
        label_info_x,label_info_y = int(label_info['x']),int(label_info['y'])
        #print(label_info_x,label_info_y)
        self.place_check(label_info_x,label_info_y)
        #print(who_turn,"체크")
        game_count = game_count +1

        if(game_count %2 == 0):
            print("(+)위쪽플레이어의 순서입니다")
            
        else:
            print("(-)아래쪽플레이어의 순서입니다")
            
        board = [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]
        place_board = []
        for i in range(0, 8, 1):
            select = {}
            sear = shogi_label[i].place_info()
            sear_x, sear_y = int(sear['x']), int(sear['y'])
            select["x"], select["y"], select['name'] = sear_x, sear_y, int(shogi_label[i].cget("textvariable"))
            place_board.append(select)
        # print(place_board)
        place_board_y_2 = []
        place_board_y_142 = []
        place_board_y_282 = []
        place_board_y_422 = []
        print_board = []
        #if (game_count % 2 == 0):
        for i in range(0, 8, 1):
                # if(place_board[i]['name'] > 0):
             if (place_board[i]['y'] == 2):
                place_board_y_2.append(place_board[i])
             elif(place_board[i]['y'] == 142):
                 place_board_y_142.append(place_board[i])
             elif(place_board[i]['y'] == 282):
                place_board_y_282.append(place_board[i])
             elif(place_board[i]['y'] == 422):
                place_board_y_422.append(place_board[i])
        print_board = [place_board_y_2, place_board_y_142, place_board_y_282, place_board_y_422]
        for i in range(0, len(print_board), 1):
            for j in range(0, len(print_board[i]), 1):
                if (print_board[i][j]['x'] == 2):
                    board[i][0] = print_board[i][j]['name']
                elif (print_board[i][j]['x'] == 142):
                    board[i][1] = print_board[i][j]['name']
                elif (print_board[i][j]['x'] == 282):
                    board[i][2] = print_board[i][j]["name"]

        print("-----------------------------------------")
        print("-", "", board[0][0], "", board[0][1], "", board[0][2], "-")
        print("-", "", board[1][0], "", board[1][1], "", board[1][2], "-")
        print("-", "", board[2][0], "", board[2][1], "", board[2][2], "-")
        print("-", "", board[3][0], "", board[3][1], "", board[3][2], "-")
        print("-----------------------------------------")




#------------------------------------------------cb class--------------------------------#
#cb class is shogi_label click that open event
class ClickManager():
    def ClickLabel(self,widget):
        #---위젯 클릭-----#
        widget.bind("<ButtonPress-1>",self.order_main)
        #------------플레이어체크--------#
    def player_check(self,value):
        value = int(value)
        if  (value >0):
            return 1  #1p
        elif(value < 0):
            return 2  #2p
     # ---------움직이도록 하는 라벨 만들기------------------------------------------------#
    def move_label(self,array,x,y,value):
        storge = []
        ori_x, ori_y = x,y
        g = 0
        check_value = [0,0,0,0,0,0,0,0]
        for i in range(0,len(array),1):
            j = 0
            shogi_value = 0
            x_1,y_1 = x + array[i][j], y + array[i][j+1]
            for k in range(0,8,1):
                search = shogi_label[k].place_info()
                search_x,search_y = int(search['x']),int(search['y'])
                if(search_x == x_1 and search_y == y_1):
                    shogi_value = int(shogi_label[k].cget("textvariable"))

                    if(shogi_value > 0):
                        check_value[i] = shogi_value
                    elif(shogi_value < 0):
                        check_value[i] = shogi_value
        for i in range(0,8,1):
            if(array[i][0] != 500 and check_value[i] ==0):
                check_value[i] = 7
            #print(check_value)
            x_1 = ori_x
            y_1 = ori_y
            #print(who_turn, shogi_value, check_value
        for i in range(0,len(array),1):
            j = 0
            x_1, y_1 = x + array[i][j], y + array[i][j + 1]
            if (value == 1):
                sto = Label(root, image=blur_p_r_img_1)
            elif (value == -1):
                sto = Label(root, image=blur_p_img_1)
            elif (abs(value) == 2):
                sto = Label(root, image=blur_p_img_2)
            elif (abs(value) == 3):
                sto = Label(root, image=blur_p_img_3)
            elif (abs(value) == 4):
                sto = Label(root, image=blur_p_img_4)
            if (x_1 > 0 and y_1 > 0 and x_1 < 421 and y_1 < 560):
                if(value > 0):
                    if(check_value[i] ==7 or check_value[i] < 0):
                        #print(check_value[k])
                        storge.append(sto)
                        #x값과 y값이 출력이 안됩니다
                        storge[g].place(x=x_1, y=y_1)
                        move = Move()
                        move.Move_label(storge[g])
                        g = g + 1
                if (value < 0):
                    if (check_value[i] ==7 or check_value[i] > 0):
                        storge.append(sto)
                        # x값과 y값이 출력이 안됩니다
                        storge[g].place(x=x_1, y=y_1)
                        move = Move()
                        move.Move_label(storge[g])
                        g = g + 1

        return storge
        x_1 = ori_x
        y_1 = ori_y


    #------------------------------좌표 탐색-------------------------------------------------#
    def create_label(self,value):
        direction = [[0, -140], [140, -140], [140, 0], [140, 140], [0, 140], [-140, 140], [-140, 0],[-140, -140]]  # 12시부터
        value = int(value)
        if  (value == 1):
            direction = [[500,500],[0,140],[500,500],[500,500],[500,500],[500,500],[500,500],[500,500]]
        elif(value ==-1):
            direction = [[500,500],[500,500],[500,500],[500,500],[0,-140],[500,500],[500,500],[500,500]]
        elif(abs(value) ==2):
            direction = [[0,-140],[500,500],[140,0],[500,500],[0,140],[500,500],[-140,0],[500,500]]
        elif(abs(value) ==3):
            direction = [[0, -140], [140, -140], [140, 0], [140, 140], [0, 140], [-140, 140], [-140, 0],[-140, -140]]
        elif(abs(value)==4):
            direction = [[500,500],[140,-140],[500,500],[140,140],[500,500],[-140,140],[500,500],[-140,-140]]
        return direction

    #----------------------------클래스 메인-------------------------------#
    def order_main(self,event):
        try:

            aaaa =event.widget.place_info()
            global set_label,storge,who_turn,poro_1p,poro_2p,king_1p_win,king_2p_win,ori_count_1
            set_label = event.widget
            who_turn = event.widget.cget("textvariable")
            for i in range(0,len(shogi_label),1):
                king_value = shogi_label[i].cget("textvariable")
                if(king_value ==3):
                    p_1_king = shogi_label[i].place_info()
                    y_1 =int(p_1_king['y'])
                    if (y_1 == 422):
                        king_1p_win = 1
                        print(1)
                    ori_count_1 = game_count
                if(king_value == -3):
                    p_2_king =  shogi_label[i].place_info()
                    y_2 = int(p_2_king['y'])
                    if (y_2 == 2):
                        king_2p_win = 1
                        print("d",1)
                    ori_count_1 = game_count
            what_label = event.widget.place_info()
            what_label_x,what_label_y = int(what_label['x']), int(what_label['y'])
            
            if (game_count % 2 == 0):
                if (self.player_check(who_turn) == 1):
                    direction = self.create_label(who_turn)
                    storge = self.move_label(direction,what_label_x,what_label_y,who_turn)

            else:
                if(self.player_check(who_turn)==2):
                    direction = self.create_label(who_turn)
                    storge = self.move_label(direction, what_label_x, what_label_y, who_turn)
                    
        except:
            pass
#----------------UI 디자인 -----------------#

root.geometry("1000x640")
root.resizable(False,False)
root.config(background = "black")
#---장기 판 설정----#
shogi_board = PhotoImage(file="shogi_board.png")
board = Label(root, image = shogi_board)
board.place(x = 0, y = 0 )

#--------------------------------이미지 설정----------------------------------------#
#자
image1 = Image.open("shogi2.png")
p_image1 = ImageTk.PhotoImage(image1)

rotate_img_1 = image1
rotate_p_img = ImageTk.PhotoImage(rotate_img_1.rotate(180))
blur_img_1 = image1
blur_img_1.putalpha(100)
blur_p_img_1 = ImageTk.PhotoImage(blur_img_1)
blur_p_r_img_1 = ImageTk.PhotoImage(blur_img_1.rotate(180))

#장
image2 = Image.open("shogi3.png")
p_image2 = ImageTk.PhotoImage(image2)
blur_img_2 = image2
blur_img_2.putalpha(100)
blur_p_img_2 = ImageTk.PhotoImage(blur_img_2)
#왕
image3 = Image.open("shogi1.png")
p_image3 = ImageTk.PhotoImage(image3)
blur_img_3 = image3
blur_img_3.putalpha(100)
blur_p_img_3 = ImageTk.PhotoImage(blur_img_3)
#상
image4 = Image.open("shogi4.png")
p_image4 = ImageTk.PhotoImage(image4)
blur_img_4 = image4
blur_img_4.putalpha(100)
blur_p_img_4 = ImageTk.PhotoImage(blur_img_4)

#배열저장
img = [image1,image2,image3,image4]
p_img = [p_image1,p_image2,p_image3,p_image4]
blur_p_img = [blur_p_img_1,blur_p_img_2,blur_p_img_3,blur_p_img_4]

#-----------------------------------------라벨 이미지 저장--------------#
label_cnt = 0
fine = 0
c = 1
shogi_label = []
while (True):
    fine = fine  + 1
    if (fine == 0):
        break
    if(fine ==4):
        label_1 = Label(root,textvariable = fine, image = p_img[label_cnt])
        shogi_label.append(label_1)
        fine = fine - 9
        label_cnt = 3
        c = -1
    else:
        if(fine == 1):
            label_1 = Label(root, textvariable=fine, image=rotate_p_img)
            shogi_label.append(label_1)

        else:
            label_1 = Label(root, textvariable=fine, image=p_img[label_cnt])
            shogi_label.append(label_1)

        label_cnt = label_cnt + c

#--------------------------------------------배치--------------#
shogi_label[0].place(x = 142,y = 142)
shogi_label[1].place(x = 2,  y = 2)
shogi_label[2].place(x = 142,y = 2)
shogi_label[3].place(x = 282,y = 2)
shogi_label[4].place(x = 282,y = 422)
shogi_label[5].place(x = 142,y = 422)
shogi_label[6].place(x = 2,  y = 422)
shogi_label[7].place(x = 142,y = 282)

#---------------------------------------------클래스 집어넣기------------------#

cm = ClickManager()
for i in range(0,8,1):
    cm.ClickLabel(shogi_label[i])
board = [0,0,0],[0,0,0],[0,0,0],[0,0,0]
place_board = []
for i in range(0, 8, 1):
    select = {}
    sear = shogi_label[i].place_info()
    sear_x, sear_y = int(sear['x']), int(sear['y'])
    select["x"], select["y"], select['name'] = sear_x, sear_y, int(shogi_label[i].cget("textvariable"))
    place_board.append(select)
#print(place_board)
place_board_y_2 = []
place_board_y_142 = []
place_board_y_282 = []
place_board_y_422 = []
print_board = []
check = [2,142,282,422]

for i in range(0,8,1):
#if(place_board[i]['name'] > 0):
    if(place_board[i]['y'] ==2):
        place_board_y_2.append(place_board[i])
    elif(place_board[i]['y'] ==142):
        place_board_y_142.append(place_board[i])
    elif(place_board[i]['y'] ==282):
        place_board_y_282.append(place_board[i])
    elif(place_board[i]['y']==422):
        place_board_y_422.append(place_board[i])
print_board =[place_board_y_2,place_board_y_142,place_board_y_282,place_board_y_422]

print(print_board[0][1])
for i in range(0,len(print_board),1):
    for j in range(0,len(print_board[i]),1):
        if(print_board[i][j]['x']==2):
            board[i][0] = print_board[i][j]['name']
        elif(print_board[i][j]['x']==142):
            board[i][1] =print_board[i][j]['name']
        elif(print_board[i][j]['x']==282):
            board[i][2] = print_board[i][j]["name"]

print("-----------------------------------------")
print("-","",board[0][0],"",board[0][1],"",board[0][2],"-")
print("-","",board[1][0],"" ,board[1][1],"",board[1][2],"-")
print("-","",board[2][0],"" ,board[2][1],"",board[2][2],"-")
print("-","",board[3][0],"" ,board[3][1],"",board[3][2],"-")
print("-----------------------------------------")
#print(place_board)
#print(place_board_y_2)
#print(place_board_y_142)
#print(place_board_y_282)
#print(place_board_y_422)


#-------------------------------------------- 게임 규칙 설명-------------#

"""
게임이 시작되면 선 플레이어부터 말 1개를 1칸 이동시킬 수 있다. 말을 이동시켜 상대방의 말을 잡은 경우, 해당 말을 포로로 잡게 되며 포로로 잡은 말은 다음 턴부터 자신의 말로 사용할 수 있다.

게임 판에 포로로 잡은 말을 내려놓는 행동도 턴을 소모하는 것이며 이미 말이 놓여진 곳이나 상대의 진영에는 말을 내려놓을 수 없다.

상대방의 후(侯)를 잡아 자신의 말로 사용할 경우에는 자(子)로 뒤집어서 사용해야 한다.

게임은 한 플레이어가 상대방의 왕(王)을 잡으면 해당 플레이어의 승리로 종료된다.

하지만 자신의 왕(王)이 상대방의 진영에 들어가 자신의 턴이 다시 돌아올 때까지 한 턴을 버틸 경우 해당 플레이어의 승리로 게임이 종료된다.
결승전에는 아래와 같은 규칙과 아이템이 추가된다.
"""
root.mainloop()
