import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def detect_face_and_eyes():
    file_path = filedialog.askopenfilename()  
    if file_path:
        img = cv2.imread(file_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)
        if len(faces) == 0:
            messagebox.showinfo("Result", "No face detected")
        else:
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))
                if len(eyes) == 0:
                    messagebox.showinfo("Result", "Face detected, but eyes closed")
                else:
                    messagebox.showinfo("Result", "Face detected, and eyes open")
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)
                cv2.imshow("Image with Face and Eye Detection", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
window = tk.Tk()
window.title("Face and Eye Detection")
detect_button = tk.Button(window, text="Detect Face and Eyes", command=detect_face_and_eyes)
detect_button.pack(pady=20)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
window.mainloop()