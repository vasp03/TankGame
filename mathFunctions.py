from tkinter import *

class math:
    def __init__(self,lastEquation,lastFunction,method_list):
        self.lastFunction = lastFunction
        self.lastEquation = lastEquation
        self.method_list = method_list

    def area():
        def square(a:int,b:int):
            math.lastFunction="area_square"
            math.lastEquation=a*b
            print(math.lastEquation)
        
        def triangle(a:int,b:int):
            math.lastFunction="area_triangle"
            math.lastEquation=a*b/2
            print(math.lastEquation)

    def latestEquation():
        print(math.lastFunction,math.lastEquation)

    def choose_function():
        math.method_list = [method for method in dir(math) if method.startswith('__') is False]
        
# math.choose_function()
math.square(2,4)
print(math.method_list)

def temp(a):
    print(a)



# testList = [1,2,3,4,5]

# top = Tk()
# top.geometry("200x250")
# lbl = Label(top,text = "A list of favourite countries...")  

# list = Listbox(top)
# number=0
# for i in math.method_list:
#     list.insert(number,i)
#     number+=1

# btn = Button(top, text = "Choose", command = lambda listbox=list: temp(ANCHOR))
# lbl.pack()
# list.pack()
# btn.pack()

# menubar = Menu(top)  
# menubar.add_command(label="Quit!", command=top.quit)  
# top.config(menu=menubar)  

# top.mainloop()  

