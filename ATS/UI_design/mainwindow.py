import tkinter as tk

class MainWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ATS测试系统")
        self.root.geometry("{_wide}x{_height}".\
                           format(_wide=self.root.winfo_screenwidth(),\
                                  _height=self.root.winfo_screenheight()))
        self.root.attributes("-topmost",True) #覆盖window的开始栏，实现真正的全屏

        #构建菜单
        #构建主界面

    def start(self):
        self.root.mainloop()

    def qiut(self):
        self.root.quit()

if __name__ =="__main__":
    window = MainWindow()
    window.start()