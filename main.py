import cv2
import keyboard
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
mpHands = mp.solutions.hands
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id,landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                print(x, y)
                lbl = output.multi_handedness[0].classification[0].label
                if len(output.multi_handedness)==2:
                    print("TWO HANDS")
                elif lbl == 'Right':
                    print("its Right")
                elif lbl == 'Left':
                    if id == 8:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        index_x = screen_width/frame_width*x
                        index_y = screen_width/frame_height*y
                        # pyautogui.moveTo(index_x, index_y)
                    if id == 4:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width/frame_width*x
                        thumb_y = screen_width/frame_height*y
                        print('outside', abs(index_y - thumb_y))
                        if abs(index_y - thumb_y) < 8:
                            keyboard.press("right")
                            # pyautogui.click()
                            pyautogui.sleep(1)
                    if id == 12:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        middle_x = screen_width/frame_width*x
                        middle_y = screen_width/frame_height*y
                        print('outside', abs(thumb_y - middle_y))
                        if abs(thumb_y - middle_y) < 8:
                            keyboard.press("left")
                            # pyautogui.click()
                            pyautogui.sleep(1)
                else:
                    print("else")
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)