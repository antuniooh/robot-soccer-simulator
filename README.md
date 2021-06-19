<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/antuniooh/robot-soccer-simulator">

  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/antuniooh/robot-soccer-simulator">
  
  <a href="https://github.com/antuniooh/robot-soccer-simulator/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/antuniooh/robot-soccer-simulator">
  </a>
  
   <img alt="GitHub" src="https://img.shields.io/github/license/antuniooh/robot-soccer-simulator">
</p>


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/antuniooh/robot-soccer-simulator">
    <img src="https://cdn0.iconfinder.com/data/icons/thin-analytics/57/thin-360_hierarchy_diagram_structure-512.png" alt="Logo" width="550">
  </a>
</p>

<p align="center">
  <img alt="Math" src="https://img.shields.io/badge/Math-red?style=for-the-badge&logo=math&logoColor=white"/>
  <img alt="Python" src="https://img.shields.io/badge/Python-darkblue?style=for-the-badge&logo=python&logoColor=white"/>
    <img alt="Graph" src="https://img.shields.io/badge/Graph-darkrgreen?style=for-the-badge&logo=graph&logoColor=white"/>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#-about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#-how-to-run">How To Run</a>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## 💻 About The Project
The program reads the ball trajectory file and using small size robot attributes shows if it is possible for the robot to intercept the ball or not. To define whether there will be an intercept, the robot's intercept radius, its movement speed and the initial position being defined by the user are taken into account.

As soon as the application starts, the user must enter the X and Y position of the robot, so that the calculation is carried out and enables the prediction of contact between the robot and the ball, taking into account its trajectory, as well as the speed of the robot.
For this we use the formula of distance between two points, to calculate all the possibilities of time from the initial position of the robot and the trajectory of the ball (from the txt file).

![app](https://github.com/antuniooh/robot-soccer-simulator/blob/master/images/app.gif)

<!-- HOW TO RUN -->
## 🚀 How To Run

```bash

# Clone the repository
$ git clone https://github.com/antuniooh/robot-soccer-simulator.git

# Access the project folder in your terminal / cmd
$ cd robot-soccer-simulator/src

# Install the libs
$ python -m pip install -U pip
$ python -m pip install -U matplotlib

# In both Windows and Linux, the execution is done by executing the following line in the terminal, or using an IDE of your choice.
$ python3 BP_main.py


<!-- AUTHORS -->
## 🤖 Authors

[Antonio Gustavo](https://github.com/antuniooh)           |  [João Vitor Dias](https://github.com/JoaoDias-223)           |  [Weverson da Silva](https://github.com/WebisD)
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://avatars.githubusercontent.com/u/51217271?v=4" alt="drawing" width="150"/>  |  <img src="https://avatars.githubusercontent.com/u/63318342?v=4" alt="drawing" width="150"/>| <img src="https://avatars.githubusercontent.com/u/49571908?v=4" alt="drawing" width="150"/>
22.119.001-0 | 22.119.006-9 | 22.119.004-4
