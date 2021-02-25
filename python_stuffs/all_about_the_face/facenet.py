from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
import cv2
from PIL import ImageDraw, Image
import numpy as np
# device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
device = 'cpu'
# If required, create a face detection pipeline using MTCNN:

# Create an inception resnet (in eval mode):
# resnet = InceptionResnetV1(pretrained='vggface2').eval()

cap = cv2.VideoCapture(0)
width  = int(cap.get(3))
height = int(cap.get(4))

mtcnn = MTCNN(keep_all=True, device=device)

fps = cap.get(5)
print('WxH: {}x{}'.format(width,height))
print('FPS: ', fps)
while(True):
    ret, frame = cap.read()
    boxes, _ = mtcnn.detect(frame)
    frame_draw = Image.fromarray(frame.copy())
    draw = ImageDraw.Draw(frame_draw)
    if type(boxes).__module__ == np.__name__:
        for box in boxes:
            draw.rectangle(box.tolist(), outline=(0,255,0), width=1)
    
    cv2.imshow("Ren Jie's webcam", np.array(frame_draw, dtype='uint8'))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows