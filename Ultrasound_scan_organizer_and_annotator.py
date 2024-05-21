#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter.filedialog import askopenfile
from tkVideoPlayer import TkinterVideo
import tkinter
import tkinter as tk
import datetime
from tkinter import filedialog
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from subprocess import CREATE_NEW_CONSOLE
import subprocess
import cv2
import imutils
import numpy as np
import glob
import matplotlib.pyplot as plt
from skimage import draw
from natsort import natsorted

window = Tk()
window.title("GUI for Turtle Project")
window.geometry("550x550+10+10")

mode = True
drawing = False
start_t = [] 
end_t = []
input_path = []
filelist = []
L = []
turtle_ID = ''
Organ_Name = ''

def set_path():
    global input_path, L, turtle_ID, Organ_Name
    #global filelist
    #global types
        #global filelist
    input_path = tk.filedialog.askdirectory(initialdir = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop'),
                                                     title = "Select Directory Location")

    input_entry.delete(0, tk.END) # Remove current text in entry
    input_entry.insert(0, input_path) # Insert the 'path'
    path = os.path.normpath(input_path)
    x =    path.split(os.sep)
    turtle_ID = x[-2]
    Organ_Name = x[-1]
    turtle_id_entry.delete(0, tk.END) # Remove current text in entry
    turtle_id_entry.insert(0, turtle_ID + '-' + Organ_Name) # Insert the 'path'
#     types = ['/Timepoint*']
#     subtypes = ['/view*']
#     filelist = []
#     sublist = []
#     var = tk.StringVar()
#     #print(var)
#     var.set(str(os.path.split(input_path)[1]))
     #OrganName = tk.Label(frame01, text = 'x[-1]', font=("Arial", 20))
     #OrganName.pack(side=tk.LEFT)
#     for files in types:
#         filelist.extend(glob.glob(input_path + files))
#     lbox.delete(0, tk.END)
#     filelist = natsorted(filelist)
#     L = len(filelist)
#     for item in filelist:
#         global item2
#         item2 = os.path.split(item)[1]
#         print(item2)
#         lbox.insert(0, item2)
#         lbox.config(yscrollcommand = scrollbar.set, height = 5)

def show_files_TP1():
    types = ['/view*']
    filelist = []
    #sublist = []
    #var = tk.StringVar()
    #print(var)
    #var.set(str(os.path.split(input_path)[1]))
    #OrganName = tk.Label(frame01, textvariable = var , font=("Arial", 20))
    #OrganName.pack(side=tk.TOP)
    for files in types:
        filelist.extend(glob.glob(os.path.join(input_path, 'Timepoint1') + files))
        #print(filelist)
    lbox.delete(0, tk.END)
    filelist = natsorted(filelist)
    L = len(filelist)
    for item in filelist:
        global item2
        item2 = os.path.split(item)[1]
        #print(item2)
        lbox.insert(0, item2)
        lbox.config(yscrollcommand = scrollbar.set, height = 5)

    def showcontent(event):    
        global selected_ID1  
        x = lbox.curselection()[0]
        selected_ID1 = lbox.get(x)
    #lbox2.bind('<Double-1>', showcontent2)
    lbox.bind('<Double-1>', showcontent)
def show_files_TP2():
    types = ['/view*']
    filelist = []
    #sublist = []
    #var = tk.StringVar()
    #print(var)
    #var.set(str(os.path.split(input_path)[1]))
    #OrganName = tk.Label(frame01, textvariable = var , font=("Arial", 20))
    #OrganName.pack(side=tk.TOP)
    for files in types:
        filelist.extend(glob.glob(os.path.join(input_path, 'Timepoint2') + files))
        #print(filelist)
    lbox.delete(0, tk.END)
    filelist = natsorted(filelist)
    L = len(filelist)
    for item in filelist:
        global item2
        item2 = os.path.split(item)[1]
        #print(item2)
        lbox.insert(0, item2)
        lbox.config(yscrollcommand = scrollbar.set, height = 5)

    def showcontent(event):    
        global selected_ID2  
        x = lbox.curselection()[0]
        selected_ID2 = lbox.get(x)
    #lbox2.bind('<Double-1>', showcontent2)
    lbox.bind('<Double-1>', showcontent)

def show_files_TP3():
    types = ['/view*']
    filelist = []
    #sublist = []
    #var = tk.StringVar()
    #print(var)
    #var.set(str(os.path.split(input_path)[1]))
    #OrganName = tk.Label(frame01, textvariable = var , font=("Arial", 20))
    #OrganName.pack(side=tk.TOP)
    for files in types:
        filelist.extend(glob.glob(os.path.join(input_path, 'Timepoint3') + files))
        #print(filelist)
    lbox.delete(0, tk.END)
    filelist = natsorted(filelist)
    L = len(filelist)
    for item in filelist:
        global item2
        item2 = os.path.split(item)[1]
        #print(item2)
        lbox.insert(0, item2)
        lbox.config(yscrollcommand = scrollbar.set, height = 5)

    def showcontent(event):    
        global selected_ID3  
        x = lbox.curselection()[0]
        selected_ID3 = lbox.get(x)
    #lbox2.bind('<Double-1>', showcontent2)
    lbox.bind('<Double-1>', showcontent)

