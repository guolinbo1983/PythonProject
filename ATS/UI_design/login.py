import tkinter as tk
import tkinter.messagebox as msgbox
class LogIn():
    def __init__(self):
        self.__lonin_permission = False
        self.login = tk.Tk()
        self.login.title("登陆系统")
        self.width = 400
        self.height = 300
        self.xPosition = int((self.login.winfo_screenwidth()-self.width)/2)
        self.yPosition = int((self.login.winfo_screenheight()-self.height)/2)
        self.login.geometry("{}x{}+{}+{}".format(self.width,self.height,
                                                 self.xPosition,self.yPosition)) #设置窗体居中
        #设置logo
        self.photo = tk.PhotoImage(file="../Icon/comba.png")
        tk.Label(self.login,image=self.photo).grid(row=0,column=0)
        self.namelabel = tk.Label(self.login,text="用户名",font=("微软雅黑",20),justify=tk.LEFT)
        self.namelabel.grid(row=1,column=0,padx=5,pady=5)
        self.passwordlabel = tk.Label(self.login,text="密  码",font=("微软雅黑",20),justify=tk.LEFT)
        self.passwordlabel.grid(row=2,column=0,padx=5,pady=5)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.userentry = tk.Entry(self.login,textvariable=self.username)
        self.userentry.focus_set()  #默认激活用户名窗口
        self.passwordentry = tk.Entry(self.login,textvariable=self.password,show="*")
        self.passwordentry.bind("<Key-Return>",self.login_request2)  #如果密码输入完成后直接回车也可以登陆
        self.userentry.grid(row=1,column=1)
        self.passwordentry.grid(row=2,column=1)

        #设置登陆按钮
        self.loginbutton = tk.Button(self.login,text="登陆",font=("微软雅黑",20),command=self.login_request)
        self.quitbutton = tk.Button(self.login,text="退出",font=("微软雅黑",20),command=self.login.quit)
        self.loginbutton.grid(row=3,column=0)
        self.quitbutton.grid(row=3,column=1)

        self.login.mainloop()

    def login_request2(self,event):
        msgbox.showinfo("信息","登陆成功")
        self.__lonin_permission = True
    def login_request(self):
        msgbox.showinfo("信息","登陆成功")
        self.__lonin_permission = True

    def loninSuccess(self):
        if self.__lonin_permission:
            return True
        else:
            return False
LogIn()