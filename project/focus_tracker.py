import cv2
import time
import winsound
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

running = False  # Control flag for UI


def start_tracking_loop():
    global running
    running = True

    print("\n🎯 AI Study Focus Tracker Started\n")

    # Load face detection model
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Webcam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    time.sleep(2)

    if not cap.isOpened():
        print("❌ Could not access webcam")
        return

    # Variables
    last_state = "focused"
    last_time = time.time()
    total_focused = 0
    total_distracted = 0
    distract_start = None
    alert_threshold = 5  # seconds

    while running:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        current_time = time.time()

        if len(faces) > 0:
            if last_state == "distracted":
                total_distracted += current_time - last_time

            last_state = "focused"
            distract_start = None

            cv2.putText(frame, "Status: FOCUSED ✅", (30, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        else:
            if last_state == "focused":
                total_focused += current_time - last_time

            last_state = "distracted"

            if distract_start is None:
                distract_start = current_time
            else:
                elapsed = current_time - distract_start
                if elapsed > alert_threshold:
                    cv2.putText(frame, "⚠️ ALERT: Stay Focused!", (30, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    winsound.Beep(1000, 700)

            cv2.putText(frame, "Status: DISTRACTED ❌", (30, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        last_time = current_time

        cv2.imshow("AI Focus Tracker - Press Q to Stop", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Shutdown
    cap.release()
    cv2.destroyAllWindows()

    if last_state == "focused":
        total_focused += time.time() - last_time
    else:
        total_distracted += time.time() - last_time

    # Log Data
    total_time = total_focused + total_distracted
    focus_percent = (total_focused / total_time) * 100 if total_time > 0 else 0

    log_file = "focus_log.csv"
    session_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    df = pd.DataFrame({
        "Session": [session_time],
        "Total_Time(s)": [round(total_time, 1)],
        "Focused_Time(s)": [round(total_focused, 1)],
        "Distracted_Time(s)": [round(total_distracted, 1)],
        "Focus_Percent(%)": [round(focus_percent, 1)]
    })

    if os.path.exists(log_file):
        df.to_csv(log_file, mode="a", index=False, header=False)
    else:
        df.to_csv(log_file, index=False)

    print("\n📌 Session Logged Successfully")



def stop():
    """Called by UI to end the loop"""
    global running
    running = False