def show_files_TP4():
    types = ['/view*']
    filelist = []
    #sublist = []
    #var = tk.StringVar()
    #print(var)
    #var.set(str(os.path.split(input_path)[1]))
    #OrganName = tk.Label(frame01, textvariable = var , font=("Arial", 20))
    #OrganName.pack(side=tk.TOP)
    for files in types:
        filelist.extend(glob.glob(os.path.join(input_path, 'Timepoint4') + files))
        #print(filelist)
    lbox.delete(0, tk.END)
    filelist = natsorted(filelist)
    L = len(filelist)
    for item in filelist:
        global item2
        item2 = os.path.split(item)[1]
        #print(item2)
        lbox.insert(0, item2)
        lbox.config(yscrollcommand = scrollbar.set, height = 5)

    def showcontent(event):    
        global selected_ID4  
        x = lbox.curselection()[0]
        selected_ID4 = lbox.get(x)
    #lbox2.bind('<Double-1>', showcontent2)
    lbox.bind('<Double-1>', showcontent)

def show_files_TP5():
    types = ['/view*']
    filelist = []
    #sublist = []
    #var = tk.StringVar()
    #print(var)
    #var.set(str(os.path.split(input_path)[1]))
    #OrganName = tk.Label(frame01, textvariable = var , font=("Arial", 20))
    #OrganName.pack(side=tk.TOP)
    for files in types:
        filelist.extend(glob.glob(os.path.join(input_path, 'Timepoint5') + files))
        #print(filelist)
    lbox.delete(0, tk.END)
    filelist = natsorted(filelist)
    L = len(filelist)
    for item in filelist:
        global item2
        item2 = os.path.split(item)[1]
        #print(item2)
        lbox.insert(0, item2)
        lbox.config(yscrollcommand = scrollbar.set, height = 5)

    def showcontent(event):    
        global selected_ID5  
        x = lbox.curselection()[0]
        selected_ID5 = lbox.get(x)
    #lbox2.bind('<Double-1>', showcontent2)
    lbox.bind('<Double-1>', showcontent)

def show_files_TP6():
    types = ['/view*']
    filelist = []
    #sublist = []
    #var = tk.StringVar()
    #print(var)
    #var.set(str(os.path.split(input_path)[1]))
    #OrganName = tk.Label(frame01, textvariable = var , font=("Arial", 20))
    #OrganName.pack(side=tk.TOP)
    for files in types:
        filelist.extend(glob.glob(os.path.join(input_path, 'Timepoint6') + files))
        #print(filelist)
    lbox.delete(0, tk.END)
    filelist = natsorted(filelist)
    L = len(filelist)
    for item in filelist:
        global item2
        item2 = os.path.split(item)[1]
        #print(item2)
        lbox.insert(0, item2)
        lbox.config(yscrollcommand = scrollbar.set, height = 5)

    def showcontent(event):    
        global selected_ID6  
        x = lbox.curselection()[0]
        selected_ID6 = lbox.get(x)
    #lbox2.bind('<Double-1>', showcontent2)
    lbox.bind('<Double-1>', showcontent)
def update_duration(event):
    """ updates the duration after finding the duration """
    duration = videoplayer.video_info()["duration"]
    #print(videoplayer.video_info()["duration"])
    end_time["text"] = str(datetime.timedelta(seconds=duration)).split('.', 2)[0]
    progress_slider["to"] = duration

def update_scale(event):
    """ updates the scale value """
    progress_value.set(videoplayer.current_duration())


# def open_file():
    
#     file = askopenfile(mode='r', filetypes=[
#                        ('Video Files', ["*.mp4"])])
#     if file is not None:
#         global filename
#         filename = file.name
#         global videoplayer
#         videoplayer = TkinterVideo(master=window, scaled=True)
        
#         videoplayer.load(r"{}".format(filename))
        
#         progress_slider.config(to=0, from_=0)
#         videoplayer.pack(side = BOTTOM, expand=True, fill="both")
        
#         #progress_value.set(0)
#         #videoplayer.play()    
      
def load_video():
    """ loads the video """
    global file_path
    global file_name
    #file_path = filedialog.askopenfilename(initialdir = input_path) #os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop'))
    file_path = os.path.join(input_path, selected_ID)
    file_name = os.path.split(file_path)[1]
    #print(file_name)
    if file_path:
        
        
        global videoplayer
        videoplayer.load(file_path)
        
        progress_slider.config(to=0, from_=0)
        #play_pause_btn["text"] = "Play"
        progress_value.set(0)
        
