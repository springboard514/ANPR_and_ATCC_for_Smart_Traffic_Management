##########################################################
# Real-time video recording and processing with a webcam #
##########################################################

import cv2
from ultralytics import YOLO

model = YOLO('yolo11x.pt')
print(model.names)

webcamera = cv2.VideoCapture(0)

#Height and width adjustment
# webcamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# webcamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    success, frame = webcamera.read()

    results = model.track(frame, persist=True)
    cv2.putText(frame, f"Total: {len(results[0].boxes)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                cv2.LINE_AA)
    cv2.imshow("Live Camera", results[0].plot())

    if cv2.waitKey(1) == ord('q'):
        break

webcamera.release()
cv2.destroyAllWindows()
