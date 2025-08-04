## 시력 보호 알림  

## 시력 보호 알림 Source code  

import tkinter as tk
from tkinter import simpledialog, messagebox

# 루트 창 생성
root = tk.Tk()
root.withdraw()  # 처음엔 숨기기

# 사용자에게 입력 받기 (초 단위)
interval_seconds = simpledialog.askstring("시력 보호 설정", "몇 초마다 알림을 받을까요? (숫자만 입력)")

# 입력 확인
try:
    interval_seconds = int(interval_seconds)
    if interval_seconds <= 0:
        raise ValueError

    interval_ms = interval_seconds * 1000  # 밀리초로 변환

except:
    messagebox.showerror("오류", "올바른 숫자를 입력해주세요!")
    root.destroy()
    exit()

# 팝업 알림 함수
def show_reminder():
    popup = tk.Toplevel()
    popup.title("시력 보호 알림")
    
    # 팝업 크기 설정
    popup.geometry("300x150")
    
    # 화면 크기 구하기
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    
    # 팝업의 크기 구하기
    popup_width = 300
    popup_height = 150
    
    # 위치 계산
    x = (screen_width - popup_width) // 2
    y = (screen_height - popup_height) // 2
    
    # 팝업 창을 화면 중앙에 위치시키기
    popup.geometry(f"300x150+{x}+{y}")

    label = tk.Label(popup, text="눈을 잠시 5분 동안 쉬어주세요!", font=("Arial", 14))
    label.pack(expand=True)

    popup.after(5000, popup.destroy)  # 5초 뒤 닫기
    root.after(interval_ms, show_reminder)  # 다음 알림 예약

# 첫 알림 예약
root.after(interval_ms, show_reminder)

# tkinter 이벤트 루프 시작
root.mainloop()
