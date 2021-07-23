from random import randint
from tkinter import Button,Label,Tk,StringVar   
class roll:
    color=["#F60000","#FF8C00","#FFEE00","#4DE94C","#3783FF","#4815AA"]
    dice_face=["⚀","⚁","⚂","⚃","⚄","⚅"]
 
    def __init__(self):
        self.root =Tk()
        self.root.title("Roll the Dice")
        self.root.minsize(250,250)
        self.root.maxsize(250,250)
        self.dice_value="⬛"
        self.Btntxt=StringVar()
        self.Btntxt.set("Roll")
        self.lable = Label(self.root,width=20,height=20,text=self.dice_value,font=("times",200))
        self.btn=Button(self.root,textvariable=self.Btntxt,bg="teal",fg="black",command=self.rollDice).place(x=0,y=230,width=125,height=20)
        self.btn2=Button(self.root,text="Quit",bg="teal",fg="black",command=self.root.destroy).place(x=125,y=230,width=125,height=20)
        self.lable.pack()

        self.root.mainloop()
    
    def rollDice(self):
        self.seconds=0
        self.n=randint(0,5)
        self.Btntxt.set("Roll Again")
        color=str(self.color[self.n])
        self.root.config(bg=color)
        self.lable.config(bg=color)
        self.lable.after(100,self.refresh_label)
    def refresh_label(self):
        if(self.seconds>5):
            self.lable.configure(text=self.dice_face[self.n])
            self.seconds=0   
        else:
            self.seconds += 1
            self.lable.configure(bg=self.color[randint(0,5)],text=self.dice_face[randint(0,5)])
            self.lable.after(100, self.refresh_label)
dice=roll()
