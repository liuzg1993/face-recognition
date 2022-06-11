# 人脸识别
import cv2
from tkinter import * 
import tkinter.filedialog as tf
from PIL import Image, ImageTk
 
# 图片中人脸识别
def Face_Detect_Pic(image):
    # 1、转灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.imshow("gray", gray)
 
    # 2、训练一组人脸
    face_detector = cv2.CascadeClassifier("C:/Cpp/haarcascade_frontalface_default.xml")
 
    # 3、检测人脸（用灰度图检测，返回人脸矩形坐标(4个角)）
    faces_rect = face_detector.detectMultiScale(gray, 1.05, 10)
    #灰度图  图像尺寸缩小比例  至少检测次数（若为3，表示一个目标至少检测到k次才是真正目标）
    print("人脸矩形坐标faces_rect：", faces_rect)
 
    # 4、遍历每个人脸，画出矩形框
    img = image
    dst = img.copy()
    for x, y, w, h in faces_rect:
        cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 0, 255), 3)  #画出矩形框
 
    # 显示
    cv2.imshow("dst", dst)

def open_image():
    # 图片路径不要带有中文
    file_dir = tf.askopenfilename() 
    img = cv2.imread(file_dir)
    # img = cv2.imread("C:/Cpp/DL.jpg")

    cv2.imshow("img", img)
    Face_Detect_Pic(img)           #人脸识别（图片）
    cv2.waitKey(0)

if __name__ == "__main__":
    win = Tk() 
    win.title('请选择图片') 

    #选择界面
    ima_label = Label(win, width = 100, height = 20) 
    ima_label.pack(side = TOP)
    menubar = Menu(win) 
    filemenu = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label = '文件', menu = filemenu) 
    filemenu.add_command(label = '打开', command = open_image)
    aboutmenu = Menu(menubar, tearoff = 0)
    
    win.config(menu = menubar)

    win.mainloop()