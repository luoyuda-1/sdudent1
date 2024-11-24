from tkinter import messagebox, simpledialog, Tk
import warnings
import os
warnings.filterwarnings("ignore")
os.chdir('G:/python')
def swap_letters1(message):
    message = message.lower()
    letter_dict = {
        'a': 'b', 'b': 'd', 'c': 'f', 'd': 'h', 'e': 'j', 'f': 'l', 'g': 'n', 'h': 'p', 'i': 'r', 'j': 't', 'k': 'v', 'l': "x", 'm': 'z',
        'n': 'b1', 'o': "d1", 'p': 'f1', 'q': 'h1', 'r': 'j1', 's': 'l1', 't': 'n1', 'u': 'p1', 'v': 'r1', 'w': 't1', 'x': 'v1', 'y': 'x1', 'z': 'a',
        ' ': ' ', "?": "?", "!": "!",",":","
    }
    result = []
    for char in message:
        if char in letter_dict:
            result.append(letter_dict[char])
        else:
            result.append(char)  # Keep the character as is if it's not in the dictionary
    return ''.join(result)

def swap_letters2(message):
    message = message.lower()
    fan_letter_dict = {'b': 'a', 'd': 'b', 'f': 'c', 'h': 'd', 'j': 'e', 'l': 'f', 'n': 'g', 'p': 'h', 'r': 'i', 't': 'j', 'v': 'k', 'x': 'l', 'z': 'm', 'b1': 'n', 'd1': 'o', 'f1': 'p', 'h1': 'q', 'j1': 'r', 'l1': 's', 'n1': 't', 'p1': 'u', 'r1': 'v', 't1': 'w', 'v1': 'x', 'x1': 'y', 'a': 'z', ' ': ' ', '?': '?', '!': '!', ',': ','}
    result = []
    i = 0
    while i < len(message):
        if i + 1 < len(message) and message[i:i+2] in fan_letter_dict:
            result.append(fan_letter_dict[message[i:i+2]])
            i += 2
        else:
            result.append(fan_letter_dict.get(message[i], message[i]))  # Use get to avoid KeyError
            i += 1
    return ''.join(result)

# 询问加密还是解密
def get_task():
    task = simpledialog.askstring('窗口', '你要加密还是解密?')
    return task

# 获取回答
def get_message():
    message = simpledialog.askstring('消息', '输入消息')
    return message

def write_to_file(name, file_name):
    with open(file_name, 'a') as file:
        file.write('\n' + name)

# 运行Tkinter,打开Tk窗口
root = Tk()
# 隐藏Tk窗口
root.withdraw()

# 开始循环
while True:
    task = get_task()
    if task == '加密':
        message = get_message()
        encrypted = swap_letters1(message)
        messagebox.showinfo('消息的密文是:', encrypted)
        write_to_file(encrypted, '超密.txt')
    elif task == '解密':
        message = get_message()
        decrypted = swap_letters2(message)
        messagebox.showinfo('消息的明文是:', decrypted)
        write_to_file(decrypted, '正常.txt')
    else:
        break
