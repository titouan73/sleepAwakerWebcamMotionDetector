[![fr](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/titouan73/sleepAwakerWebcamMotionDetector)

# Motion detection with a webcam and standby management
This Python script allows you to detect movements in front of a webcam and to wake up the computer when a movement is detected.

## Prerequisites
To use this script, you need :

- Python 3.x (tested with version 3.8)
- OpenCV (`pip install opencv-python`)
- PyAutoGUI (`pip install pyautogui`)


## Optional

- xscreensaver (to put the computer to sleep when no movement is detected)
- A package manager like apt or yum (to install xscreensaver)


## Usage

1. Connect a webcam to your computer.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script by typing python script_name.py.
4. The webcam window opens and displays in real time what is happening in front of the camera.
5. When motion is detected, a green rectangle appears around the moving object and the computer wakes up.
6. Press "q" to exit the script.


## Notes

- You can adjust the threshold of motion detection by changing the value of threshold in the function cv2.threshold().
- You can adjust minimum size of objects considered as motion by changing value of min_area in condition if cv2.contourArea(c) < min_area:.

## Launch the script automatically at startup

To run the script automatically every time you start your computer with PM2, follow these steps:

1. Make sure you have PM2 installed by running `npm install pm2 -g` (requires Node.js and npm)
2. Open a terminal and navigate to the directory containing the script
3. Run the command `pm2 start script_name.py` (replace "script_name.py" with the name of your Python file)
4. Run the `pm2 save` command to save the state of PM2
5. Run the `pm2 startup` command to create a PM2 startup script that will be executed every time your computer starts up
6. Follow the instructions displayed in the terminal to finalize the PM2 startup configuration

Once you have completed these steps, your script should be executed automatically each time your computer is started. You can check if the script is running by using the pm2 list command.

> Note: if you want to stop the script being run by PM2, use the command `pm2 stop script_name.py`. If you want to remove it from the list of processes managed by PM2, use the command `pm2 delete script_name.py`.

## License

This script is under MIT license. Feel free to use it and adapt it to your needs.

Translated with www.DeepL.com/Translator (free version)