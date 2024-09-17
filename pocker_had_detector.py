from ultralytics import YOLO
import cv2
import cvzone
import math
import pocker_function
 
cap = cv2.VideoCapture("./handRanking.mp4")
 
model = YOLO("playingCards.pt")
classNames = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']
 
while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame from the video.")
        break

    results = model(img, stream=True)
    hand = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            
            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            
            # Class Name
            cls = int(box.cls[0])

            # Check if the class index is within the bounds of the classNames list
            if cls < len(classNames):
                cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
                
                if conf > 0.5:
                    hand.append(classNames[cls])
            else:
                print(f"Warning: Detected class index {cls} is out of range.")
 
    hand = list(set(hand))
    print(hand)
    if len(hand) == 5:
        results = pocker_function.findPokerHand(hand)
        print(results)
        cvzone.putTextRect(img, f'Your Hand: {results}', (300, 75), scale=3, thickness=5)
 
    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
