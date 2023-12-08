import tkinter as tk
import turtle
import random

# tkinter 윈도우 생성
root = tk.Tk()
root.geometry("600x600")
root.configure(bg='black')

# turtle 캔버스 생성
canvas = tk.Canvas(root, width=600, height=600, bg='black')
canvas.pack()

# turtle 스크린 생성
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("black")

# 배경색 설정
turtle.bgcolor('black')

# 눈사람 그리기 함수
def draw_snowman():
    # 몸통 그리기
    body = turtle.Turtle()
    body.penup()
    body.goto(0, -150)
    body.pendown()
    body.begin_fill()
    body.color("white")
    body.circle(100)
    body.end_fill()

    # 머리 그리기
    head = turtle.Turtle()
    head.penup()
    head.goto(0, 30)
    head.pendown()
    head.begin_fill()
    head.color("white")
    head.circle(70)
    head.end_fill()

    # 눈 그리기
    left_eye = turtle.Turtle()
    left_eye.penup()
    left_eye.goto(-30, 100)
    left_eye.pendown()
    left_eye.begin_fill()
    left_eye.color("black")
    left_eye.circle(10)
    left_eye.end_fill()

    right_eye = turtle.Turtle()
    right_eye.penup()
    right_eye.goto(30, 100)
    right_eye.pendown()
    right_eye.begin_fill()
    right_eye.color("black")
    right_eye.circle(10)
    right_eye.end_fill()

    # 당근 그리기
    carrot = turtle.Turtle()
    carrot.penup()
    carrot.goto(0, 75)
    carrot.pendown()
    carrot.color("orange")
    carrot.begin_fill()
    carrot.goto(0, 105)
    carrot.goto(40, 85)
    carrot.goto(0, 75)
    carrot.end_fill()

    # 입 그리기
    smile = turtle.Turtle()
    smile.penup()
    smile.goto(-5, 45)
    smile.pendown()
    smile.width(10)
    smile.color("black")
    smile.circle(60, 45)

    # 팔 그리기
    right_arm = turtle.Turtle()
    right_arm.penup()
    right_arm.goto(75, -10)
    right_arm.width(8)
    right_arm.pendown()
    right_arm.pencolor("#a52a2a") # 갈색
    right_arm.goto(110, -10)

    left_arm = turtle.Turtle()
    left_arm.penup()
    left_arm.goto(-75, -10)
    left_arm.width(8)
    left_arm.pendown()
    left_arm.pencolor("#a52a2a") # 갈색
    left_arm.goto(-110, -10)

    # 바닥 그리기
    Ground = turtle.Turtle()
    Ground.penup()
    Ground.goto( 300,-140)
    Ground.width(10)
    Ground.pendown()
    Ground.begin_fill()
    Ground.color("white")
    Ground.goto(-300, -148)
    Ground.goto(-300, -250)
    Ground.goto( 300, -250)
    Ground.goto( 300, -140)
    Ground.end_fill()

# 눈 그리기 함수
def draw_snow():
    snow = turtle.Turtle()
    snow.hideturtle()
    snow.penup()
    x = random.randint(-300, 300)
    y = random.randint(  50, 300)
    snow.goto(x, y)
    snow.pendown()
    snow.color("white")
    snow.begin_fill()
    snow.circle(3)
    snow.end_fill()

# 윈도우 창 설정
turtle.setup(width=600, height=600)

# 눈사람 그리기
draw_snowman()

# 눈 내리는 효과 추가
cnt = 1
while True:
    draw_snow()
    cnt = cnt + 1
    turtle.delay(20)
    if cnt > 15 :
        break

# "Have a happy Christmas" 텍스트 추가
text = turtle.Turtle()
text.penup()
text.goto(-200, -200)
text.color('orange')
text.write("Happy Merry Holly Jolly Christmas", font=("Arial", 20, "bold"))
text.goto(-200, -230)
text.write("And Happy New Year ♥", font=("Arial", 20, "bold"))
# 그리기 완료 후 종료하기
turtle.done()
