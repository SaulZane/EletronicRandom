# 使用tkinter制作电子骰子
# 导入tkinter模块
import random
import tkinter as tk

# 创建窗口
window = tk.Tk()
# 设置窗口标题
window.title('骰子')
# 设置窗口大小
window.geometry('200x200')
# 创建骰子面板
dice_label = tk.Label(window, text='骰子', font=('Arial', 20), width=10, height=2)
dice_label.pack()

#

# 禁用最大化按钮
window.resizable(0, 0)

#设置为窗口嘴前端
window.attributes("-topmost", True)

# 创建投掷骰子按钮
def roll_dice():
    # 随机生成1-6的数
    dice_num = random.randint(1, 9)
    # 设定回答人员
    people: str = [ '王久安', '张伟', '张树勋', '李雅君', '张宏宇', '蒲津', '高瑾', '高丽娜',
                   '沈兴愉']
    answer = people[dice_num - 1]
    # 设置骰子面板的文本
    dice_label.config(text=answer, font=('微软雅黑', 30, 'bold'), fg="green")


# 创建按钮
button = tk.Button(window, text='选定回答人员', font=('微软雅黑', 15), width=10, height=2, command=roll_dice)
button.pack()

dice_labe2 = tk.Label(window, text='©2023张硕|保留所有权利', font=('Arial', 10), width=30, height=7)
dice_labe2.pack()



# 运行窗口
window.mainloop()