play_icon  = PhotoImage(file='play.png')
pause_icon = PhotoImage(file='pause.png')
stop_icon  = PhotoImage(file='stop.png')

frame0  = tk.Frame(window)
frame01 = tk.Frame(window)
frame02 = tk.Frame(window)
frame1  = tk.Frame(window)
frame2  = tk.Frame(window)


def seek(value):
    
    videoplayer.seek(int(value))


def skip(value: int):
    """ skip seconds """
    videoplayer.seek(int(progress_slider.get())+value)
    progress_value.set(progress_slider.get() + value)    
    
def best_TP1():
    global file_path
    file_path = os.path.join(os.path.join(input_path, 'Timepoint1'), selected_ID1)
    
def best_TP2():
    global file_path
    file_path = os.path.join(os.path.join(input_path, 'Timepoint2'), selected_ID2)

def best_TP3():
    global file_path
    file_path = os.path.join(os.path.join(input_path, 'Timepoint3'), selected_ID3)

def best_TP4():
    global file_path
    file_path = os.path.join(os.path.join(input_path, 'Timepoint4'), selected_ID4)

def best_TP5():
    global file_path
    file_path = os.path.join(os.path.join(input_path, 'Timepoint5'), selected_ID5)

def best_TP6():
    global file_path
    file_path = os.path.join(os.path.join(input_path, 'Timepoint6'), selected_ID5)
    
def playAgain():
    global file_path
    global file_name
    #file_path = os.path.join(os.path.join(input_path, 'Timepoint1'), selected_ID1)
    file_name = os.path.split(file_path)[1]
    #print(file_name)
    if file_path:
        global videoplayer
        videoplayer.load(file_path)
        progress_slider.config(to=0, from_=0)
        #play_pause_btn["text"] = "Play"
        progress_value.set(0)
    videoplayer.play()
    
def StopVideo():
    #print(filename)
    videoplayer.stop()
def PauseVideo():
    #print(filename)
    videoplayer.pause()

def video_ended(event):
    
    progress_slider.set(progress_slider["to"])
    progress_slider.set(0)    

def my_upd_start():
    global start_t
    
    start_t = progress_slider.get()
    start_entry.delete(0, tk.END) # Remove current text in entry
    start_entry.insert(0, start_t) # Insert the 'path'
def my_upd_end():
    global end_t
    
    end_t = progress_slider.get()
    end_entry.delete(0, tk.END) # Remove current text in entry
    end_entry.insert(0, end_t) # Insert the 'path'
def view_selected():
    videoplayer.stop()
    #new_win = Tk()
    #new_win.geometry("400x400")
    #videoplayer = TkinterVideo(scaled=True, master=new_win)
    videoplayer.pack(expand=True, fill="both")
    print(start_t)
    ffmpeg_extract_subclip(file_path, start_t, end_t, targetname=os.path.join(os.path.split(file_path)[0], 'Trimmed_' + file_name)) # + file_name)
    #print(file_path)
    
    videoplayer.load(os.path.join(os.path.split(file_path)[0], 'Trimmed_' + file_name))
    videoplayer.play()
    
    #new_win.mainloop()
def crop_video():

    ffmpeg_extract_subclip(file_path, start_t, end_t, targetname="cropped_video.avi")
    
def roi_extractor():
    
    global dot_x, dot_y
    #drawing=False # true if mouse is pressed
    #mode=True     # if True, draw rectangle. Press 'm' to toggle to curve
    dot_x = []    # collecing the point where mouse is moving along x-axis
    dot_y = []    # collecing the point where mouse is moving along y-axis

    # mouse callback function
    def freehand_draw(event,former_x,former_y,flags,param):

        global current_former_x,current_former_y,drawing, mode

        if event==cv2.EVENT_LBUTTONDOWN: # start to collect the (x, y) point as soon as mouse clicks down
            drawing=True
            current_former_x,current_former_y=former_x,former_y
        elif event==cv2.EVENT_MOUSEMOVE: # main loop on grabbing all the (x, y) points while mouse is clicked
            if drawing==True:
                if mode==True:
                    cv2.line(im,(current_former_x,current_former_y),(former_x,former_y),(0,255,0),2)
                    current_former_x = former_x
                    current_former_y = former_y
                    dot_x.append(former_x) # appending all points together along x-axis
                    dot_y.append(former_y) # appending all points together along y-axis
                    #print former_x,former_y 
        elif event==cv2.EVENT_LBUTTONUP: # the last location of mouse before stop moving
            drawing=False
            if mode==True:
                cv2.line(im,(current_former_x,current_former_y),(former_x,former_y),(0,255,0),2)
                current_former_x = former_x
                current_former_y = former_y
        return former_x,former_y    

    cap = cv2.VideoCapture(os.path.join(os.path.split(file_path)[0], 'Trimmed_' + file_name)) # test video
    ret, im = cap.read()
    cv2.namedWindow("FreeHand")
    cv2.setMouseCallback('FreeHand',freehand_draw)
    while(1):
        cv2.imshow('FreeHand',im)
        if cv2.waitKey(1) & 0xFF == ord('q'): # by pressing 'q' the window will be shut down! All you need is on dot_x and dot_y!
            break
    cv2.destroyAllWindows()

