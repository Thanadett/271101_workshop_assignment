import cv2
import mediapipe as mp
import time
import pyfirmata

time.sleep(2.0)

# use function drawing_utils to draw straight connect landmark point
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands  # use function hands to find hand on camera


tipIds = [4, 8, 12, 16, 20]  # media-pipe position  of fingertips


def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        # print("Input is an integer number. Number = ", val)
        bv = True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            # print("Input is a float  number. Number = ", val)
            bv = True
        except ValueError:
            # print("No.. input is not a number. It's a string")
            bv = False
    return bv


cport = input('Enter the camera port: ')
while not (check_user_input(cport)):
    print('Please enter a number not string')
    cport = input('Enter the camera port: ')

comport = input('Enter the arduino board COM port: ')
while not (check_user_input(comport)):
    print('Please enter a number not string')
    comport = input('Enter the arduino board COM port: ')

board = pyfirmata.Arduino('COM'+comport)
led_1 = board.get_pin('d:13:o')  # Set pin to output
led_2 = board.get_pin('d:12:o')
led_3 = board.get_pin('d:11:o')
led_4 = board.get_pin('d:10:o')
led_5 = board.get_pin('d:9:o')

# LED write function

## controller.py ##


def led(Finger, led_1, led_2, led_3, led_4, led_5):
    if 'Thumb' in Finger:
        led_1.write(1)
    else:
        led_1.write(0)

    if 'Index' in Finger:
        led_2.write(1)
    else:
        led_2.write(0)

    if 'Middle' in Finger:
        led_3.write(1)
    else:
        led_3.write(0)

    if 'Ring' in Finger:
        led_4.write(1)
    else:
        led_4.write(0)

    if 'Little' in Finger:
        led_5.write(1)
    else:
        led_5.write(0)


######

video = cv2.VideoCapture(int(cport))  # OpenCamera at index position 0

with mp_hand.Hands(min_detection_confidence=0.5,
                   min_tracking_confidence=0.5) as hands:  # (min_detection_confidence, min_tracking_confidence) are Value to considered for detect and tracking image
    while True:
        ret, image = video.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList = []
        Finger = []

        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
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
            if cx3 < cx4:
                Finger.append('Thumb')
            if cy8 < cy6:
                Finger.append('Index')
            if cy12 < cy10:
                Finger.append('Middle')
            if cy16 < cy14:
                Finger.append('Ring')
            if cy20 < cy18:
                Finger.append('Little')

            mp_draw.draw_landmarks(image, hand_landmark,
                                   mp_hand.HAND_CONNECTIONS)

            # import function in module to control arduino output
            led(Finger, led_1, led_2, led_3, led_4, led_5)
            """
            creat condition to put text in frame

            """
            if ((results.multi_hand_landmarks)) != "None":
                cv2.putText(image, str(Finger), (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            0.75, (255, 0, 0), 2)

        cv2.imshow("Frame", image)  # show edited image
        k = cv2.waitKey(1)
        if k == ord('q'):  # press "q" to exit programe
            break
video.release()
cv2.destroyAllWindows()
