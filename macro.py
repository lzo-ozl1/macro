import time
import threading
import tkinter as tk
from pynput.keyboard import Key, Controller

# 키보드 컨트롤러 초기화
keyboard = Controller()

is_running = False
macro_thread = None

def macro_loop():
    global is_running
    
    # 시작 버튼 누른 후 3초 여유 대기 (창 전환용)
    for _ in range(30):
        if not is_running: return
        time.sleep(0.1)
        
    while is_running:
        # ==================================================
        # 1부: 쉬프트 30초 -> F키 -> 왼쪽 -> 쉬프트 10초 -> 오른쪽
        # ==================================================
        
        # [1] 쉬프트 30초 누르기
        if not is_running: return
        status_label.config(text="[1] 쉬프트 5초 누르는 중...", fg="green")
        keyboard.press(Key.shift)
        for _ in range(50): 
            if not is_running:
                keyboard.release(Key.shift)
                return
            time.sleep(0.1)
        keyboard.release(Key.shift)
        time.sleep(0.5)
        
        # [2] F 키 입력 (0.2초)
        if not is_running: return
        status_label.config(text="[2] F 키 입력", fg="blue")
        keyboard.press('f')
        time.sleep(0.2)
        keyboard.release('f')
        time.sleep(0.3)
        
        # [3] 왼쪽 방향키 입력 (0.2초)
        if not is_running: return
        status_label.config(text="[3] 왼쪽 방향키 입력", fg="blue")
        keyboard.press(Key.left)
        time.sleep(0.2)
        keyboard.release(Key.left)
        time.sleep(0.5)
        
        # [4] 쉬프트 10초 누르기
        if not is_running: return
        status_label.config(text="[4] 쉬프트 5초 누르는 중...", fg="green")
        keyboard.press(Key.shift)
        for _ in range(50): # 10초 대기
            if not is_running:
                keyboard.release(Key.shift)
                returnㄹ
            time.sleep(0.1)
        keyboard.release(Key.shift)
        time.sleep(0.5)
        
        # [5] 오른쪽 방향키 입력 (0.1초)
        if not is_running: return
        status_label.config(text="[5] 오른쪽 방향키 입력", fg="blue")
        keyboard.press(Key.right)
        time.sleep(0.1)
        keyboard.release(Key.right)
        time.sleep(0.5)

        # ==================================================
        # 2부: 쉬프트 30초 -> 왼쪽 -> 쉬프트 10초 -> 오른쪽 (루프)
        # ==================================================
        
        # [6] 쉬프트 30초 누르기
        if not is_running: return
        status_label.config(text="[6] 쉬프트 5초 누르는 중...", fg="green")
        keyboard.press(Key.shift)
        for _ in range(50): 
            if not is_running:
                keyboard.release(Key.shift)
                return
            time.sleep(0.1)
        keyboard.release(Key.shift)
        time.sleep(0.5)
        
        # [7] 왼쪽 방향키 입력 (0.2초)
        if not is_running: return
        status_label.config(text="[7] 왼쪽 방향키 입력", fg="blue")
        keyboard.press(Key.left)
        time.sleep(0.2)
        keyboard.release(Key.left)
        time.sleep(0.5)
        
        # [8] 쉬프트 10초 누르기
        if not is_running: return
        status_label.config(text="[8] 쉬프트 5초 누르는 중...", fg="green")
        keyboard.press(Key.shift)
        for _ in range(50): # 10초 대기
            if not is_running:
                keyboard.release(Key.shift)
                return
            time.sleep(0.1)
        keyboard.release(Key.shift)
        time.sleep(0.5)
        
        # [9] 오른쪽 방향키 입력 (0.2초) -> 이후 다시 [1]번으로 루프
        if not is_running: return
        status_label.config(text="[9] 오른쪽 방향키 입력 (루프)", fg="blue")
        keyboard.press(Key.right)
        time.sleep(0.1)
        keyboard.release(Key.right)
        time.sleep(0.5)

def start_macro():
    global is_running, macro_thread
    if not is_running:
        is_running = True
        status_label.config(text="상태: 준비 중...", fg="orange")
        start_btn.config(state="disabled")
        stop_btn.config(state="normal")
        
        macro_thread = threading.Thread(target=macro_loop)
        macro_thread.daemon = True
        macro_thread.start()

def stop_macro():
    global is_running
    if is_running:
        is_running = False
        status_label.config(text="상태: 정지됨 🔴", fg="red")
        start_btn.config(state="normal")
        stop_btn.config(state="disabled")

# --- GUI 창 설정 ---
root = tk.Tk()
root.title("맥 매크로 v4.0")
root.geometry("320x130")
root.resizable(False, False)
root.attributes("-topmost", True)

# 상태 표시 레이블
status_label = tk.Label(root, text="상태: 정지됨 🔴", font=("Helvetica", 13, "bold"), fg="red")
status_label.pack(pady=15)

# 버튼 프레임
btn_frame = tk.Frame(root)
btn_frame.pack()

# 시작 버튼
start_btn = tk.Button(btn_frame, text="시작", width=8, command=start_macro)
start_btn.pack(side="left", padx=5)

# 중단 버튼
stop_btn = tk.Button(btn_frame, text="중단", width=8, command=stop_macro, state="disabled")
stop_btn.pack(side="left", padx=5)

def on_closing():
    stop_macro()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