def apply_mask():

    cap = cv2.VideoCapture(os.path.join(os.path.split(file_path)[0], 'Trimmed_' + file_name))
    width  = max(dot_x) - min(dot_x) #int(cap.get(3))  # float `width`
    height = max(dot_y) - min(dot_y) #int(cap.get(4))  # float `height`
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    output = cv2.VideoWriter(os.path.join(os.path.split(file_path)[0],'Output_'+turtle_ID+'_'+Organ_Name+'_'+os.path.split(os.path.split(file_path)[0])[1]+'_'+file_name), 
                             fourcc, fps, frameSize=(width, height))
    mask = cv2.VideoWriter(os.path.join(os.path.split(file_path)[0],'Mask_'+turtle_ID+'_'+Organ_Name+'_'+os.path.split(os.path.split(file_path)[0])[1]+'_'+file_name), 
                             fourcc, fps, frameSize=(width, height))
    img = np.zeros([int(cap.get(4)),int(cap.get(3)),3],dtype=np.uint8)
    print(img.shape)
    img.fill(255) # or img[:] = 255
    x_offset = []
    y_offset = []
    np.random.seed(1)
    x = dot_x
    y = dot_y
    shape = tuple(                    # tuple is required to have a fixed ROI size
            int(np.ceil(np.ptp(arr))) # np.ptp() or 'peak-to-peack' finds the range of your 
            for arr in [y, x]         # data along x- and y-axis (range = maximum - minimum)
            )
    x_offset = x
    y_offset = y
    image = draw.polygon2mask(       # mask generator according to the collected points above, i.e., dot_x and dot_y
            (int(cap.get(4)), int(cap.get(3))),         # im.shape[0] and im.shape[1] are required to have the size of frames while making mask
            np.stack((y_offset, x_offset), axis=1)
            )
    
    while True:                     # applying the mask loop per-frame
        ret, im = cap.read()  
        if ret == True:             # ret checks if there is frame on-going
            im[np.where((image == False))] = [0, 0, 0]
            img[np.where((image == False))] = [0, 0, 0]
            output.write(im[min(y):max(y),min(x):max(x)])
            mask.write(img[min(y):max(y),min(x):max(x)])
            cv2.imshow('mask', im[min(y):max(y),min(x):max(x)])
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else: 
            break
    cap.release()
    output.release()
    cv2.destroyAllWindows()
    #p = subprocess.Popen('python video_crop.py')
    #p.wait()
    #videoplayer.load(r"C:\Users\azarang\Desktop\Postdoc\Katherine\Turtles_dataset\Turtle_ID1\Heart\trimmed_video_cropped.avi")
    #videoplayer.play()

    
def show_final():
    videoplayer.load(os.path.join(os.path.split(file_path)[0], 'Output_'+turtle_ID+'_'+Organ_Name+'_'+os.path.split(os.path.split(file_path)[0])[1]+'_'+file_name))
    videoplayer.play()

    
