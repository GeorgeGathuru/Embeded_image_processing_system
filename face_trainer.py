import os
import cv2
import numpy as np
from PIL import Image


face_cascade=cv2.CascadeClassifier("/home/george/PycharmProjects/Embeded image processing system/haarcascade_frontalface_alt2.xml")

# recognizer=cv2.face_LBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'George'
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir= os.path.join(BASE_DIR,"images")
print(path)

def getImages(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # print(imagePaths)
    faces = []
    IDs = []
    current_id=0


    for imagePath in imagePaths:
        # pil_image = Image.open(path).convert("L")
        label = os.path.basename(os.path.basename(path))
        label= np.array(label)
        print(label)
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        print(faceNp)
        # faces = face_cascade.detectMultiScale(faceNp, scaleFactor=1.5, minNeighbors=4)

        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)


    #     print(IDs)
    # cv2.imshow("Training",faceNp)
    # cv2.waitKey(10)
    return np.array(IDs), faces


IDs, faces = getImages(path)

recognizer.train(faces, IDs)
recognizer.save('recognizer/trainingData.yml')
# cv2.destroyAllWindows()