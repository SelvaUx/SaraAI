import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=FutureWarning)
import threading, cv2

def start_gesture_listener():
    import mediapipe as mp
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1)
    cap = cv2.VideoCapture(0)
    def loop():
        while True:
            ok, img = cap.read()
            if not ok: break
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            res = hands.process(rgb)
            if res.multi_hand_landmarks:
                # simple open-palm detection
                print("Gesture detected")
    threading.Thread(target=loop, daemon=True).start()
