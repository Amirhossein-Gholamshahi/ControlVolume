import time

import cv2
import mediapipe as mp
import pyautogui

wb = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

while True:

    success, img = wb.read()

    if not success:
        break
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)


    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

            pinky_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y
            middle_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y


            if index_finger_y < thumb_y:
                hand_gesture = "pointing up"
            elif index_finger_y > thumb_y:
                hand_gesture = "pointing down"
            elif pinky_y > thumb_y:
                hand_gesture = "pinky up"
            # elif middle_finger_y > thumb_y and middle_finger_y > index_finger_y:
            #     hand_gesture = "middle up"
            else:
                hand_gesture = "other"

            if hand_gesture == "pointing up":
                pyautogui.press('volumeup')
            elif hand_gesture == "pointing down":
                pyautogui.press('volumedown')
            elif hand_gesture == "pinky up":
                pyautogui.press("playpause")
            # elif hand_gesture == "middle up":
            #     pyautogui.press("prevtrack")

            cv2.imshow("Volume Control With Hand Gestures", img)
            key = cv2.waitKey(1)
            if key == 27:
                break
wb.release()
cv2.destroyAllWindows()
