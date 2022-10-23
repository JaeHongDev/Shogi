from tkinter import *
from PIL import Image,ImageTk

root = Tk()

root.resizable(False,False)
#클래스 제작

class move():
    def m_click(self,widget):

        widget.bind("<ButtonPress-1>",self.Click_here)


    def Click_here(self,event): #이미지 불러오기

        a = event.widget.place_info()
        global m_x,m_y
        m_x,m_y= int(a['x']),int(a['y'])

        #print(set_label.winfo_x ,set_label.winfo_y())
        #좌표탐색
        for i in range(0,8,1):
            search_x,search_y = shogi_label[i].winfo_x(),shogi_label[i].winfo_y()
            #print(search_x,search_y)
            if(search_x ==m_x and search_y ==m_y):
                shogi_label[i].place(x = 480,y=2)
                break;
        set_label.place(x=m_x, y=m_y)

        i = 0
        for des in storge:
            storge[i].destroy()
            i = i+1

class DragManager():

    def Check(self,event): #이미지 넣기
        global a
        a = event.widget.cget("textvariable")
        #print(abs(a))
        if(abs(a) == 1): # 상하 움직이는 말
            #print("자")

            return image1
        elif(abs(a) == 2):# 상하좌우 움직이는
            #print("차")

            return image2
        elif(abs(a) == 3): #대각선 움직이는 말
            #print("왕")

            return image3
        elif(abs(a) == 4): # 바라보고 있는 방향으로 움직이는 말들
            #print("상")

            return image4
    def create_label(self,event,x_1,y_1): #클릭-라벨-이동
        count = 0
        a = [[0,0],[0,-140],[140,-140],[140,0],[140,140],[0,140],[-140,140],[-140,0],[-140,-140]]  #12시부터

        global storge
        storge = []
        x_1,y_1= int(x_1),int(y_1)

        ori_x, ori_y = x_1, y_1


        check_value = self.move_mal(event)
        if(check_value == 1):
            i = 0
            g = 0
            while(i<9):
                j = 0
                if(i==0 or i==5):
                     x_1, y_1 = x_1 + a[i][j], y_1 + a[i][j + 1]
                     if (x_1 > 0 and y_1 > 0 and x_1 < 421 and y_1 < 560):

                        sto = Label(root, image = r_img1)
                        storge.append(sto)
                        storge[g].place(x = x_1,y = y_1)
                        Move = move()
                        Move.m_click(storge[g])
                        g = g+1
                x_1 = ori_x
                y_1 = ori_y
                i = i + 1
        elif(check_value == -1):
            i = 0
            g = 0
            c_img = ImageTk.PhotoImage(img[0])
            while (i < 9):
                j = 0
                if (i == 0 or i == 1):
                    x_1, y_1 = x_1 + a[i][j], y_1 + a[i][j + 1]
                    if (x_1 > 0 and y_1 > 0 and x_1 < 421 and y_1 < 560):
                        sto = Label(root, image=s_image0)
                        storge.append(sto)
                        storge[g].place(x=x_1, y=y_1)
                        Move = move()
                        Move.m_click(storge[g])
                        g = g + 1
                x_1 = ori_x
                y_1 = ori_y
                i = i + 1

        elif(check_value ==2):
            i = 0
            g = 0
            count = 0
            while(i<9):
                #print("카",count,i)
                j = 0
                x_1, y_1 = x_1 + a[i][j], y_1 + a[i][j + 1]
                if(i == 0 or i % 2 != 0):
                    if(x_1 > 0 and y_1 > 0 and x_1 <421 and y_1 <560):
                        #print(x_1, y_1)
                        sto = Label(root, image = s_image1)
                        storge.append(sto)
                        #print("1",i,storge[i])
                        storge[g].place(x=x_1,y=y_1)
                        Move = move()
                        Move.m_click(storge[g])
                        g = g +1
                x_1 = ori_x
                y_1 = ori_y
                i = i+1

        elif(check_value ==3):
            for i in range(0,9,1):
                 j = 0
                 x_1, y_1 = x_1 + a[i][j], y_1 + a[i][j + 1]

                 if(x_1>0 and y_1 >0 and x_1 <421 and y_1 < 560):
                    sto = Label(root, image=s_image2)
                    i = i -count
                    storge.append(sto)
                    storge[i].place(x = x_1, y= y_1)
                    Move = move() #라벨-이동
                    Move.m_click(storge[i])
                 else:
                    count = count +1
                 x_1 = ori_x
                 y_1 = ori_y
        elif(check_value ==4):
            i = 0
            g = 0
            count = 0
            while (i < 9):
                # print("카",count,i)
                j = 0
                x_1, y_1 = x_1 + a[i][j], y_1 + a[i][j + 1]
                #print(y_1)
                if (i == 0 or i % 2 == 0):
                    if (x_1 > 0 and y_1 > 0 and x_1 < 421 and y_1 < 560):
                        # print(x_1, y_1)
                        sto = Label(root, image=s_image3)
                        storge.append(sto)
                        # print("1",i,storge[i])
                        storge[g].place(x=x_1, y=y_1)
                        Move = move()
                        Move.m_click(storge[g])
                        g = g + 1
                    else:
                        # print(i,"해당안됨")
                        count = count + 1
                else:
                    # print(i, "해당안됨")
                    count = count + 1
                x_1 = ori_x
                y_1 = ori_y
                i = i + 1
    def move_mal(self, event):# "말 들의 움직이는 범위"
        a = event.widget.cget("textvariable")
        if(a == -1):
            return -1
        elif(a==1):
            return 1
        a = abs(a)
        if(a == 3):
            return 3
        elif(a==2):
            return 2
        elif(a==4):
            return 4
    def add_drag(self,widget): #이미지 클릭
        widget.bind("<ButtonPress-1>",self.drag_start) #잡았을때
        #잡았을때
    def drag_start(self,event): #잡았을때
        label_dic = event.widget.place_info()  # 라벨의 속성을 딕셔너리에 저장한다
        x_1 = label_dic['x']
        y_1 = label_dic['y']
        global set_label,des_label
        #print(label_dic)
        set_label = event.widget
        self.create_label(event,x_1,y_1)
