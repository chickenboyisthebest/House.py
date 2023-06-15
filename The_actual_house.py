#setting up thingy m bobs
import turtle
import tkinter
import time
#import math
#import keyboard
import pyautogui
import playsound

print("Do you want me to draw you a house by using:")
print("*Turtle")
print("*Tkinter")
variable = input(">>>")

albert = turtle.Turtle()
albert.hideturtle()
wn = turtle.Screen()
albert.left(90)
canvas = turtle.getcanvas()
canvas.config(bg='dodgerblue')
albert.speed(0)

if (variable=="tkinter"):
	n_win_col = "dim gray"
	d_win_col = "dodgerblue"
	l_on = "yellow"
	
	sky_color = "day"
	room = canvas.create_rectangle(-100,100, 100, -100, fill="brown")
	
	def reset():
		albert.penup()
		albert.goto(0, 0)
		albert.pendown()
		albert.pencolor("black")
		albert.pensize(5)
		
	reset()
	
	def skyday():
		global sky_color
		canvas.config(bg='dodgerblue')
		sky_color = "day"
		
		
	def skynight():
		global sky_color
		canvas.config(bg='black')
		sky_color = "night"
		
	def sky_togl():
		global sky_color
		if sky_color == "day":
			canvas.config(bg='midnight blue')
			sky_color = "night"
			night_ground = canvas.create_rectangle(-400, 100, 400, 400, fill="dark olive green")
		else:
			canvas.config(bg='dodgerblue')
			sky_color = "day"
			day_ground = canvas.create_rectangle(-400, 100, 400, 400, fill="green")
			
		
	def window_top_left(win_col):
		return canvas.create_rectangle(-30, -30, -70, -70, fill=win_col)
		
	def window_top_right(win_col):
		return canvas.create_rectangle(30, -30, 70, -70, fill=win_col)
	
	def window_bottom_left(win_col):
		return canvas.create_rectangle(-30, 30, -70, 70, fill=win_col)
		
	def window_bottom_right(win_col):
		return canvas.create_rectangle(30, 30, 70, 70, fill=win_col)
		
		
	roof = canvas.create_polygon(100, -100, 0, -200, -100, -100, fill="brown")
	door = canvas.create_rectangle(-20, 0, 20, 100, fill="saddlebrown")
	door_knob = canvas.create_oval(-15, 50, -10, 55, fill="maroon")
	night_ground = canvas.create_rectangle(-400, 100, 400, 400, fill="maroon")
	day_ground = canvas.create_rectangle(-400, 100, 400, 400, fill="green")
	
		
	def moon():
		return canvas.create_oval(-400,-260,-360,-220,fill="light grey")
		
	def sun():
		return canvas.create_oval(-400,-260,-360,-220,fill="yellow")
		
	
	#██████╗░░█████╗░██╗░░░██╗  ███╗░░██╗██╗░██████╗░██╗░░██╗████████╗  ░█████╗░██╗░░░██╗░█████╗░██╗░░░░░███████╗
	#██╔══██╗██╔══██╗╚██╗░██╔╝  ████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝  ██╔══██╗╚██╗░██╔╝██╔══██╗██║░░░░░██╔════╝
	#██║░░██║███████║░╚████╔╝░  ██╔██╗██║██║██║░░██╗░███████║░░░██║░░░  ██║░░╚═╝░╚████╔╝░██║░░╚═╝██║░░░░░█████╗░░
	#██║░░██║██╔══██║░░╚██╔╝░░  ██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░  ██║░░██╗░░╚██╔╝░░██║░░██╗██║░░░░░██╔══╝░░
	#██████╔╝██║░░██║░░░██║░░░  ██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░  ╚█████╔╝░░░██║░░░╚█████╔╝███████╗███████╗
	#╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ░╚════╝░░░░╚═╝░░░░╚════╝░╚══════╝╚══════╝
	
	x = 1
	
	
	#day	
	win_tl = window_top_left("dodgerblue")
	win_tr = window_top_right("dodgerblue")
	win_bl = window_bottom_left("dodgerblue")
	win_br = window_bottom_right("dodgerblue")
	
	if (x==1):
		sun = sun()
	else:
		canvas.move(sun, -400, 0)
		canvas.move(moon, -400, 0)
	
	#makes the sun move
	for i in range(750):
		canvas.move(sun,1, 0)
		time.sleep(0.01)
		canvas.update()
		
	#night
	
	sky_togl()
	win_tl = window_top_left("yellow")
	win_tr = window_top_right("yellow")
	win_bl = window_bottom_left("yellow")
	win_br = window_bottom_right("yellow")
	
	moon = moon()
		
	for i in range(50):
		canvas.move(moon,1, 0)
		time.sleep(0.01)
		canvas.update()
		
	win_bl = window_bottom_left("dim gray")
	for i in range(30):
		canvas.move(moon,1, 0)
		time.sleep(0.01)
		canvas.update()
	win_br = window_bottom_right("dim gray")
	
	for i in range(60):
		canvas.move(moon,1, 0)
		time.sleep(0.01)
		canvas.update()
	
	win_tl = window_top_left("dim gray")
	for i in range(30):
		canvas.move(moon,1, 0)
		time.sleep(0.01)
		canvas.update()
	win_tr = window_top_right("dim gray")
	
	for i in range(200):
		canvas.move(moon,1, 0)
		time.sleep(0.01)
		canvas.update()
	
	#shoooting star
	shoot_star_ball = canvas.create_oval(-300, -70, -280, -60, fill = "yellow")
	#                                       #Head                 #End point
	shoot_star_tail = canvas.create_polygon(-300, -65, -280, -65, -340, -20, fill = "yellow")
	for i in range(140):
		canvas.move(moon,1, 0)
		canvas.move(shoot_star_ball,5, -5)
		canvas.move(shoot_star_tail,5, -5)
		time.sleep(0.01)
		canvas.update()
		canvas.update()
	
	for i in range(60):
		canvas.move(moon,1, 0)
		time.sleep(0.01)
		canvas.update()
	
	win_tl = window_top_left(l_on)
	for i in range(30):
		canvas.move(moon,1, 0)
		time.sleep(0.01)
		canvas.update()
	win_tr = window_top_right(l_on)
	
	for i in range(110):
		canvas.move(moon,1, 0)
		time.sleep(0.01)
		canvas.update()
		
	win_bl = window_bottom_left(l_on)
	for i in range(30):
		canvas.move(moon,1, 0)
		time.sleep(0.01)
		canvas.update()
	win_br = window_bottom_right(l_on)
	#Big word art
	print("                                                                                                             ")
	print("                                                                                                             ")
	print("                                                                                                             ")
	print("██████╗░██╗██████╗░  ██╗░░░██╗░█████╗░██╗░░░██╗  ░██████╗███████╗███████╗  ████████╗██╗░░██╗███████╗")
	print("██╔══██╗██║██╔══██╗  ╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔════╝██╔════╝  ╚══██╔══╝██║░░██║██╔════╝")
	print("██║░░██║██║██║░░██║  ░╚████╔╝░██║░░██║██║░░░██║  ╚█████╗░█████╗░░█████╗░░  ░░░██║░░░███████║█████╗░░")
	print("██║░░██║██║██║░░██║  ░░╚██╔╝░░██║░░██║██║░░░██║  ░╚═══██╗██╔══╝░░██╔══╝░░  ░░░██║░░░██╔══██║██╔══╝░░")
	print("██████╔╝██║██████╔╝  ░░░██║░░░╚█████╔╝╚██████╔╝  ██████╔╝███████╗███████╗  ░░░██║░░░██║░░██║███████╗")
	print("╚═════╝░╚═╝╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═════╝░╚══════╝╚══════╝  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝")
	print("███╗░░░███╗███████╗████████╗███████╗░█████╗░██████╗░  ░█████╗░")
	print("████╗░████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗")
	print("██╔████╔██║█████╗░░░░░██║░░░█████╗░░██║░░██║██████╔╝  ╚═╝███╔╝")
	print("██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══╝░░██║░░██║██╔══██╗  ░░░╚══╝░")
	print("██║░╚═╝░██║███████╗░░░██║░░░███████╗╚█████╔╝██║░░██║  ░░░██╗░░")
	print("╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░")
	#big word art
	meteor_spotted = input(">>>")
	if (meteor_spotted == "yes"):
		print("That's good!")
	elif (meteor_spotted == "Yes"):
		print("That's good!")
	elif (meteor_spotted == "YES"):
		print("That's good!")
	elif (meteor_spotted == "no"):
		print("Oh I'm sorry.")
	elif (meteor_spotted == "No"):
		print("Oh I'm sorry.")
	elif (meteor_spotted == "NO"):
		print("Oh I'm sorry.")
	else:
		print("Oh I'm sorry. I don't understand.")
		
	#TURTLE
