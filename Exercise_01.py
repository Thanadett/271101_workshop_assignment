# This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

# Call hand pipeline module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:

    Finger = ['Thumb', 'Index', 'Middle', 'Ring', 'Little']

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
                if id == 3:
                    cx3, cy3 = cx, cy
                if id == 8:
                    cx8, cy8 = cx, cy
                if id == 6:
                    cx6, cy6 = cx, cy
                if id == 12:
                    cx12, cy12 = cx, cy
                if id == 10:
                    cx10, cy10 = cx, cy
                if id == 16:
                    cx16, cy16 = cx, cy
                if id == 14:
                    cx14, cy14 = cx, cy
                if id == 20:
                    cx20, cy20 = cx, cy
                if id == 18:
                    cx18, cy18 = cx, cy

            if cx3 > cx4 and 'Thumb' in Finger:
                Finger.remove('Thumb')
            if cy8 > cy6 and 'Index' in Finger:
                Finger.remove('Index')
            if cy12 > cy10 and 'Middle' in Finger:
                Finger.remove('Middle')
            if cy16 > cy14 and 'Ring' in Finger:
                Finger.remove('Ring')
            if cy20 > cy18 and 'Little' in Finger:
                Finger.remove('Little')

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, str(Finger), (50, 450), cv2.FONT_HERSHEY_PLAIN, 1.75,
                (700, 150, 50), 2)
    cv2.imshow("Image", img)

    # Esc --> End Program
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Closeing all open windows
# cv2.destroyAllWindows()