root.geometry("1000x640") #전체 배경
shogi_board = PhotoImage(file="shogi_board.png") #십이장기
board = Label(root,image = shogi_board)
board.place(x=0,y=0)
root.configure(background = "black") # 배경


image3 = Image.open("shogi1.png")
p_image3 = ImageTk.PhotoImage(image3)

image1 = Image.open("shogi2.png")
p_image1 = ImageTk.PhotoImage(image1)
image2 = Image.open("shogi3.png")
p_image2 = ImageTk.PhotoImage(image2)

image4 = Image.open("shogi4.png")
p_image4 = ImageTk.PhotoImage(image4)


img =[image1,image2,image3,image4]
p_img = [p_image1,p_image2,p_image3,p_image4]

s_img = img




label_cnt = 0
fine = 0
c = 1
shogi_label = []

while (True):
    fine = fine  + 1
    print(fine)
    if (fine == 0):
        break
    if(fine ==4):
        label_1 = Label(root,textvariable = fine, image = p_img[label_cnt])
        #print(label_cnt,fine,label_1)
        shogi_label.append(label_1)

        fine = fine - 9
        label_cnt = 3
        c = -1
    else:
        if(fine == 1):
            r_img = ImageTk.PhotoImage(img[label_cnt].rotate(180))
            label_1 = Label(root, textvariable=fine, image=r_img)
            shogi_label.append(label_1)
            # print(label_cnt, fine,label_1)

        else:
            label_1 = Label(root, textvariable=fine, image=p_img[label_cnt])
            shogi_label.append(label_1)
            #print(label_cnt, fine,label_1)
        label_cnt = label_cnt + c

"""
#shogi_label0.place(x = 2,  y = 2)

"""
#x = shogi_label0.place_info()
shogi_label[0].place(x = 142,y = 142)
shogi_label[1].place(x = 2,  y = 2)
shogi_label[2].place(x = 142,y = 2)
shogi_label[3].place(x = 282,y = 2)
shogi_label[4].place(x = 282,y = 422)
shogi_label[5].place(x = 142,y = 422)
shogi_label[6].place(x = 2,  y = 422)
shogi_label[7].place(x = 142,y = 282)
#label.place(x = 5, y = 5) # 장기판 가운데에 오도록 함
"""board = [ 1, 2, 3,
          0, 4, 0,
          0,-4, 0,
         -1,-2,-3]
"""
s_img[0].putalpha(100)
s_img[1].putalpha(100)
s_img[2].putalpha(100)
s_img[3].putalpha(100)

s_image0 = ImageTk.PhotoImage(s_img[0])
s_image1 = ImageTk.PhotoImage(s_img[1])
s_image2 = ImageTk.PhotoImage(s_img[2])
s_image3 = ImageTk.PhotoImage(s_img[3])
img[0].putalpha(100)
r_img1 = ImageTk.PhotoImage(img[0].rotate(180))


dnd = DragManager()
dnd.add_drag(shogi_label[0])
dnd.add_drag(shogi_label[1])
dnd.add_drag(shogi_label[2])
dnd.add_drag(shogi_label[3])
dnd.add_drag(shogi_label[4])
dnd.add_drag(shogi_label[5])
dnd.add_drag(shogi_label[6])
dnd.add_drag(shogi_label[7])

frame = Frame(root)
frame.place(x = 560,y=2)


root.mainloop()
