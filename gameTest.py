import tkinter as tk
import random
import time

class BrickBreakerGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("벽돌 깨기 게임")
        self.root.resizable(False, False)
        
        # 게임 설정
        self.width = 800
        self.height = 600
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg='black')
        self.canvas.pack()
        
        # 게임 변수
        self.paddle_width = 100
        self.paddle_height = 15
        self.ball_size = self.width // 4  # 화면 너비의 1/4 크기
        self.ball_speed_x = 4
        self.ball_speed_y = -4
        self.score = 0
        self.lives = 3
        self.bricks = []
        self.game_running = True
        
        # 객체 생성
        self.create_paddle()
        self.create_ball()  # 단일 공 생성
        self.create_bricks()
        self.create_score_display()
        
        # 키 바인딩
        self.root.bind('<KeyPress-Left>', self.move_paddle_left)
        self.root.bind('<KeyPress-Right>', self.move_paddle_right)
        self.root.bind('<KeyPress-a>', self.move_paddle_left)
        self.root.bind('<KeyPress-d>', self.move_paddle_right)
        self.root.bind('<KeyPress-r>', self.restart_game)
        self.root.focus_set()
        
        # 게임 루프 시작
        self.game_loop()
    
    def create_paddle(self):
        x = self.width // 2 - self.paddle_width // 2
        y = self.height - 50
        self.paddle = self.canvas.create_rectangle(
            x, y, x + self.paddle_width, y + self.paddle_height,
            fill='blue', outline='white'
        )
    
    def create_ball(self):
        x = self.width // 2 - self.ball_size // 2
        y = self.height // 2
        self.ball = self.canvas.create_oval(
            x, y, x + self.ball_size, y + self.ball_size,
            fill='white'
        )
    
    def create_bricks(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'cyan']
        brick_width = 75
        brick_height = 20
        
        for row in range(8):
            for col in range(10):
                x1 = col * (brick_width + 5) + 35
                y1 = row * (brick_height + 5) + 50
                x2 = x1 + brick_width
                y2 = y1 + brick_height
                
                color = colors[row % len(colors)]
                brick = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color, outline='white'
                )
                self.bricks.append(brick)
    
    def create_score_display(self):
        self.score_text = self.canvas.create_text(
            60, 20, text=f"점수: {self.score}", fill='white', font=('Arial', 14)
        )
        self.lives_text = self.canvas.create_text(
            60, 40, text=f"생명: {self.lives}", fill='white', font=('Arial', 14)
        )
    
    def move_paddle_left(self, event):
        coords = self.canvas.coords(self.paddle)
        if coords[0] > 0:
            self.canvas.move(self.paddle, -15, 0)
    
    def move_paddle_right(self, event):
        coords = self.canvas.coords(self.paddle)
        if coords[2] < self.width:
            self.canvas.move(self.paddle, 15, 0)
    
    def move_ball(self):
        self.canvas.move(self.ball, self.ball_speed_x, self.ball_speed_y)
        
        # 벽 충돌
        ball_coords = self.canvas.coords(self.ball)
        if ball_coords[0] <= 0 or ball_coords[2] >= self.width:
            self.ball_speed_x = -self.ball_speed_x
        
        if ball_coords[1] <= 0:
            self.ball_speed_y = -self.ball_speed_y
        
        # 바닥 충돌
        if ball_coords[3] >= self.height:
            self.lives -= 1
            if self.lives <= 0:
                self.game_over()
            else:
                self.reset_ball()
    
    def check_paddle_collision(self):
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle)
        
        if (ball_coords[2] >= paddle_coords[0] and 
            ball_coords[0] <= paddle_coords[2] and
            ball_coords[3] >= paddle_coords[1] and
            ball_coords[1] <= paddle_coords[3]):
            self.ball_speed_y = -abs(self.ball_speed_y)
            
            # 패들의 어느 부분에 맞았는지에 따라 각도 조정
            ball_center = (ball_coords[0] + ball_coords[2]) / 2
            paddle_center = (paddle_coords[0] + paddle_coords[2]) / 2
            hit_pos = (ball_center - paddle_center) / (self.paddle_width / 2)
            self.ball_speed_x = int(hit_pos * 6)
    
    def check_brick_collision(self):
        ball_coords = self.canvas.coords(self.ball)
        
        for brick in self.bricks[:]:  # 복사본으로 반복
            if brick and self.canvas.coords(brick):  # 벽돌이 존재하는지 확인
                brick_coords = self.canvas.coords(brick)
                
                if (ball_coords[2] >= brick_coords[0] and 
                    ball_coords[0] <= brick_coords[2] and
                    ball_coords[3] >= brick_coords[1] and
                    ball_coords[1] <= brick_coords[3]):
                    
                    self.canvas.delete(brick)
                    self.bricks.remove(brick)
                    self.score += 10
                    self.ball_speed_y = -self.ball_speed_y
                    
                    if not self.bricks:  # 모든 벽돌을 깼을 때
                        self.win_game()
                    break
    
    def reset_ball(self):
        self.canvas.coords(self.ball, 
                          self.width//2 - self.ball_size//2,
                          self.height//2,
                          self.width//2 + self.ball_size//2,
                          self.height//2 + self.ball_size)
        self.ball_speed_x = random.choice([-4, 4])
        self.ball_speed_y = -4
    
    def update_display(self):
        self.canvas.itemconfig(self.score_text, text=f"점수: {self.score}")
        self.canvas.itemconfig(self.lives_text, text=f"생명: {self.lives}")
    
    def game_over(self):
        self.game_running = False
        self.canvas.create_text(
            self.width//2, self.height//2, 
            text="게임 오버!\nR을 눌러 다시 시작", 
            fill='red', font=('Arial', 20), justify=tk.CENTER
        )
    
    def win_game(self):
        self.game_running = False
        self.canvas.create_text(
            self.width//2, self.height//2, 
            text="축하합니다! 승리!\nR을 눌러 다시 시작", 
            fill='green', font=('Arial', 20), justify=tk.CENTER
        )
    
    def restart_game(self, event=None):
        self.canvas.delete("all")
        self.score = 0
        self.lives = 3
        self.bricks = []
        self.game_running = True
        self.ball_speed_x = 4
        self.ball_speed_y = -4
        
        self.create_paddle()
        self.create_ball()
        self.create_bricks()
        self.create_score_display()
    
    def game_loop(self):
        if self.game_running:
            self.move_ball()
            self.check_paddle_collision()
            self.check_brick_collision()
            self.update_display()
        
        self.root.after(16, self.game_loop)  # 약 60 FPS
    
    def run(self):
        print("tkinter 벽돌 깨기 게임을 시작합니다!")
        print("조작법:")
        print("- 좌우 화살표 키 또는 A/D 키로 패들 이동")
        print("- R 키로 게임 재시작")
        print("- 대형 공으로 게임을 즐기세요!")
        self.root.mainloop()

# 게임 실행
if __name__ == "__main__":
    game = BrickBreakerGame()
    game.run()