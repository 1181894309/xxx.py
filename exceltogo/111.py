赐v  import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import  pandas as pd

root = tk.Tk()
root.minsize(300,50)
def callback():
    filepath = tk.filedialog.askopenfilename()
    return filepath
tk.Button(root, text="打开你需要操作的文件", command=callback).pack()

filepath=callback()

root.mainloop()
print(filepath)      # C:/Users/admin/Desktop/1111.xlsx
# df=pd.read_excel(file_path,header=1)  #读取文件内容,并且以第二行为列名
# # print(len(df))  行数
# # print(df.shape[1])  列数
# print(df)
# print("+++++++++++++++++++++++++")
# df2=df[df.目标3.between(1, 5)]


法法规的
是
上的方法


12132123
阿斯顿发

阿斯顿发
上的方法