def play_all():
#     names = [os.path.join(os.path.split(file_path)[0], 'Output_view1.avi'), 
#              os.path.join(os.path.split(file_path)[0], 'Output_view2.wmv'), 
#              os.path.join(os.path.split(file_path)[0], 'Output_view3.avi')]
    xx = []
    types = ['/*']
    for files in types:
        xx.extend(glob.glob(input_path + files))
    L_tp = len(xx)
    #print(L_tp)
    if L_tp == 1:        
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), selected_ID1)]
        window_titles = ['TP1: ' + selected_ID1]
        cv2.namedWindow(window_titles[0])

        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cap = [cv2.VideoCapture(i) for i in names]

    elif L_tp == 2:        
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), selected_ID1),
                 os.path.join(os.path.join(input_path, 'Timepoint2'), selected_ID2)]
        window_titles = ['TP1: ' + selected_ID1, 'TP2: ' + selected_ID2]
        cv2.namedWindow(window_titles[0])
        cv2.namedWindow(window_titles[1])

        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cv2.moveWindow(window_titles[1], 250,600)
        cap = [cv2.VideoCapture(i) for i in names]

    elif L_tp == 3:        
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), selected_ID1),
                 os.path.join(os.path.join(input_path, 'Timepoint2'), selected_ID2),
                 os.path.join(os.path.join(input_path, 'Timepoint3'), selected_ID3)]
        window_titles = ['TP1: ' + selected_ID1, 'TP2: ' + selected_ID2, 'TP3: ' + selected_ID3]
        cv2.namedWindow(window_titles[0])
        cv2.namedWindow(window_titles[1])
        cv2.namedWindow(window_titles[2])

        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cv2.moveWindow(window_titles[1], 250,600)
        cv2.moveWindow(window_titles[2], 600,600)
        cap = [cv2.VideoCapture(i) for i in names]
    elif L_tp == 4: 
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), selected_ID1),
                 os.path.join(os.path.join(input_path, 'Timepoint2'), selected_ID2),
                 os.path.join(os.path.join(input_path, 'Timepoint3'), selected_ID3),
                 os.path.join(os.path.join(input_path, 'Timepoint4'), selected_ID4)]
                 
        window_titles = ['TP1: ' + selected_ID1, 'TP2: ' + selected_ID2, 'TP3: ' + selected_ID3, 'TP4: ' + selected_ID4]
        cv2.namedWindow(window_titles[0])
        cv2.namedWindow(window_titles[1])
        cv2.namedWindow(window_titles[2])
        cv2.namedWindow(window_titles[3])
                
        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cv2.moveWindow(window_titles[1], 250,600)
        cv2.moveWindow(window_titles[2], 500,600)
        cv2.moveWindow(window_titles[3], 750,600)
        cap = [cv2.VideoCapture(i) for i in names]        

    
    elif L_tp == 5: 
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), selected_ID1),
                 os.path.join(os.path.join(input_path, 'Timepoint2'), selected_ID2),
                 os.path.join(os.path.join(input_path, 'Timepoint3'), selected_ID3),
                 os.path.join(os.path.join(input_path, 'Timepoint4'), selected_ID4),
                 os.path.join(os.path.join(input_path, 'Timepoint5'), selected_ID5)]
        window_titles = ['TP1: ' + selected_ID1, 'TP2: ' + selected_ID2, 'TP3: ' + selected_ID3, 'TP4: ' + selected_ID4,
                         'TP5: ' + selected_ID5,]
        cv2.namedWindow(window_titles[0])
        cv2.namedWindow(window_titles[1])
        cv2.namedWindow(window_titles[2])
        cv2.namedWindow(window_titles[3])
        cv2.namedWindow(window_titles[4])        
        
        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cv2.moveWindow(window_titles[1], 250,600)
        cv2.moveWindow(window_titles[2], 500,600)
        cv2.moveWindow(window_titles[3], 750,600)
        cv2.moveWindow(window_titles[4], 1000,600)
        cap = [cv2.VideoCapture(i) for i in names]        
    else: 
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), selected_ID1),
                 os.path.join(os.path.join(input_path, 'Timepoint2'), selected_ID2),
                 os.path.join(os.path.join(input_path, 'Timepoint3'), selected_ID3),
                 os.path.join(os.path.join(input_path, 'Timepoint4'), selected_ID4),
                 os.path.join(os.path.join(input_path, 'Timepoint5'), selected_ID5),
                 os.path.join(os.path.join(input_path, 'Timepoint6'), selected_ID5)]
        window_titles = ['TP1: ' + selected_ID1, 'TP2: ' + selected_ID2, 'TP3: ' + selected_ID3, 'TP4: ' + selected_ID4,
                         'TP5: ' + selected_ID5, 'TP6: ' + selected_ID6]
        cv2.namedWindow(window_titles[0])
        cv2.namedWindow(window_titles[1])
        cv2.namedWindow(window_titles[2])
        cv2.namedWindow(window_titles[3])
        cv2.namedWindow(window_titles[4])
        cv2.namedWindow(window_titles[5]) 
        
        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cv2.moveWindow(window_titles[1], 250,600)
        cv2.moveWindow(window_titles[2], 500,600)
        cv2.moveWindow(window_titles[3], 750,600)
        cv2.moveWindow(window_titles[4], 1000,600)
        cv2.moveWindow(window_titles[5], 1250,600)
        cap = [cv2.VideoCapture(i) for i in names]        

    frames = [None] * len(names)
    gray = [None] * len(names)
    ret = [None] * len(names)
    #length = int(cap[1].get(cv2.CAP_PROP_FRAME_COUNT))
    frame_counts = []
    frame_fps = []
    for i in range(len(names)):
        frame_fps.append(int(cap[i].get(cv2.CAP_PROP_FRAME_COUNT)))
        frame_counts.append(int(cap[i].get(cv2.CAP_PROP_FPS)))
    max_index = np.argmax(frame_counts)
    global fps_min
    fps_min = np.min(frame_fps)
    #ii = 0
    while True:
    #while cap[max_index].isOpened():
        for i, c in enumerate(cap):
            if c is not None:
                ret[i], frames[i] = c.read()
        for i, f in enumerate(frames):
            if ret[i] is True:
                #f = imutils.resize(f, width=320, height =240)
                f = cv2.resize(f, (240, 200))
                gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
                cv2.imshow(window_titles[i], gray[i])
            else: 
                break
        if cv2.waitKey(int(fps_min/3)) & 0xFF == ord('q'):
            break

    for c in cap:
        if c is not None:
            c.release()

    cv2.destroyAllWindows()
