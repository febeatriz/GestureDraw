# GestureDraw 🎨🤚

**GestureDraw** is a desktop application developed in Python that uses computer vision to allow the user to draw in the air using only hand gestures captured by the computer's webcam.

The system tracks movements in real-time, turning your hand into a mouse and your fingers into drawing and erasing tools on a virtual canvas.

## 🚀 Features and Interaction Rules

The system recognizes finger positions to activate different modes. For safety and precision, drawing and erasing actions are only executed when **exactly one** specific finger is raised.

* ✏️ **Drawing Mode:** Activated only when the **index finger** is raised. The movement generates continuous lines on the canvas.
* 🧹 **Eraser Mode:** Activated only when the **pinky finger** is raised. Erases the strokes near the finger's current position.
* ⏸️ **Neutral Mode:** Activated with the **hand fully open**. No action is executed, and the virtual cursor disappears, pausing the interaction.

## 🛠️ Technologies Used

* **Python 3.11+**
* **OpenCV:** For real-time video capture and visual rendering.
* **MediaPipe Hands:** For precise detection and tracking of the 21 hand landmarks.
* **NumPy:** For mathematical calculations and canvas matrix manipulation.

## 📂 Project Structure

The project was built using a modular and object-oriented architecture, clearly separating computer vision from business rules and interface:

```text
AirDraw/
│
├── src/
│   ├── main.py                     # Application entry point
│   ├── hand_tracking/              # Computer vision module
│   │   ├── detector.py             # MediaPipe initialization and usage
│   │   └── finger_utils.py         # Logic to identify raised fingers
│   ├── gestures/                   # Control logic
│   │   └── gesture_manager.py      # State and command management
│   ├── drawing/                    # Canvas tools
│   │   ├── canvas.py               # Drawing surface
│   │   ├── brush.py                # Pen/stroke logic
│   │   └── eraser.py               # Eraser logic
│   └── utils/                      # General utilities
│       ├── constants.py            # Colors, thicknesses, and settings
│       └── helpers.py              # Mathematical/visual helper functions
│
├── assets/                         # Images, icons, etc.
├── docs/                           # Additional documentation
└── tests/                          # Unit and integration tests
