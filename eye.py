import cv2
import mediapipe as mp
import pyautogui
import time
import threading

print(cv2.__version__)
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
smoothing_buffer = []
blink_threshold = 0.2
blink_count = 0
last_blink_time = time.time()
frame_skip = 5
frame_count = 0

frame = None


def smooth_position(x, y):
    global smoothing_buffer
    smoothing_buffer.append((x, y))
    if len(smoothing_buffer) > 5:
        smoothing_buffer.pop(0)
    avg_x = sum(pos[0] for pos in smoothing_buffer) / len(smoothing_buffer)
    avg_y = sum(pos[1] for pos in smoothing_buffer) / len(smoothing_buffer)
    return avg_x, avg_y


def capture_frames():
    global frame
    while True:
        _, frame = cam.read()


capture_thread = threading.Thread(target=capture_frames)
capture_thread.daemon = True
capture_thread.start()

while True:
    if frame is None:
        continue

    # frame = cv2.flip(frame,-1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue

    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks

    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Draw green circles around eye landmarks
        for id in [33, 133, 362, 263]:  # Example landmarks for eyes
            x = int(landmarks[id].x * frame_w)
            y = int(landmarks[id].y * frame_h)
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            avg_x, avg_y = smooth_position(x, y)
            screen_x = screen_w / frame_w * avg_x
            screen_y = screen_h / frame_h * avg_y
            pyautogui.moveTo(screen_x, screen_y)

        left = [landmarks[145], landmarks[159]]
        if (left[0].y - left[1].y) < blink_threshold:
            current_time = time.time()
            if current_time - last_blink_time < 0.5:
                blink_count += 1
            else:
                blink_count = 1
            last_blink_time = current_time
            if blink_count == 2:
                pyautogui.doubleClick()
        else:
            blink_count = 0

        if (left[0].y - left[1].y) < 0.02:
            pyautogui.click()
            pyautogui.sleep(1)

    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
