import cv2
import mediapipe as mp

Nfing = "None"
cap = cv2.VideoCapture(0)

# Call hand pipeline module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 1024, 768)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

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

            if (cx4 > cx3 and cy8 < cy6 and cy12 < cy10 and cy16 < cy14 and cy20 < cy18):
                Nfing = "Thumb  Index   Middle  Ring    Little"
            elif (cx4 < cx3 and cy8 < cy6 and cy12 < cy10 and cy16 < cy14 and cy20 < cy18):
                Nfing = "Index   Middle  Ring    Little"
            elif (cx4 < cx3 and cy8 > cy6 and cy12 < cy10 and cy16 < cy14 and cy20 < cy18):
                Nfing = "Middle  Ring    Little"
            elif (cx4 < cx3 and cy8 > cy6 and cy12 > cy10 and cy16 < cy14 and cy20 < cy18):
                Nfing = "Ring    Little"
            elif (cx4 > cx3 and cy8 < cy6 and cy12 < cy10 and cy16 < cy14 and cy20 > cy18):
                Nfing = "Thumb  Index   Middle  Ring"
            elif (cx4 > cx3 and cy8 < cy6 and cy12 < cy10 and cy16 > cy14 and cy20 > cy18):
                Nfing = "Thumb  Index   Middle"
            elif (cx4 > cx3 and cy8 < cy6 and cy12 > cy10 and cy16 > cy14 and cy20 > cy18):
                Nfing = "Thumb  Index"
            elif (cx4 > cx3 and cy8 < cy6 and cy12 < cy10 and cy16 > cy14 and cy20 < cy18):
                Nfing = "Thumb  Index   Middle  Little"
            elif (cx4 > cx3 and cy8 < cy6 and cy12 > cy10 and cy16 < cy14 and cy20 < cy18):
                Nfing = "Thumb  Index  Ring    Little"
            elif (cx4 > cx3 and cy8 > cy6 and cy12 < cy10 and cy16 < cy14 and cy20 < cy18):
                Nfing = "Thumb  Middle  Ring    Little"
            elif cx4 > cx3:
                Nfing = "Thumb"
            elif cx8 > cx6:
                Nfing = "Index"
            elif cx12 > cx10:
                Nfing = "Middle"
            elif cx16 > cx14:
                Nfing = "Ring"
            elif cx20 > cx18:
                Nfing = "Little"
            elif (cx4 < cx3 and cy8 > cy6 and cy12 > cy10 and cy16 > cy14 and cy20 > cy18):
                Nfing = "None"
            else:
                Nfing = "None"

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, str(Nfing), (70, 450), cv2.FONT_HERSHEY_PLAIN, 1.75,
                (700, 180, 100), 2)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# Close all open windows
cv2.destroyAllWindows()
