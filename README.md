#🎯 AI Focus Tracker  
A real-time focus monitoring system that uses Computer Vision (OpenCV) and Python to detect whether a user is focused or distracted. The system displays live status, plays alerts when distracted for too long, logs session data, and provides a GUI dashboard for easy control.

---

## 🚀 Features
- 🔍 **Real-time face detection** using Haar Cascade  
- ⚠️ **Distraction alerts** (visual + sound)  
- 📊 **Focus percentage logging**  
- 🗂️ **Automatic CSV session storage**  
- 📈 **Progress graphs** using Matplotlib  
- 🖥️ **Tkinter GUI dashboard**  
- ⚡ **Smooth performance** using multi-threading  
- 🧠 **Beginner-friendly project** combining AI + GUI + Data Visualization  

---

---

## 🛠️ Tech Stack
- Python  
- OpenCV  
- Tkinter  
- Pandas  
- Matplotlib  
- Pillow (PIL)  
- Threading  

---

## 📁 Project Structure
AI-Focus-Tracker/
│── focus_tracker.py # Core tracking logic
│── app.py # Tkinter GUI
│── haarcascade_frontalface_default.xml
│── focus_log.csv # Generated automatically

---

## ⚙️ Installation & Setup
1️⃣ Install Requirements

pip install opencv-python pandas matplotlib pillow
3️⃣ Run the GUI Dashboard
python app.py

🎯 How It Works

1) Start focus tracking from the GUI

2) The webcam monitors your face

3) If your face disappears → status changes to DISTRACTED

4) If distraction lasts too long → an alert sound is played

5) Session details (time focused, distracted %) are saved

6) You can view a focus progress graph from the GUI

🧩 Core Logic Overview
Face Detection

The system uses OpenCV’s Haar Cascade model (haarcascade_frontalface_default.xml) to detect the user’s face in real time.

Focus Tracking

The program calculates:

Total session time
Focused time
Distracted time
Focus percentage
Data is logged automatically in focus_log.csv.

📝 Acknowledgments

This project uses the Haar Cascade Frontal Face Detection model from the OpenCV library.
Source: https://github.com/opencv/opencv
