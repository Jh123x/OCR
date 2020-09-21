#For the core OCR functionality
import pytesseract

#Import computer vision
import cv2
import os

from PIL import Image

def main()->None:
    """The main function to be executed"""

    #Path to tesseract (Change it to path for tesseract.exe)
    pytesseract.pytesseract.tesseract_cmd = os.path.join("example_path")

    #Create the video capture
    capture = cv2.VideoCapture(0)

    # #Loop through the frame
    while True:

        #Read the frame from the camera
        ret, frame = capture.read()

        #Covert the image to RGB
        img_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        #Read data in the image
        print(pytesseract.image_to_string(img_rgb))

        #Show the frame
        cv2.imshow('Title',frame)

        #Check if the Q key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #If so break the loop
            break 

    #Release capture and destroy all windows
    capture.release()
    cv2.destroyAllWindows()

#If the file is run as the main file, execute the main function
if __name__ == "__main__":
    main()

