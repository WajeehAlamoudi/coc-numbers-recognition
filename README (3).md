
# CoC Numbers Recognition with EasyOCR

This project demonstrates how to use EasyOCR to recognize numbers from Clash of Clans (CoC) images. The goal is to extract numeric values from screenshots or in-game images that contain numbers (such as resources or player scores) using Optical Character Recognition (OCR).
# Description
- works with not only coc but, for any search games.
- it captured a specific region in screen then read the value.
- the preform a clikck if the village not as wantted.
# Libraries Required
- pyautogui: For capturing the screen and simulating mouse clicks.
- easyocr: For optical character recognition (OCR) to extract text.
- opencv-python: For image manipulation and saving images.
- numpy: For working with image arrays.
# How to use
- ensure the read region.
- ensure the pc screen not zoomed (from settings).
- create data file to store read image to track the process. (you can remove this part from the code).
# Note
- it has small drawback:
1. Regular falling in reading millions digits.
2. it reads only one place like only Golds or Cups, etc.
3. Need to modify the screen reagion according to yours.
- due that I made coc number generator to simulate coc numbers to train custom EasyOCR model:
https://github.com/WajeehAlamoudi/clash-of-clans-numbers-generator

