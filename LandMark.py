# This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = 5
cap = cv2.VideoCapture(0)

# Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    cx4, cy4 = cx, cy
                elif id == 3:
                    cx3, cy3 = cx, cy
                elif id == 8:
                    cx8, cy8 = cx, cy
                elif id == 6:
                    cx6, cy6 = cx, cy
                elif id == 12:
                    cx12, cy12 = cx, cy
                elif id == 10:
                    cx10, cy10 = cx, cy
                elif id == 16:
                    cx16, cy16 = cx, cy
                elif id == 14:
                    cx14, cy14 = cx, cy
                elif id == 20:
                    cx20, cy20 = cx, cy
                elif id == 18:
                    cx18, cy18 = cx, cy
            if cy8 > cy6:
                Nfing = 0
            elif cy12 > cy10:
                Nfing = 1
            elif cy16 > cy14:
                Nfing = 2
            elif cy20 > cy18:
                Nfing = 3
            elif cx4 < cx3:
                Nfing = 4
            else:
                Nfing = 5

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, str(int(Nfing)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Closeing all open windows
# cv2.destroyAllWindows()
