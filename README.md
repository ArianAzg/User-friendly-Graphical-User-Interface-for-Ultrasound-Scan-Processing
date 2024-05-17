# User-friendly-Graphical-User-Interface-for-Echocardiography-Processing


<p align="center">
  <img width="600" height="600" src="https://user-images.githubusercontent.com/48659018/183148498-c4812dae-6494-4c20-93e5-46c4c44e8d85.jpg">
</p>


Requirements
------------

The Python code is written in Python 3.9. All the required Python packages can be installed using the following command:
    
    $ pip install -r requirements.txt


How to run
----------

The current graphical user interface (GUI) presents a user-friendly interactive module for processing ultrasound videos (echocardiography). In general, the GUI has two major component: 
- ### Setting up the directory
- ### Video-processing toolbox

The first step is to select the input directory by clicking on **"Set Path"** button on GUI. From the opened window, the user must select the organ folder of a specific turtle. The **Turtle-ID** along with the **Organ Name** will be shown in a small entry box below the **"Set Path"** button. For this project, each folder consists of several timepoints and within each timepoint, there are a number of views avaibale for a given organ (Heart, Kidney, and Liver). To be more specific, a sample structure of dataset is summarized below (for only one turtle ID):
```
├── Main folder
|   ├── Turtle ID_1
|   |   ├── Heart
|   |   |   ├── Timepoint 1
|   |   |   |   ├── Scan 1
|   |   |   |   ├── Scan 2
|   |   |   |   ├── Scan 3
|   |   |   ├── Timepoint 2
|   |   |   |   ├── Scan 1
|   |   |   |   ├── Scan 2
|   |   ├── Liver
|   |   |   ├── Timepoint 1
|   |   |   |   ├── Scan 1
|   |   |   |   ├── Scan 2
|   |   |   |   ├── Scan 3
|   |   |   ├── Timepoint 2
|   |   |   |   ├── Scan 1
|   |   |   |   ├── Scan 2
|   |   |   ├── Timepoint 3
|   |   |   |   ├── Scan 1
|   |   |   |   ├── Scan 2
|   |   |   |   ├── Scan 3
|   |   ├── Kidney
|   |   |   ├── Timepoint 1
|   |   |   |   ├── Scan 1
|   |   |   |   ├── Scan 2
|   |   |   |   ├── Scan 3
|   |   |   ├── Timepoint 2
|   |   |   |   ├── Scan 1
|   |   |   |   ├── Scan 2
```

Plesae not that number of timepoints per organ is not consistent throughout the dataset (ranging between 3 to 5). First, the user must select a desired organ folder to work with through setting up the path. Next, the user has three timepoints available for each organ, denoted as **"TP1"**, **"TP2"**, and **"TP3"** buttons. For example, by clicking on **"TP1"**, all the available videos within the folder will be shown on the listbox. At this point, the user must select one of the available videos by double-clicking on the file name (in the listbox). The same steps must be repearted for **"TP2"** and **"TP3"**. 

#### Please note that in case 5 timepoints available in organ directory, the steps must be taken from **"TP1"** through **"TP5"**.

### NOTE: All three "TP1", "TP2", and "TP3" must be processed and one video in each must be selected. Then, the user can click on "Play" button on the top right corner. All the selected videos will be shown at the same time. To quit the opened videos, the user must select "q" on the keyboard. This step must be repeated to the point that user's decision is finalized and don't want to make any more changes to the selected vidoes. 

Next step is involving the video processing units for each selected video. The user must select **"Best TP1"**, **"Best TP2"**, and **"Best TP3"** only once throughout the entire video processing module. What it means is that once, for example, **"Best TP1"**, gets selected, the user must go through all the buttons from **"Play"** to **"Final"** in the last row before clicking on **"Best TP2"** or **"Best TP3"**. The video processing module consists of the following buttons:

- **Triangle button (Play)**: It plays the selected video in the video feed located at the center of GUI. 
- **Square button (Stop)**: It stops and resets the selected video. To replay, the above button must be selected. 
- **Pause button**: It freezes the video at the current time stamp. To resume, the same button must be selected. 
- **Set start**: The user can set the starting point of trimming in time. 
- **Set end**: The user can set the ending point of trimming in time. 
- **View**: It shows and saves the trimmed version of video in the current directory. 
- **Crop**: It shows one frame of the video in a separate display and the user can draw a random geometric shape (region-of-interest (ROI) selection) by holding the mouse. Once the user is happy with the drawn ROI, he/she must select **"q"** on the keyboard. 
- **Mask**: The selected ROI will be applied to all frames and the output will be shown in a separate display.
- **Final**: The output of the masking will be displayed in the main video feed of GUI. Moreover, the processed video will be saved in the current directory. 

The above steps must be repeated for **"Best TP2"** and **"Best TP3"** buttons. Once all the processing units are complete, the user must click on **"Play All"** button on the right lower corner. This will play all the processed videos at the same time. The videos can be closed by clicking on **"q"** on the keyboard.


License and Citation
---------
The codes are licensed under GPL 2.0 license. 
