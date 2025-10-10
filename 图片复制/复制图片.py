
file_path = "/Users/grubby/Downloads/"

with open(file_path+"SCR-20250329-rjij.png", "rb") as file:
    img = file.read()

with open(r"/Users/grubby/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/langChain/python_learn/python_learn/图片复制/copy.jpg", "wb") as file:
    file.write(img)