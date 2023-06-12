# CPIS-222-project
If you do not have Python, follow the following steps to install Python
    - Go to https://www.python.org/downloads/release/python-3114/
    - Scroll to the bottom, select the installer that corresponds to your Operating System.
    - Click on Windows installer (64-bit) if your device is a Windows 64-bit device running Windows as Operating System

Open Powershell or Command Prompt as administrator.
Install psutil by running this command
```
pip3 install psutil
```
Install matplotlib by running this command
```
pip3 install matplotlib
```
Download main.py at [this link](https://github.com/tfulanchan/CPIS-222-project/blob/main/main.py)
In Powershell or Command Prompt, navigate to the directory where you downloaded the main.py file. You can use file explorer to navigate to the directory. Then right-click your mouse and select “Open in Terminal”. You can also use Powershell as Administrator


For simulation of FIFO and LRU algorithms, run this command in Command Prompt or Powershell:
```
python simulation.py
```
You will be prompted to "Enter number of pages: "
You will then be prompted to "Enter page reference string generation method (manual/uniform/gaussian): " You can only type “manual” or “uniform” or “gaussian”.
You will then be prompted to "Enter number of available frames: "
You will then be prompted to "Enter page replacement algorithm (LRU/FIFO): "

Sample input & output:
![7 pages, gaussian, 4 frames, FIFO](https://github.com/tfulanchan/CPIS-222-project/blob/main/output_7pages_gaussian_4frames_FIFO.jpg)
![7 pages, uniform, 4 frames, LRU](https://github.com/tfulanchan/CPIS-222-project/blob/main/output_7pages_uniform_4frames_LRU.jpg)



For graphs of comparison between FIFO and LRU, run this command in Command Prompt or Powershell:
```
python comparisonGraphs.py
```
You will be prompted to “Enter number of pages:”. Enter number of pages of your choice.
You will then be prompted to “Enter page reference string generation method (manual/uniform/gaussian):”. You can only type “manual” or “uniform” or “gaussian”

Two graphs will be displayed if the input is correct.

Sample input & output:
![3 pages. Uniform.](https://github.com/tfulanchan/CPIS-222-project/blob/main/output_comparisonGraphs_3pages_uniform.jpg
)
