import numpy as np
import dlib
import cv2
from math import hypot

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

font = cv2.FONT_HERSHEY_TRIPLEX

def compute_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_lenght / ver_line_lenght
    return ratio

def compute_mouth_ratio(lips_points, facial_landmarks):
    left_point = (facial_landmarks.part(lips_points[0]).x, facial_landmarks.part(lips_points[0]).y)
    right_point = (facial_landmarks.part(lips_points[2]).x, facial_landmarks.part(lips_points[2]).y)
    center_top = (facial_landmarks.part(lips_points[1]).x, facial_landmarks.part(lips_points[1]).y)
    center_bottom = (facial_landmarks.part(lips_points[3]).x, facial_landmarks.part(lips_points[3]).y)

    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
    if hor_line_lenght == 0:
        return ver_line_lenght
    ratio = ver_line_lenght / hor_line_lenght
    return ratio

count = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:

        landmarks = predictor(gray, face)

        left_eye_ratio = compute_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = compute_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
        cv2.putText(frame, str(blinking_ratio), (0, 13), font, 0.5, (100, 100, 100))
        print(left_eye_ratio,right_eye_ratio,blinking_ratio)

        inner_lip_ratio = compute_mouth_ratio([60,62,64,66], landmarks)
        outter_lip_ratio = compute_mouth_ratio([48,51,54,57], landmarks)
        mouth_opening_ratio = (inner_lip_ratio + outter_lip_ratio) / 2;
        cv2.putText(frame, str(mouth_opening_ratio), (448, 13), font, 0.5, (100, 100, 100))
        print(inner_lip_ratio,outter_lip_ratio,mouth_opening_ratio)
        if mouth_opening_ratio > 0.38 and blinking_ratio > 4 or blinking_ratio > 4.3:
            count = count+1
        else:
            count = 0
        x,y = face.left(), face.top()
        x1,y1 = face.right(), face.bottom()
        if count>8:
            cv2.rectangle(frame, (x,y), (x1,y1), (0, 0, 255), 2)
            cv2.putText(frame, "Drowsing", (x, y-5), font, 0.5, (0, 0, 255))
        else:
            cv2.rectangle(frame, (x,y), (x1,y1), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
