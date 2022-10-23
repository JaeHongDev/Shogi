from tkinter import *


root = Tk()
root.resizable(False,False)
#클래스 제작

def drawcircle(x,y):
    label = Label(root, text = x)
    
    #label.place(
    
class DragManager():
    
    def Check(self,event): #숫자 체크     
        a = event.widget.cget("textvariable")
        #print(abs(a))
        if(abs(a) == 1): # 상하 움직이는 말
            return a
        elif(abs(a) == 2):# 상하좌우 움직이는 
            return a
        elif(abs(a) == 3): #대각선 움직이는 말
            return a
        elif(abs(a) == 4): # 바라보고 있는 방향으로 움직이는 말들
            return a
    def add_drag(self,widget):          
        widget.bind("<ButtonPress-1>",self.drag_start) #잡았을때
        #잡았을때
        widget.bind("<B1-Motion>",self.drag_moving) # 움직일때
        widget.bind("<ButtonRelease-1>",self.drag_finish) #내려놨을때 


    def drag_start(self,event): #잡았을때 
        self.Check(event)
        #x,y = event.x,event.y #그림의 좌표
    
       
          
        global r_x,r_y #좌표받
        r_x,r_y = event.widget.winfo_pointerxy()
        r_x = r_x -140
        r_y = r_y -140
        #print(r_x,r_y)
        #event.widget.place(x = r_x,y =r_y)          
    def drag_moving(self,event):
        #print(x1,y1)좌표 받기 성공
        global x1, y1
        x1, y1 = event.widget.winfo_pointerxy()  # 현재 마우스 좌표 받음
        #119, 105 는 세로와 가로 크기
        x1 = x1- 140  #135가로길이
        y1 = y1- 140  #세로길이 
        event.widget.place(x=x1, y=y1)
        

    def drag_finish(self,event):
        try:
            #현재 위치가 어딘교?
            print(x1,y1)
        except:
            pass
    
       
root.geometry("640x640") #전체 배경 


shogi_board = PhotoImage(file="shogi_board.png") #십이장기
board = Label(root,image = shogi_board)
board.place(x=0,y=0)
root.configure(background = "black") # 배경

image = PhotoImage(file = "shogi4.png")
image1= PhotoImage(file = "shogi1.png")
image2 = PhotoImage(file = "shogi2.png")
image3 = PhotoImage(file = "shogi3.png")

shogi_label0 = Label(root,textvariable =  1,image = image2)
shogi_label1 = Label(root,textvariable =  2,image = image)
shogi_label2 = Label(root,textvariable =  3,image = image3)
shogi_label3 = Label(root,textvariable =  4,image = image1)
shogi_label4 = Label(root,textvariable = -4,image = image1)
shogi_label5 = Label(root,textvariable = -1,image = image2)
shogi_label6 = Label(root,textvariable = -2,image = image)
shogi_label7 = Label(root,textvariable = -3,image = image3)

s_p_r =[0,140,140,280] #shogi_place_row
s_p_c =[0,140,280,420] #shogi_place_col

shogi_label0.place(x = 2,  y = 2)
shogi_label1.place(x = 142,y = 2)
shogi_label2.place(x = 282,y = 2)
shogi_label3.place(x = 143,y = 142)
shogi_label4.place(x = 143,y = 282)
shogi_label5.place(x = 2,  y = 422)
shogi_label6.place(x = 142,  y = 422)
shogi_label7.place(x = 282,  y = 422)





#label.place(x = 5, y = 5) # 장기판 가운데에 오도록 함
"""board = [ 1, 2, 3,
          0, 4, 0,
          0,-4, 0,
         -1,-2,-3]
"""
dnd = DragManager()
dnd.add_drag(shogi_label0)
dnd.add_drag(shogi_label1)
dnd.add_drag(shogi_label2)
dnd.add_drag(shogi_label3)
dnd.add_drag(shogi_label4)
dnd.add_drag(shogi_label5)
dnd.add_drag(shogi_label6)
dnd.add_drag(shogi_label7)
root.mainloop()