def play_all2():
#     names = [os.path.join(os.path.split(file_path)[0], 'Output_view1.avi'), 
#              os.path.join(os.path.split(file_path)[0], 'Output_view2.wmv'), 
#              os.path.join(os.path.split(file_path)[0], 'Output_view3.avi')]
    xx = []
    types = ['/*']
    for files in types:
        xx.extend(glob.glob(input_path + files))
    L_tp = len(xx)
    if L_tp == 1:        
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), 
                              os.path.join(os.path.split(file_path)[0],'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint1'+'_'+ selected_ID1))]
        window_titles = ['Best ROI TP1']
        cv2.namedWindow(window_titles[0])

        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cap = [cv2.VideoCapture(i) for i in names]

    elif L_tp == 2:        
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint1'+'_'+ selected_ID1),
                 os.path.join(os.path.join(input_path, 'Timepoint2'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint2'+'_'+ selected_ID2)]
        window_titles = ['Best ROI TP1', 'Best ROI TP2']
        cv2.namedWindow(window_titles[0])
        cv2.namedWindow(window_titles[1])

        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cv2.moveWindow(window_titles[1], 250,600)
        cap = [cv2.VideoCapture(i) for i in names]

    elif L_tp == 3:        
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint1'+'_'+ selected_ID1),
                 os.path.join(os.path.join(input_path, 'Timepoint2'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint2'+'_'+ selected_ID2),
                 os.path.join(os.path.join(input_path, 'Timepoint3'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint3'+'_'+ selected_ID3)]
        window_titles = ['Best ROI TP1', 'Best ROI TP2' , 'Best ROI TP3']
        cv2.namedWindow(window_titles[0])
        cv2.namedWindow(window_titles[1])
        cv2.namedWindow(window_titles[2])

        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cv2.moveWindow(window_titles[1], 250,600)
        cv2.moveWindow(window_titles[2], 500,600)
        cap = [cv2.VideoCapture(i) for i in names]
    elif L_tp == 4:
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint1'+'_'+ selected_ID1),
                 os.path.join(os.path.join(input_path, 'Timepoint2'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint2'+'_'+ selected_ID2),
                 os.path.join(os.path.join(input_path, 'Timepoint3'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint3'+'_'+ selected_ID3), 
                 os.path.join(os.path.join(input_path, 'Timepoint4'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint4'+'_'+ selected_ID4)]
        window_titles = ['Best ROI TP1', 'Best ROI TP2' , 'Best ROI TP3', 'Best ROI TP4']
        cv2.namedWindow(window_titles[0])
        cv2.namedWindow(window_titles[1])
        cv2.namedWindow(window_titles[2])
        cv2.namedWindow(window_titles[3])
        

        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cv2.moveWindow(window_titles[1], 250,600)
        cv2.moveWindow(window_titles[2], 500,600)
        cv2.moveWindow(window_titles[3], 750,600)
        cap = [cv2.VideoCapture(i) for i in names]

    elif L_tp == 5:
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint1'+'_'+ selected_ID1),
                 os.path.join(os.path.join(input_path, 'Timepoint2'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint2'+'_'+ selected_ID2),
                 os.path.join(os.path.join(input_path, 'Timepoint3'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint3'+'_'+ selected_ID3), 
                 os.path.join(os.path.join(input_path, 'Timepoint4'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint4'+'_'+ selected_ID4), 
                 os.path.join(os.path.join(input_path, 'Timepoint5'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint5'+'_'+ selected_ID5)]
        window_titles = ['Best ROI TP1', 'Best ROI TP2' , 'Best ROI TP3', 'Best ROI TP4', 'Best ROI TP5']
        cv2.namedWindow(window_titles[0])
        cv2.namedWindow(window_titles[1])
        cv2.namedWindow(window_titles[2])
        cv2.namedWindow(window_titles[3])
        cv2.namedWindow(window_titles[4])

        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cv2.moveWindow(window_titles[1], 250,600)
        cv2.moveWindow(window_titles[2], 500,600)
        cv2.moveWindow(window_titles[3], 750,600)
        cv2.moveWindow(window_titles[4], 1000,600)
        cap = [cv2.VideoCapture(i) for i in names]
    else:
        names = [os.path.join(os.path.join(input_path, 'Timepoint1'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint1'+'_'+ selected_ID1),
                 os.path.join(os.path.join(input_path, 'Timepoint2'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint2'+'_'+ selected_ID2),
                 os.path.join(os.path.join(input_path, 'Timepoint3'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint3'+'_'+ selected_ID3), 
                 os.path.join(os.path.join(input_path, 'Timepoint4'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint4'+'_'+ selected_ID4), 
                 os.path.join(os.path.join(input_path, 'Timepoint5'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint5'+'_'+ selected_ID5),
                 os.path.join(os.path.join(input_path, 'Timepoint6'), 'Output_'+turtle_ID+'_'+Organ_Name+'_'+'Timepoint6'+'_'+ selected_ID6)]
        window_titles = ['Best ROI TP1', 'Best ROI TP2' , 'Best ROI TP3', 'Best ROI TP4', 'Best ROI TP5', 'Best ROI TP6']
        cv2.namedWindow(window_titles[0])
        cv2.namedWindow(window_titles[1])
        cv2.namedWindow(window_titles[2])
        cv2.namedWindow(window_titles[3])
        cv2.namedWindow(window_titles[4])
        cv2.namedWindow(window_titles[5])
        
        cv2.moveWindow(window_titles[0], 0, 600)  # Move it to (40,30)
        cv2.moveWindow(window_titles[1], 250,600)
        cv2.moveWindow(window_titles[2], 500,600)
        cv2.moveWindow(window_titles[3], 750,600)
        cv2.moveWindow(window_titles[4], 1000,600)
        cv2.moveWindow(window_titles[4], 1250,600)
        cap = [cv2.VideoCapture(i) for i in names]

    frames = [None] * len(names)
    gray = [None] * len(names)
    ret = [None] * len(names)
    
    while True:

        for i, c in enumerate(cap):
            if c is not None:
                ret[i], frames[i] = c.read();

        
        for i, f in enumerate(frames):
            if ret[i] is True:
                #f = imutils.resize(f, width=320, height =240)
                f = cv2.resize(f, (240, 200))
                gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
                cv2.imshow(window_titles[i], gray[i]);
            else: 
                break
        if cv2.waitKey(int(fps_min/2)) & 0xFF == ord('q'):
            break


    for c in cap:
        if c is not None:
            c.release()

    cv2.destroyAllWindows()

setpath = Button(frame0, text='Set Path', command= lambda: set_path())    #lambda: open_file())
setpath.pack(side=tk.LEFT, pady=2)

TP1_btn = Button(frame0, text='TP1', command = lambda: show_files_TP1())    #lambda: open_file())
TP2_btn = Button(frame0, text='TP2', command = lambda: show_files_TP2())    #lambda: open_file())
TP3_btn = Button(frame0, text='TP3', command = lambda: show_files_TP3())    #lambda: open_file())
TP4_btn = Button(frame0, text='TP4', command = lambda: show_files_TP4())    #lambda: open_file())
TP5_btn = Button(frame0, text='TP5', command = lambda: show_files_TP5())    #lambda: open_file(
TP6_btn = Button(frame0, text='TP6', command = lambda: show_files_TP6())    #lambda: open_file(


input_entry = tk.Entry(frame0, text = "", width = 25)
input_entry.insert(0, input_path)
input_entry.pack(side = tk.LEFT, pady = 5, padx = 5)

TP1_btn.pack(side = tk.LEFT)
TP2_btn.pack(side = tk.LEFT)
TP3_btn.pack(side = tk.LEFT)
TP4_btn.pack(side = tk.LEFT)
TP5_btn.pack(side = tk.LEFT)
TP6_btn.pack(side = tk.LEFT)


lbox = tk.Listbox(frame0, height = 6, width = 10)
lbox.pack(side = tk.LEFT, padx = 10, pady = 5)
lbox.config(height = 0)
scrollbar = Scrollbar(frame0, orient = 'vertical', command = lbox.yview)
scrollbar.pack(side = tk.LEFT, fill = 'y')    


playAll = Button(frame0, text = 'Play',  width = 6, height = 1, command=lambda: play_all())
playAll.pack(side=LEFT, padx=2)

# setpath = Button(frame0, text='Set Path', command= lambda: set_path())    #lambda: open_file())
# setpath.pack(side=tk.LEFT, pady=2)
start_time = tk.Label(frame01, text='Turtle ID - Organ:')
start_time.pack(side=tk.LEFT)

turtle_id_entry = tk.Entry(frame01, text = "", width = 16)
turtle_id_entry.insert(0, turtle_ID + Organ_Name) 
turtle_id_entry.pack(side = tk.LEFT, padx = 10)

Best_TP1_Slct = Button(frame01, text = 'Best TP1',  width = 6, height = 1, command = lambda: best_TP1())
Best_TP1_Slct.pack(side=LEFT, padx=1, pady = 2)

Best_TP2_Slct = Button(frame01, text = 'Best TP2',  width = 6, height = 1, command = lambda: best_TP2())
Best_TP2_Slct.pack(side=LEFT, padx=1, pady = 2)

Best_TP3_Slct = Button(frame01, text = 'Best TP3',  width = 6, height = 1, command = lambda: best_TP3())
Best_TP3_Slct.pack(side=LEFT, padx=1, pady = 2)

Best_TP4_Slct = Button(frame01, text = 'Best TP4',  width = 6, height = 1, command = lambda: best_TP4())
Best_TP4_Slct.pack(side=LEFT, padx=1, pady = 2)

Best_TP5_Slct = Button(frame01, text = 'Best TP5',  width = 6, height = 1, command = lambda: best_TP5())
Best_TP5_Slct.pack(side=LEFT, padx=1, pady = 2)

Best_TP6_Slct = Button(frame01, text = 'Best TP6',  width = 6, height = 1, command = lambda: best_TP6())
Best_TP6_Slct.pack(side=LEFT, padx=1, pady = 2)

#openbtn = Button(frame2, text='Open', command= lambda: load_video())    #lambda: open_file())
#openbtn.pack(side=LEFT, pady=2)
videoplayer = TkinterVideo(scaled=True, master=window)

        
playbtn = Button(frame2, image = play_icon, width = 15, height = 15, command=lambda: playAgain())
playbtn.pack(side=LEFT, padx=2)

pausebtn = Button(frame2, image=pause_icon,  width = 15, height = 15, command=lambda: PauseVideo())
pausebtn.pack(side=LEFT, padx=2)

stopbtn = Button(frame2, image = stop_icon,  width = 15, height = 15, command=lambda: StopVideo())
stopbtn.pack(side=LEFT, padx=2)

set1 = Button(frame2, text = 'Set start', width = 6, height = 1, command=lambda: my_upd_start())
set1.pack(side=LEFT, padx=2)

set2 = Button(frame2, text = 'Set end', width = 6, height = 1, command=lambda: my_upd_end())
set2.pack(side=LEFT, padx=2)

play_selected = Button(frame2, text = 'View',  width = 3, height = 1, command=lambda: view_selected())
play_selected.pack(side=LEFT, padx=2)

cropbtn = Button(frame2, text = 'Crop',  width = 4, height = 1, command=lambda: roi_extractor())
cropbtn.pack(side=LEFT, padx=2)

applymask = Button(frame2, text = 'Mask',  width = 4, height = 1, command=lambda: apply_mask())
applymask.pack(side=LEFT, padx=2)

showFinal = Button(frame2, text = 'Final',  width = 4, height = 1, command=lambda: show_final())
showFinal.pack(side=LEFT, padx=2)

playAll = Button(frame2, text = 'Play all',  width = 6, height = 1, command=lambda: play_all2())
playAll.pack(side=LEFT, padx=2)

quit = Button(frame2, text = 'Quit',  width = 4, height = 1, command= window.destroy)
quit.pack(side=LEFT, padx=2)

skip_plus_5sec = tk.Button(frame1, text="Skip -5 s", width = 7, height = 1, command=lambda: skip(-5))
skip_plus_5sec.pack(side="left")

start_time = tk.Label(frame1, text=str(datetime.timedelta(seconds=0)))
start_time.pack(side="left")

progress_value = tk.IntVar(frame1)

progress_slider = tk.Scale(frame1, variable=progress_value, sliderlength=7, from_=0, to=0, orient="horizontal", command=seek)
#progress_slider.bind("<ButtonRelease-1>", seek)
progress_slider.pack(side="left", fill="x", expand=True)

end_time = tk.Label(frame1, text=str(datetime.timedelta(seconds=0)).split('.', 2)[0])
end_time.pack(side="left")

videoplayer.bind("<<Duration>>", update_duration)
videoplayer.bind("<<SecondChanged>>", update_scale)
videoplayer.bind("<<Ended>>", video_ended)

skip_plus_5sec = tk.Button(frame1, text="Skip +5 s", width = 7, height = 1, command=lambda: skip(5))
skip_plus_5sec.pack(side="left")

start_entry = tk.Entry(frame1, text = "", width = 3)
start_entry.insert(0, start_t)

end_entry = tk.Entry(frame1, text = "", width = 3)
end_entry.insert(0, end_t)

end_entry.pack(side = tk.RIGHT, pady = 5, padx = 5)
start_entry.pack(side = tk.RIGHT, pady = 5, padx = 5)

frame0.pack(side = TOP)
frame01.pack(side = TOP)
videoplayer.pack(expand=True, fill="both", padx = 20)
frame1.pack(side = TOP)
frame2.pack(side = TOP)        
window.mainloop()