elif(variable=="turtle"):
	import turtle
	import time
	import random
	wn = turtle.Screen()
	albert = turtle.Turtle()
	albert.reset()
	albert.speed(0)
	albert.lt(90)
	day = 0
	albert.hideturtle()
	
	##########Definitions##########
	
	def safegoto(x, y):
		albert.setheading(90)
		albert.penup()
		albert.goto(x, y)
		albert.pendown()
		albert.pensize(1)
		albert.pencolor("black")
	
	def wheel(x, y):
		safegoto(x, y)
		albert.fillcolor("black")
		albert.begin_fill()
		albert.circle(10)
		albert.end_fill()
		safegoto(-130, 0)
		albert.fillcolor("grey")
		albert.begin_fill()
		albert.circle(5)
		albert.end_fill()
	
	def car():
		wheel(-170, 0)
		wheel()
	
	def end():
		albert.setheading(90)
		albert.penup()
		albert.goto(0, 0)
		albert.pensize(1)
		albert.pencolor("black")
	
	def flower(x, y):
		albert.fillcolor('yellow')
		albert.pencolor('green')
		albert.penup()
		albert.goto(x, y)
		albert.pendown()
		albert.setheading(90)
		#stick
		albert.pensize(2)
		albert.setheading(-90)
		albert.fd(60)
		albert.setheading(90)
		albert.fd(90)
		#petals
		for i in range(20):
			albert.begin_fill()
			albert.forward(60 - i)
			albert.left(170)
			albert.forward(60 - i)
			albert.end_fill()
		albert.pencolor("black")
		albert.fillcolor("black")
		albert.begin_fill()
		albert.circle(5)
		albert.end_fill()
		#end	
		albert.penup()
		albert.goto(0, 0)
		albert.pendown()
		albert.setheading(90)
		albert.pencolor("black")
		albert.pensize(1)

	def sun():
		global day
		albert.penup()
		albert.goto(-100, 100)
		albert.pendown()
		albert.fillcolor("yellow")
		albert.begin_fill()
		albert.circle(30)
		albert.end_fill()
		albert.penup()
		albert.goto(0,0)
		albert.pendown()
		
	def moon():
		global day
		albert.penup()
		albert.goto(-100, 100)
		albert.pendown()
		albert.fillcolor("gray")
		albert.begin_fill()
		albert.circle(30)
		albert.end_fill()
		albert.penup()
		albert.goto(0,0)
		albert.pendown()
	
	def make_ground():
		albert.fillcolor("brown")
		albert.begin_fill()
		albert.right(90)
		albert.fd(400)
		albert.right(90)
		albert.fd(400)
		albert.right(90)
		albert.fd(800)
		albert.right(90)
		albert.fd(400)
		albert.end_fill()
		albert.right(90)
		albert.fd(400)
		albert.left(90)
	
	def house_outline():
		albert.fillcolor("red")
		albert.begin_fill()
		albert.right(90)
		albert.fd(150)
		albert.left(90)
		albert.fd(150)
		albert.left(45)
		albert.fd(150)
		albert.left(90)
		albert.fd(150)
		albert.left(45)
		albert.fd(150)
		albert.left(90)
		albert.fd(150)
		albert.left(90)
		albert.end_fill()
		#Start home down tabbing here
		albert.penup()
		albert.goto(0, 0)
		albert.pendown
		
	def square():
		albert.begin_fill()
		for i in range(4):
			albert.fd(30)
			albert.lt(90)
			i=i+1
		albert.end_fill()
	
	def windows(on):
		if on == 1:
			albert.fillcolor("yellow")
			sky_night()
		else:
			albert.fillcolor("lightblue")
			sky_day()
		albert.penup()
		albert.goto(0,30)
		albert.pendown()
		square()
		albert.penup()
		albert.goto(0,90)
		albert.pendown()
		square()
		albert.penup()
		albert.goto(120,30)
		albert.pendown()
		square()
		albert.penup()
		albert.goto(120,90)
		albert.pendown()
		square()
		albert.penup()
		albert.goto(0, 0)
		albert.pendown()
	
	def sky_day():
		global day
		wn.bgcolor("lightblue")
		sun()
		day = 1
	
	def sky_night():
		global day
		wn.bgcolor("black")
		moon()
		day = 1
		
	def sky_togl():
		global day
		if day == 1:
			sky_night()
			moon()
			day = 0
		else:
			sky_day()
			sun()
			day = 1
			
	def window_right_color():
		global day
		if day ==1:
			windows(0)
		else:
			windows(1)
			
	def day_night_cycle():
		global day
		for i in range(10):
			day = 1
			time.sleep(5)
			day = 0
			time.sleep(5)
			window_right_color()
			sky_togl()
			i = i+1
			
	def door():
		albert.fillcolor("blue")
		albert.penup()
		albert.goto(30,0)
		albert.pendown()
		albert.begin_fill()
		albert.right(90)
		albert.fd(40)
		albert.left(90)
		albert.fd(90)
		albert.left(90)
		albert.fd(40)
		albert.left(90)
		albert.fd(90)
		albert.left(180)
		albert.end_fill()
		albert.penup()
		albert.goto(43,40)
		albert.pendown()
		albert.fillcolor("yellow")
		albert.begin_fill()
		albert.circle(5)
		albert.end_fill()
		albert.penup()
		albert.goto(0, 0)
		albert.pendown()
		
	def albert_code():
		make_ground()
		house_outline()
		door()
		sky_day()
		window_right_color()
		day_night_cycle()
	
	##########Definitions###########
	
	make_ground()
	flower(200, 60)
	sun()
	house_outline()
	door()
	sky_day()
	window_right_color()
	pyautogui.screenshot('Turtle.png')
	pyautogui.screenshot('Turtle.png')
	import sys
	sys.exit()
else:
	playsound.playsound("rick.mp3", True)
playsound.playsound("crazy.mp3", True)
