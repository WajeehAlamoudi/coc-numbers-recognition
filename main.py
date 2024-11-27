import mss
import numpy as np
import easyocr
import cv2
import os
import pyautogui  # Import the pyautogui library for clicking
import time  # Import time for delay between captures
import pygame


def capture_screen(region):
    with mss.mss() as sct:
        # Capture the specified region of the screen
        screenshot = sct.grab(region)
        # Convert to a numpy array
        img = np.array(screenshot)
        # Convert BGRA to BGR
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img


def extract_text_from_image(image):
    # Create an EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Read text from the image
    result = reader.readtext(image)

    # Check if at least one result is found
    if len(result) > 0:
        text = result[0][1]  # The detected text
        prob = result[0][2]  # The probability of the detected text

        # Remove spaces from the detected text and convert to int
        text = text.replace(" ", "")
    else:
        text = "0"  # Default to 0 if no text found
        prob = 0  # Probability is zero

    return int(text), prob  # Return text as integer


# Define the region of the screen to capture (left, top, width, height)
region = {
    "top": 640,  # y coordinate of the top left corner
    "left": 1035,  # x coordinate of the top left corner
    "width": 140,  # width of the capture area
    "height": 35  # height of the capture area
}


# Function to save images with incrementing names
def save_image_with_incrementing_name(image, directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Find the next available filename
    index = 2  # Start from image2
    while True:
        filename = os.path.join(directory, f"image{index}.png")
        if not os.path.exists(filename):
            break
        index += 1

    # Save the image
    cv2.imwrite(filename, image)
    print(f"Captured image saved as '{filename}'.")


# Function to click the mouse at a specified position
def click_mouse(x, y):
    pyautogui.click(x, y)  # Click at the specified position
    print(f"Clicked at position ({x}, {y}).")


# Main function
def main():
    max_n = int(1200000 / 1100)
    n = 1
    while n <= max_n:  # Continuous loop
        captured_image = capture_screen(region)  # Capture the screen
        save_image_with_incrementing_name(captured_image, 'data')  # Save the image
        detected_text, probability = extract_text_from_image(captured_image)  # Extract text

        # Check the conditions for clicking
        if detected_text >= 900000 and probability >= 0.79:
            print(f"Detected text: {detected_text}, Probability: {probability}.")
            print('the village found')

            # Initialize pygame mixer
            pygame.mixer.init()
            # Path to your sound file
            sound_file = r'data/The demanded village found, please check clash of clans.mp3'
            # Load the sound file
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
            time.sleep(30)  # to check the village
            click_mouse(1100, 1150)
            break
        else:
            print(f"Detected text: {detected_text}, Probability: {probability} CONTINUE SEARCHING! n = {n}")
            click_mouse(2100, 1150)
            n = n + 1
            # Perform the click
        time.sleep(3)  # Optional delay between iterations
        # to exit searching when n is max
    click_mouse(1100, 1150)


# Run the main function
if __name__ == "__main__":
    main()
