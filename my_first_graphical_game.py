from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import re
import sys,os



class singleton:

    instance=None

    def __new__(cls,master):
        if cls.instance==None:
            cls.instance=singleton.Mygame(master)
            

        

        return cls.instance    

    class Mygame:
        # structure=["{}.{}".format(i,j)  for i in range(1,11) for j in range(25)  ]
        L=["_|"]*24
        player_valid_moves=["{}.{}".format(i,j)  for i in range(1,11)  for j in range(24)  if j%2==0 ]
        

        def __init__(self,master):
            self.master=master
            
           
            
            master.title("GAME")
            master.config(bg="#e1d8b9")
            master.geometry('480x450+200+200')
            master.resizable(False,False)

            
            

            self.frame1=ttk.Frame(master)
            self.frame1.config(relief=RAISED)
            self.frame1.pack()
            
            self.view=StringVar()

            

            self.text=Text(self.frame1,width=38,font=(40),wrap="char",height=10,bd=30,bg="light blue",fg='black')
            self.text.pack(fill=BOTH,expand=True)
            
            self.frame2=ttk.Frame(master)
            self.frame2.config(relief=GROOVE)

            self.frame2.bind('<F5>',sys.exit)
            self.frame2.pack()

            self.up_b=Button(self.frame2,bg="black",padx=10,pady=5,fg="white",bd=10,text="UP",command=self.sub_y)
            self.up_b.pack(side=TOP)
            self.down_b=Button(self.frame2,bg="black",fg="white",padx=10,pady=5,bd=10,text="DOWN",command=self.add_y)
            self.down_b.pack(side=BOTTOM)

            self.left_b=Button(self.frame2,bg="black",fg="white",padx=10,pady=5,bd=10,text="LEFT",command=self.sub_x)
            self.left_b.pack(side=LEFT)

            self.right_b=Button(self.frame2,bg="black",fg="white",padx=10,pady=5,bd=10,text="RIGHT",command= self.add_x)
            self.right_b.pack(side=RIGHT)
            
            self.submit=Button(self.frame2,bg="black",fg="white",padx=5,pady=5,bd=10,state=['normal'],text="I WANT TO.",command=self.submit_act)
            self.submit2=Button(self.frame2,bg="black",fg="white",padx=5,pady=5,bd=10,state=['normal'],text="NO THANKS.",command=sys.exit)
            
            
            
            
            
            

            # messagebox.showinfo(title="welcome",message="welcome to my game")

            


        

            self.player,self.door,self.monster=random.sample(self.player_valid_moves,3)

            self.map()

            self.master.bind('<Escape>',sys.exit)

            self.master.bind("<Up>",self.sub_y_keyboard)
            self.master.bind("<Down>",self.add_y_keyboard)
            self.master.bind("<Left>",self.sub_x_keyboard)
            self.master.bind("<Right>",self.add_x_keyboard)
            

        def map(self):
            
            
            self.text.configure(state=["normal"])
            self.master.bind("<Return>",None)

         
            
            for i in range(1,11):

                self.text.insert('1.0','{}\n'.format(''.join(self.L)))
            self.text.delete('11.0',END)

            self.text.delete('{}'.format(self.player))
            self.text.insert(self.player,"x")
            os.system("cls")
            print('player=',self.player)
            print('monster=',self.monster)
            print('door=',self.door) 
            self.play_game() 
            self.text.configure(state=["disabled"])
           
            
                
        
            

        def play_game(self):
            
            
            
            if self.player==self.monster  or self.player==self.door:
                if self.player==self.monster:
                    messagebox.showinfo(title='loooooose',message='you lose!')
                    self.text.config(bg='red')
                    



                elif self.player==self.door:
                    messagebox.showinfo(title='wiiiiiiiiin',message='you win!')
                    self.text.config(bg='light green')
                    
                

                self.up_b.pack_forget()
                self.down_b.pack_forget()
                self.left_b.pack_forget()
                self.right_b.pack_forget()
                

                self.submit.pack(side=RIGHT)
                self.submit2.pack(side=LEFT)

                self.clear()
                t=''' DO YOU WANT TO PLAY AGIAN? \nPRESS [ENTER] TO PLAY AGIAN. \nPRESS [ECS] TO EXIT.'''
                self.text.insert('1.0',t)
                self.master.bind('<Return>',self.submit_act_keyboard)
               

            else:
                self.master.bind('<Return>',None) 
                self.submit.pack_forget()
                self.submit2.pack_forget()
                self.up_b.pack(side=TOP) 
                self.down_b.pack(side=BOTTOM)  
                self.left_b.pack(side=LEFT)
                self.right_b.pack(side=RIGHT)
                
                self.text.config(bg='light blue')

                
                
                

                

                
            
                
            

        def submit_act(self):
            self.clear()
            self.player,self.door,self.monster=random.sample(self.player_valid_moves,3)
            self.map()

        def submit_act_keyboard(self,event):
            self.clear()
            self.player,self.door,self.monster=random.sample(self.player_valid_moves,3)
            self.map()    
            
            

            
            
                    
                    
                            
        def add_x(self):
           

            self.clear()
            x=re.split("[.]",self.player)

            
            if  int(x[-1])<46:
                z=str(int(x[-1])+2)

                del x[-1]
                x.append(z)
            
                self.player='.'.join(x)
            self.map()

          
            
        

        def sub_x(self):
           
            self.clear()
            x=re.split("[.]",self.player)

            
            if int(x[-1]) >0 :
                z=str(int(x[-1])-2)

                del x[-1]
                x.append(z)
            
                self.player='.'.join(x)
            self.map()       
            

        def add_y(self):
         
            self.clear()
            x=re.split("[.]",self.player)

            
            if  int(x[0])<=9:
                z=str(int(x[0])+1)

                del x[0]
                x.insert(0,z)
            
                self.player='.'.join(x)
            self.map()






        def sub_y(self):
          
            self.clear()
            x=re.split("[.]",self.player)

            
            if  int(x[0])>1:
                z=str(int(x[0])-1)

                del x[0]
                x.insert(0,z)
            
                self.player='.'.join(x)
            self.map()
            


        def clear(self):
            self.text.delete("1.0","end")


        def add_x_keyboard(self,event):
           

            self.clear()
            x=re.split("[.]",self.player)

            
            if  int(x[-1])<46:
                z=str(int(x[-1])+2)

                del x[-1]
                x.append(z)
            
                self.player='.'.join(x)
            self.map()      
        

        def sub_x_keyboard(self,event):
           
            self.clear()
            x=re.split("[.]",self.player)

            
            if int(x[-1]) >0 :
                z=str(int(x[-1])-2)

                del x[-1]
                x.append(z)
            
                self.player='.'.join(x)
            self.map()  


        def add_y_keyboard(self,event):
         
            self.clear()
            x=re.split("[.]",self.player)

            
            if  int(x[0])<=9:
                z=str(int(x[0])+1)

                del x[0]
                x.insert(0,z)
            
                self.player='.'.join(x)
            self.map()  

        def sub_y_keyboard(self,event):
          
            self.clear()
            x=re.split("[.]",self.player)

            
            if  int(x[0])>1:
                z=str(int(x[0])-1)

                del x[0]
                x.insert(0,z)
            
                self.player='.'.join(x)
            self.map()      


def main():
    root=Tk()
   

    singleton(root)
    

    root.mainloop()


if __name__=="__main__":
    main()