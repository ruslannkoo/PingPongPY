import random
import tkinter
from tkinter import *
from configPing import *

flag = False
root = Tk()

root.attributes('-fullscreen', True)
root.title("Ping Pong")

c = Canvas(root, width=WIDTH, height=HEIGHT, background=BGcol)
c.pack()
c.focus_set()


p_1_text = c.create_text(WIDTH-WIDTH/6, PAD_H/4,
                         text=PLAYER_1_SCORE,
                         font="Arial 20",
                         fill="white")
p_2_text = c.create_text(WIDTH/6, PAD_H/4,
                          text=PLAYER_2_SCORE,
                          font="Arial 20",
                          fill="white")

p_3_text = c.create_text(WIDTH/2, HEIGHT - HEIGHT/1.5,
                          text="Oops... \nPress [SPACE] to continue",
                          font="Arial 40",
                          fill="white",
                          state= tkinter.HIDDEN
                         )
p_4_text = c.create_text(WIDTH/2, HEIGHT-HEIGHT/1.5,
                          text="Press [SPACE] to start",
                          font="Arial 40",
                          fill="white",

                         )
p_5_text = c.create_text(WIDTH/2, HEIGHT-HEIGHT/3,
                          text="Press [Escape] to close game",
                          font="Arial 40",
                          fill="white",
                         )

c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="black")
c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill="black")
c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill="black")


BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2,
                     HEIGHT/2-BALL_RADIUS/2,
                     WIDTH/2+BALL_RADIUS/2,
                     HEIGHT/2+BALL_RADIUS/2, fill="white")

LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill="yellow")
RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 0, WIDTH-PAD_W/2,
                          PAD_H, width=PAD_W, fill="yellow")


def move_ball():
    global flag
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center = (ball_top + ball_bot) / 2


    if ball_right + BALL_X_SPEED < right_line_distance and \
            ball_left + BALL_X_SPEED > PAD_W:

        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)


    elif ball_right == right_line_distance or ball_left == PAD_W:

        if ball_right > WIDTH / 2:

            if c.coords(RIGHT_PAD)[1] < ball_center < c.coords(RIGHT_PAD)[3]:
                bounce("strike")

            else:
                update_score("left")
                soundgo.play()
                flag = False
                c.itemconfigure(p_3_text, state="normal")
                c.itemconfigure(p_5_text, state="normal")
        else:

            if c.coords(LEFT_PAD)[1] < ball_center < c.coords(LEFT_PAD)[3]:
                bounce("strike")
            else:
                update_score("right")
                soundgo.play()
                flag = False
                c.itemconfigure(p_3_text, state="normal")
                c.itemconfigure(p_5_text, state="normal")

    else:
        if ball_right > WIDTH / 2:
            c.move(BALL, right_line_distance-ball_right, BALL_Y_SPEED)
        else:
            c.move(BALL, -ball_left+PAD_W, BALL_Y_SPEED)

    if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
        bounce("ricochet")

def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED, flag
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "space":
        c.itemconfigure(p_4_text,state = "hidden")
        if flag == False:
            spawn_ball()
    elif event.keysym == "Escape":
        flag = False
        on_closing()

    if flag == True:
        move_pads()



c.bind("<KeyPress>", movement_handler)

def move_pads():
    if flag == False:
        return

    PADS = {LEFT_PAD: LEFT_PAD_SPEED,
            RIGHT_PAD: RIGHT_PAD_SPEED}

    for pad in PADS:

        c.move(pad, 0, PADS[pad])

        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])



def spawn_ball():
    global BALL_X_SPEED
    global flag
    c.itemconfigure(p_3_text, state="hidden")
    c.itemconfigure(p_5_text, state="hidden")
    flag = True
    c.coords(BALL, WIDTH/2-BALL_RADIUS/2,
             HEIGHT/2-BALL_RADIUS/2,
             WIDTH/2+BALL_RADIUS/2,
             HEIGHT/2+BALL_RADIUS/2)

    BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED) / abs(BALL_X_SPEED)



def update_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        PLAYER_2_SCORE += 1
        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)


def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED

    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0


# Привяжем к Canvas эту функцию
c.bind("<KeyRelease>", stop_pad)



def bounce(action):
    global BALL_X_SPEED, BALL_Y_SPEED

    if action == "strike":

        sound1.play()
        BALL_Y_SPEED = random.randrange(-10, 10)
        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
            BALL_X_SPEED *= -BALL_SPEED_UP
        else:
            BALL_X_SPEED = -BALL_X_SPEED
    else:

        sound2.play()
        BALL_Y_SPEED = -BALL_Y_SPEED


def main():
    if flag == True:
        move_ball()
    root.after(30, main)

def on_closing():
    global flag
    flag = False
    print('Closing')
    soundbg.stop()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

main()
soundbg.set_volume(0.2)
soundbg.play(-1)
root.mainloop()












