import tkinter as tk
from PIL import ImageTk, Image
import os

import requests
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO
import os
import cv2


def write_slogan():
    print("Tkinter is easy to use!")
  
def emotionCheck(emotion, but_no):
    global kolor1
    global button
    kolor1 = "red"
    if(emotion>0.5):
            print("correct")
            button_arr[but_no].config(bg="green")
    else:
            print("wrong")
            button_arr[but_no].config(bg="red")
    
    
  # Replace <Subscription Key> with your valid subscription key.
subscription_key = "78b8678ae0a849cf9eeda79b7e0ffcc3" #DSFace API  
 
kolor1 = "black"
kolor2 = "black"
kolor3 = "black"
kolor4 = "black"
   

camera = cv2.VideoCapture(0)
while True:
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('test.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()


    
 


# Set image path from local file.
image_path = os.path.join('test.jpg')

assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the westcentralus region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

image_data = open(image_path, "rb")

headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key}
params = {
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,smile,' +
    'emotion'
}

response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
response.raise_for_status()
faces = response.json()

# Display the original image and overlay it with the face information.
image_read = open(image_path, "rb").read()
image = Image.open(BytesIO(image_read))

plt.figure(figsize=(8, 8))
ax = plt.imshow(image, alpha=1)
for face in faces:
    fr = face["faceRectangle"]
    fa = face["faceAttributes"]
    origin = (fr["left"], fr["top"])
    p = patches.Rectangle(
        origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
    ax.axes.add_patch(p)
    plt.text(origin[0], origin[1], "%s, %d"%(fa["gender"].capitalize(), fa["age"]),
             fontsize=20, weight="bold", va="bottom")
_ = plt.axis("off")
plt.show()

print(faces)

#
angerValue = faces[0]['faceAttributes']['emotion']['anger']
contemptValue = faces[0]['faceAttributes']['emotion']['contempt']
disgustValue  = faces[0]['faceAttributes']['emotion']['disgust']
fearValue = faces[0]['faceAttributes']['emotion']['fear']
happinessValue = faces[0]['faceAttributes']['emotion']['happiness']
neutralValue = faces[0]['faceAttributes']['emotion']['neutral']
sadnessValue = faces[0]['faceAttributes']['emotion']['sadness']
surpriseValue = faces[0]['faceAttributes']['emotion']['surprise']
   

root = tk.Tk()

frame = tk.Frame(root)


button1 = tk.Button(frame, 
                   text="Happy", 
                   font=("Courier", 20),
                   fg=kolor1,
                   command = lambda: emotionCheck(happinessValue,0) )
button1.pack(side=tk.LEFT)
button1.config(width=5, height=1)



button2 = tk.Button(frame, 
                   text="Angry", 
                   font=("Courier", 20),
                   fg=kolor2,
                   command =lambda: emotionCheck(angerValue,1))
button2.pack(side=tk.LEFT)
button2.config(width=5, height=1)

button3 = tk.Button(frame, 
                   text="Sad",
                   font=("Courier", 20),
                   fg=kolor3,
                   command =lambda: emotionCheck(sadnessValue,2))
button3.pack(side=tk.LEFT)
button3.config(width=4, height=1)


button4 = tk.Button(frame, 
                   text="Neutral", 
                   font=("Courier", 20),
                   fg=kolor4,
                   command =lambda: emotionCheck(neutralValue,3))
button4.pack(side=tk.LEFT)
button4.config(width=7, height=1)

button5 = tk.Button(frame, 
                   text="Contempt", 
                   font=("Courier", 20),
                   fg=kolor4,
                   command =lambda: emotionCheck(contemptValue,4))
button5.pack(side=tk.LEFT)
button5.config(width=8, height=1)

button6 = tk.Button(frame, 
                   text="Disgust", 
                   font=("Courier", 20),
                   fg=kolor4,
                   command =lambda: emotionCheck(disgustValue,5))
button6.pack(side=tk.LEFT)
button6.config(width=7, height=1)

button7 = tk.Button(frame, 
                   text="Fear", 
                   font=("Courier", 20),
                   fg=kolor4,
                   command =lambda: emotionCheck(fearValue,6))
button7.pack(side=tk.LEFT)
button7.config(width=6, height=1)

button8 = tk.Button(frame, 
                   text="Surprise", 
                   font=("Courier", 20),
                   fg=kolor4,
                   command =lambda: emotionCheck(surpriseValue,7))
button8.pack(side=tk.LEFT)
button8.config(width=9, height=1)

#button9 = tk.Button(frame, 
#                   text="dupa", 
#                   font=("Courier", 20),
#                   fg=kolor4,
#                   command =lambda: emotionCheck(surpriseValue,8))
#button8.pack(side=tk.BOTTOM)
#button8.config(width=9, height=1)

button_arr = [button1, button2, button3, button4,button5,button6,button7,button8]
frame.pack()


img = ImageTk.PhotoImage(Image.open("test.jpg"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()



