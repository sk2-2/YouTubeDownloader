from tkinter import *
from pytube import YouTube
import time

root=Tk()

root.title("YouTube Downloader")
root.geometry("500x500")


def download():
    pass
    global e1
    string=e1.get()
    
    yt = YouTube(str(string))
    videos = yt.streams.filter(subtype='mp4').all()

    l=[]
    for v in videos:
        l.append(str(v))
    #print(l)
    s=0
    
    for i in l:
        print(str(s)+"."+str(l[s][41:52]))
        s=s+1
        
        
    
    

    n = int(input("Select Resolution of the video: "))
    vid = videos[n]

    destination = str(input("Enter the destination: "))
    vid.download(destination)

    for i in range(20):
        time.sleep(0.1)
        print("#" ,end = ' ')

    print(" successfully downloaded")
    
f1=Frame(root)
f1.pack(side=TOP)
l=Label(f1,text="Paste the url below")
l.pack()

f2=Frame(root)
f2.pack()

e1=Entry(f2,bd=3)
e1.pack(side=TOP)

b1=Button(f2,text="Download",command=download)
b1.pack()



root.mainloop()
