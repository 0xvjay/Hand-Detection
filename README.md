# Real Time Hand-Detection
  
### Recognizes hand gesture using OpenCV and Python and controls VLC player depending on the gestures.
----------------------------------------------------------------------------------------------------------------------------
## Libraries Needed
----------------------------------------------------------------------------------------------------------------------------

- numpy
- cv2
- openCV
- cvzone
- pyautogui


## How it works
----------------------------------------------------------------------------------------------------------------------------

- Capture real time video sequence from camera
- Captured video is converted into grayscale and further blurred to remove strong pixels
- Running average method over 30 frames is used for background substraction and giving the hand region as foreground
- Convex Hull and convexity defects are further used to find the number for fingers raised which is equal to one more than total number of defects.
- Based on the number of defects VLC player is controlled. Available Commands are
  - Play
  - Pause
  - Mute
  - Forward
  - Backward
  

## Screenshots
----------------------------------------------------------------------------------------------------------------------------

- Play and Pause through Palm

![alt text](https://github.com/st0rm2/Hand-Detection/blob/main/images/Picture1.png)

- Volume Up through 1 Finger up

![alt text](https://github.com/st0rm2/Hand-Detection/blob/main/images/Picture2.png)


## Contribution
----------------------------------------------------------------------------------------------------------------------------

- Feel free to contribute to fix any problems, or to submit an issue!
- Just make a PR to add any improvement you would like to see in the code.
