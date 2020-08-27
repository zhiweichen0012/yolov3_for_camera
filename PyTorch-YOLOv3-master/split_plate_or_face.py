import os
import shutil
from PIL import Image
#path='/media/sda4/tongan_project/PyTorch-YOLOv3-master/data/custom/allimg_guiyi'
#path1='/media/sda4/tongan_project/PyTorch-YOLOv3-master/data/custom/alllabels_guiyi'
path = "/home/tongan/face_images" #文件夹目录
path1="/home/tongan/face_labels" 
path2='/media/sda4/tongan_project/PyTorch-YOLOv3-master/data/custom3/images'
path3='/media/sda4/tongan_project/PyTorch-YOLOv3-master/data/custom3/labels'

files= os.listdir(path) #得到文件夹下的所有文件名称
txts1 = []
txts2=[]
num=0
for file in files: #遍历文件夹
    position = path+'/'+ file 
    position2 = path2+'/'+ file 
    shutil.copy(position,position2)
    position1 = path1+'/'+ file.split(".")[0]+".txt" 
    position3 = path3+'/'+ file.split(".")[0]+".txt"
    shutil.copy(position1,position3)
    print (position2)
    if (num < 5):
        txts1.append(position2)
        num+=1
    else:
        txts2.append(position2)
        num = 0
txts1 = '\n'.join(txts1)#转化为非数组类型
txts2 = '\n'.join(txts2)#转化为非数组类型
f1 = "/media/sda4/tongan_project/PyTorch-YOLOv3-master/data/custom3/train.txt"
with open(f1,"a") as file1:   #只需要将之前的”w"改为“a"即可，代表追加内容
    file1.write(txts1)
f2 = "/media/sda4/tongan_project/PyTorch-YOLOv3-master/data/custom3/valid.txt"
with open(f2,"a") as file2:   #只需要将之前的”w"改为“a"即可，代表追加内容
    file2.write(txts2)
