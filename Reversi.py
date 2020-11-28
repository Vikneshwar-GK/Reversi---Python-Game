import time
import random
from graphics import *
box=[]
message=0
win=0
li=[]
top=[]
graphics_choice=[]
x_pts=0
o_pts=0
possible_choice=[]
xo=[[27,36],[28,35]]
chance_X=0
chance_O=0
player_no=2
mark=0
difficult=-1
box_color=[["white","yellow","light green","grey"],["red","dark blue","blue","yellow"],["grey","red","orange","yellow"],["brown","dark grey","light grey","brown"],["red","light blue","light green","dark grey"]]
bg_color=[["black","yellow","light green",color_rgb(255,149,98)],["light blue","dark blue","violet","blue"],["light green","brown","red","green"],[color_rgb(225,160,66),"blue","brown","red"],["white","black","red","black"]]
bg_col_no=0
box_col_no=0
bor_left=0
bor_right=0
bor_top=0
bor_down=0		

col=[["black","white","yellow","light green"],["blue","red","dark blue","blue"],["green","grey","red","orange"],["violet","brown","dark grey","light grey"],[color_rgb(184,204,228),"red","light blue","light green"]]
col1=['grey','yellow','yellow',"brown","dark grey"]

def graphics_main():
	global win
	win=GraphWin("REVERSI",750,600)
	
	def graphics_control():
		win.close()
		graphics_main()

	def initializer():
		global box
		global li
		global top
		global graphics_choice
		global x_pts
		global o_pts
		global possible_choice
		global xo
		global chance_X
		global chance_O
		global player_mode
		#global mark
		#mark=0
		win=0
		box=[]
		li=[]
		top=[]		
		graphics_choice=[]
		x_pts=0	
		o_pts=0
		possible_choice=[]
		xo=[[27,36],[28,35]]
		chance_X=0
		chance_O=0
		player_mode=[]

	def display_winner():
		global xo
		global player_no

		if(player_no==2):
			s1="WHITE WON!!"
			s2="BLACK WON!!"
		elif(player_no==1):
			s1="YOU WON!!"
			s2="YOU LOST!!"
		rect=Oval(Point(220,200),Point(520,350))
		#rect1=Oval(Point(230,210),Point(510,340))
		rect.setOutline("orange")
		rect.setWidth(5)
		rect.setFill("white")
		#rect1.setFill("orange")
		if(len(xo[0])>len(xo[1])):
			winner=Text(Point(370,275),s2)
		elif(len(xo[0])<len(xo[1])):
			winner=Text(Point(370,275),s1)
		else:
			winner=Text(Point(370,275),"MATCH DRAW")
		
		rect.draw(win)
		winner.setTextColor("Red")
		winner.setFace("courier")
		winner.setStyle("bold italic")
		winner.setSize(25)
		winner.draw(win)
		win.getMouse()

	def display_possible_choice_color(pos):
		global win
		global graphics_choice
		global box
		global box_col_no
		global box_color
		cen1=box[pos].getCenter()
		cir=Circle(cen1,3)
		graphics_choice.append(cir)
		graphics_choice[-1].setFill(box_color[box_col_no][3])
		graphics_choice[-1].setOutline(box_color[box_col_no][3])
		graphics_choice[-1].draw(win)
	
	def display_color(pos,num):
		global box
		if(num==0):
			color='black'
		else:
			color='white'
		cen1=box[pos].getCenter()
		cir=Circle(cen1,18)
		cir.setFill(color)
		cir.draw(win)
	
	def help_box():
		win1=GraphWin("HELP",700,690)
		win1.setBackground(color_rgb(184,204,228))
		msg=Image(Point(350,325),"Images/help_box1.png")
		msg.draw(win1)
	
	def color_change():
		global box
		global graphics_choice
		global box_color
		global box_col_no

		box_col_no=(box_col_no+1)%5
		n=0
		k=0
		for i in graphics_choice:
			i.setFill(box_color[box_col_no][3])
			i.setOutline(box_color[box_col_no][3])
		for i in range(8):
			for j in range(8):
				box[n].setOutline(box_color[box_col_no][0])
				box[n].setWidth(1)
				if(k==0):
					box[n].setFill(box_color[box_col_no][1])
					k=1
				else:
					box[n].setFill(box_color[box_col_no][2])
					k=0
				n+=1
			if(k==0):
				k=1
			else:
				k=0
	
	def display_detail():
		global player_no

		if(player_no==2):
			s1="WHITE"
			s2="BLACK"
		elif(player_no==1):
			s1="YOU"
			s2="COMPUTER"

		rec1=Rectangle(Point(35,255),Point(145,280))
		rec1.setOutline("black")
		rec1.setFill("white")
		rec1.draw(win)
		rec2=Rectangle(Point(585,255),Point(695,280))
		rec2.setOutline("black")
		rec2.setFill("white")
		rec2.draw(win)
		
		try1=Polygon(Point(80,255),Point(100,255),Point(90,240))
		try1.setFill("light grey")
		try1.setOutline("black")
		try2=Polygon(Point(630,255),Point(650,255),Point(640,240))
		try2.setFill("light grey")
		try2.setOutline("black")

		txt1=Text(Point(90,267),s1)
		txt1.setFace("arial")
		txt1.setStyle("bold italic")
		txt2=Text(Point(640,267),s2)
		txt2.setFace("arial")			
		txt2.setStyle("bold italic")

		try1.draw(win)
		try2.draw(win)
		txt1.draw(win)
		txt2.draw(win)

		time.sleep(1)
		rec1.undraw()
		rec2.undraw()
		try1.undraw()
		try2.undraw()
		txt1.undraw()
		txt2.undraw()

	def bg_color():
		global x_pts
		global o_pts
		global chance_X
		global chance_O
		global message
		global bg_color
		global bg_col_no
		global bor_left
		global bor_right
		global bor_top
		global bor_down		
		
		bg_col_no=(bg_col_no+1)%5
		win.setBackground(bg_color[bg_col_no][0])
		chance_X.setOutline(bg_color[bg_col_no][1])
		chance_O.setOutline(bg_color[bg_col_no][1])
		x_pts.setTextColor(bg_color[bg_col_no][1])
		o_pts.setTextColor(bg_color[bg_col_no][1])
		message.setTextColor(bg_color[bg_col_no][2])		
		bor_down.setFill(bg_color[bg_col_no][3])
		bor_top.setFill(bg_color[bg_col_no][3])
		bor_right.setFill(bg_color[bg_col_no][3])
		bor_left.setFill(bg_color[bg_col_no][3])
		bor_down.setOutline(bg_color[bg_col_no][3])
		bor_top.setOutline(bg_color[bg_col_no][3])
		bor_right.setOutline(bg_color[bg_col_no][3])
		bor_left.setOutline(bg_color[bg_col_no][3])

	def check_box(clickPoint):
		global box
		global win
		global possible_choice
		global player_no
		global player_mode
		global difficult
		x=clickPoint.getX()
		y=clickPoint.getY()
		if(x>40 and y>530 and x<105 and y<590): #and player_no==2):
			#player_no=1
			n=game_mode()
			if(n!=1):
				graphics_control()
			return(-1)
		elif(x>165 and y>530 and x<230 and y<590 and player_no==1):
			player_no=2
			difficult=-1
			graphics_control()
		elif(x>280 and y>530 and x<345 and y<590):
			help_box()
			return(-1)
		elif(x>405 and y>530 and x<470 and y<590):
			bg_color()
			return(-1)
		elif(x>525 and y>530 and x<590 and y<590):
			graphics_control()
		elif(x>645 and y>530 and x<710 and y<590):
			win.close()
			exit(0)
		
		elif((x>35 and y>145 and x<145 and y<255) or (x>585 and y>145 and x<695 and y<255 )):
			display_detail()
			return(-1)
		else:
			for i in range(64):
				cornerPoint1 = box[i].getP1()
				cornerPoint2 = box[i].getP2()
				x1=cornerPoint1.getX()
				y1=cornerPoint1.getY()
				x2=cornerPoint2.getX()
				y2=cornerPoint2.getY()
				if(x>x1 and y>y1 and x<x2 and y<y2):
					break		
			if(i in possible_choice):
				return(i)
			elif(x>210 and y>160 and x<530 and y<480):
				color_change()
				return(-1)
			else:
				return(-1)

	def game_mode():
		global difficult
		global player_no
		rect=Rectangle(Point(40,400),Point(110,520))
		rect.setFill("white")
		rect.setOutline("white")
		diff=[0,0,0]
		diff[0]=Text(Point(75,415),"EASY")#40 400 110 435
		diff[1]=Text(Point(75,455),"MEDIUM")#40 435 110 475
		diff[2]=Text(Point(75,500),"HARD")#40 475 110 515
		while(1):
			rect.draw(win)
			if(difficult!=-1):
				diff[difficult].setFill("yellow")
			diff[0].draw(win)
			diff[1].draw(win)
			diff[2].draw(win)
			clickPoint=win.getMouse()
			x=clickPoint.getX()
			y=clickPoint.getY()
			rect.undraw()
			diff[0].undraw()
			diff[1].undraw()
			diff[2].undraw()
			if(x>40 and y>400 and x<110 and y<435 and difficult!=0):
				difficult=0
				player_no=1
				return -1
			elif(x>40 and y>435 and x<110 and y<475 and difficult!=1):
				difficult=1
				player_no=1
				return -1
			elif(x>40 and y>475 and x<110 and y<515 and difficult!=2):
				difficult=2
				player_no=1
				return -1			
			elif(x>40 and y>530 and x<105 and y<590):
				return 1

	def main_box():
		global win
		
		global box
		#global player_mode
		global player_no
		global box_color
		global box_col_no
		global x_pts
		global o_pts
		global chance_X
		global chance_O
		global message
		global bg_color
		global bg_col_no
		global bor_left
		global bor_right
		global bor_top
		global bor_down		
		win.setBackground(bg_color[bg_col_no][0])

		k=0
		for i in range(64):
			box.append(0)
		for i in range(8):
			for j in range(8):
				box[k]=Rectangle(Point(210+(40*j),160+(40*i)),Point(250+(40*j),200+(40*i)))
				k+=1
		
		cir1=Circle(Point(90,200),55)
		cir2=Circle(Point(640,200),55)
		x_msg=Image(Point(90,200),"Images/player_1.png")
		o_msg=Image(Point(640,200),"Images/player_2.png")
		cir1.setFill("white")
		cir2.setFill("white")
		cir2.draw(win)
		cir1.draw(win)
		x_msg.draw(win)
		o_msg.draw(win)

		x_pts=Text(Point(90,300),len(xo[0]))
		o_pts=Text(Point(640,300),len(xo[1]))
		x_pts.setSize(18)
		o_pts.setSize(18)
		x_pts.setStyle("bold italic")
		o_pts.setStyle("bold italic")
		x_pts.setTextColor(bg_color[bg_col_no][1])
		o_pts.setTextColor(bg_color[bg_col_no][1])
		x_pts.draw(win)
		o_pts.draw(win)
		chance_X=Circle(Point(90,200),47)
		chance_O=Circle(Point(640,200),47)
		chance_X.setOutline(bg_color[bg_col_no][1])
		chance_O.setOutline(bg_color[bg_col_no][1])
		chance_X.setWidth(3)
		chance_O.setWidth(3)

		k=0
		n=0
		message = Text(Point(370,90), "R~E~V~E~R~S~I")
		message.setSize(30)
		message.setStyle("bold italic")
		message.setFace("courier")
		message.setTextColor(bg_color[bg_col_no][2])
		message.draw(win)
		for i in range(8):
			for j in range(8):
				box[n].setOutline(box_color[box_col_no][0])
				box[n].setWidth(1)
				if(k==0):
					box[n].setFill(box_color[box_col_no][1])
					k=1
				else:
					box[n].setFill(box_color[box_col_no][2])
					k=0
				box[n].draw(win)
				n+=1
			if(k==0):
				k=1
			else:
				k=0
			display_color(27,0)
			display_color(36,0)
			display_color(28,1)
			display_color(35,1)

			line=Line(Point(0,520),Point(750,520))
			line.setOutline('black')
			line.setWidth(2)
			
			rect=Rectangle(Point(0,520),Point(750,600))
			rect.setFill("white")
			rect.setOutline("white")
			rect.draw(win)
			coll=color_rgb(255,149,98)
			
			bor_left=Rectangle(Point(0,0),Point(15,520))
			bor_top=Rectangle(Point(0,0),Point(750,15))
			bor_right=Rectangle(Point(735,0),Point(750,520))
			bor_down=Rectangle(Point(0,505),Point(750,520))
			
			bor_left.setOutline(coll)
			bor_top.setOutline(coll)
			bor_right.setOutline(coll)
			bor_down.setOutline(coll)
			
			bor_left.setFill(coll)
			bor_top.setFill(coll)
			bor_right.setFill(coll)
			bor_down.setFill(coll)
			
			bor_left.draw(win)
			bor_top.draw(win)
			bor_right.draw(win)
			bor_down.draw(win)

			img1=Image(Point(75,560),"Images/single_player.png") #40,530 105,590
			img2=Image(Point(195,560),"Images/dual_player.png")  #220=190,530 255,590
			img3=Image(Point(315,560),"Images/help.png")	      #375=340,530 405,590
			img4=Image(Point(435,560),"Images/change.png")	      #530=500,530 565,590
			img5=Image(Point(555,560),"Images/refresh.png")	  #660=630,530 695,590
			img6=Image(Point(675,560),"Images/exit.png")

			img1.draw(win)	
			img2.draw(win)
			img3.draw(win)
			img4.draw(win)
			img5.draw(win)
			img6.draw(win)

			player_mode_2=Circle(Point(195,562),37)
			player_mode_2.setOutline("grey")
			player_mode_2.setWidth(2)
			#player_mode[-1].draw(win)
			
			player_mode_1=Circle(Point(75,562),37)
			player_mode_1.setOutline("grey")
			player_mode_1.setWidth(2)
			if(player_no==2):
				player_mode_2.draw(win)
				player_mode_1.undraw()
				
			elif(player_no==1):
				player_mode_2.undraw()
				player_mode_1.draw(win)
		#display_winner()		
	
	class Node:
		def __init__(self,value):
			self.value=value
			self.next=None

	class List:
		def __init__(self):
			self.head=None
		def push(self,value):
			newnode=Node(value)
			if(self.head==None):
				self.head=newnode
			else:
				newnode.next=self.head
				self.head=newnode
		def pop(self):
			if(self.head!=None):
				temp=self.head.value
				self.head=self.head.next
				return(temp)
			else:
				return(None)
		def length(self):
			temp=self.head
			l=0
			while(temp!=None):
				l+=1
				temp=temp.next
			return(l)

	def change_pts():
		global xo
		global x_pts
		global o_pts
		x_pts.setText(len(xo[1]))
		o_pts.setText(len(xo[0]))
		
	def one_player(num):
		global possible_choice
		global top
		global difficult
		choice=0
		m=0
		li1=[]
		dic={}
		for  i in possible_choice:
			k=top[i].length()
			dic[k]=i
			li1.append(k)
		li1.sort()
		if(difficult!=1):	
			if(len(li1)>2):
				if(difficult==0):
					m=li1[1]
				elif(difficult==2):
					m=li1[-1]
			else:
				if(difficult==0):
					m=li1[0]
				elif(difficult==2):
					m=li1[-1]
			choice=dic[m]
		else:
			choice=random.choice(possible_choice)
		change_form(choice,num)

	def change_form(choice,num):
		global possible_choice
		global top
		global xo
		while(True):
			value=top[choice].pop()
			if(value==None):
				break
			else:
				display_color(value,num)
				t=0.15
				time.sleep(t)
				if(value not in xo[num]):
					xo[num].append(value)
				if(value in xo[1-num]):
					xo[1-num].remove(value)
				change_pts()
		refill_me()
		
	def refill_me():
		global top
		global graphics_choice
		for i in range(64):
			top[i]=List()
		for i in graphics_choice:
			i.undraw()

	def fill_me():
		global top
		for i in range(64):
			top.append(0)	

	def linked_list(test_li,value):
		global top
		for i in test_li:
			top[value].push(i)

	def input_choice(num):
		global win
		global possible_choice
		global chance_X
		global chance_O
		if(num==1):
			chance_X.draw(win)
			chance_O.undraw()
		elif(num==0):
			chance_X.undraw()
			chance_O.draw(win)
		if(len(possible_choice)==0):
			return(0)			
		else:
			if(player_no==2):
				while(1):
					clickPoint = win.getMouse()
					choice=check_box(clickPoint)
					if(choice!=-1):
						change_form(choice,num)
						break
			elif(player_no==1):
				if(num!=0):
					while(1):
						clickPoint = win.getMouse()
						choice=check_box(clickPoint)
						if(choice!=-1):
							change_form(choice,num)
							break
				else:
					one_player(num)
			
	def find_possibility(num):
		global possible_choice
		global xo
		possible_choice=[]
		for i in xo[num]:
			xcord=i//8
			ycord=i%8
			
			for j in range(8):
				if(j==0):
					diff=-8
					limit=xcord
				elif(j==1):
					diff=-7
					if(xcord==0 or ycord==7):
						limit=0
					else:
						limit=8
				elif(j==2):
					diff=1
					limit=7-ycord
				elif(j==3):
					diff=9
					if(xcord==7 or ycord==7):
						limit=0
					else:
						limit=8
				elif(j==4):
					diff=8
					limit=7-xcord
				elif(j==5):
					diff=7
					if(xcord==7 or ycord==0):
						limit=0
					else:
						limit=8
				elif(j==6):
					diff=-1
					limit=ycord
				else:
					diff=-9
					if(xcord==0 or ycord==0):
						limit=0
					else:
						limit=8
				value=i
				signal=0
				test_li=[]

				for k in range(limit):
					value+=diff
					test_li.append(value)
					xcord1=value//8
					ycord1=value%8
					if(j in [1,3,5,7] and (xcord1==0 or ycord1==0 or xcord1==7 or ycord1==7)):
						if(li[xcord1][ycord1]=='_' and signal==1):
							signal=2
						break	
					if(value in xo[num]):
						break
					elif(value in xo[1-num]):
						signal=1
					elif(li[xcord1][ycord1]=='_'):
						if(signal==1):
							signal=2
						break
				
				if(signal==2):
					linked_list(test_li,value)
					possible_choice.append(value)
					if(player_no==1 and num!=0):
						display_possible_choice_color(value)
					elif(player_no==2):
						display_possible_choice_color(value)
					
	def display():
		global xo
		global li
		temp=[]
		for i in range(8):
			for j in range(8):
				temp.append("_")
			li.append(temp)
			temp=[]
		for i in xo[0]:
			xcord=i//8
			ycord=i%8
			li[xcord][ycord]='X'
		for i in xo[1]:
			xcord=i//8
			ycord=i%8
			li[xcord][ycord]='O'

	def function_caller():
		display()
		fill_me()
		refill_me()
		num=0
		global xo
		for i in range(60):	
			if(num==0):
				num=1
			else:
				num=0
			find_possibility(num)
			input_choice(num)
			display()
			if(player_no==1):
				if(i%2==0):	
					t=1
					time.sleep(t)

		display_winner()
		graphics_control()
	
	initializer()
	main_box()
	function_caller()

def opening_screen():
	win2=GraphWin("REVERSI",750,600)
	win2.setBackground("black")
	line=[]
	k1=0
	st1="WeLcOmE To ReVeRsI"
	l1=0
	txt1=Text(Point(380,100),st1[0:l1])
	txt1.setTextColor(color_rgb(225,225,60))
	txt1.setSize(30)
	txt1.setStyle("bold italic")
	txt1.setFace("courier")
	txt1.draw(win2)
	rect1=Rectangle(Point(255,200),Point(495,440))
	rect1.setOutline("white")
	k=0
	box1=[]
	l=[]
	load=0
	n=0
	txt=Text(Point(375,525),load)
	t1=Text(Point(403,525),"%")
	rect=Rectangle(Point(125,500),Point(625,550))
	rect.setOutline("grey")
	rect.draw(win2)
	txt.setTextColor("red")
	t1.setTextColor("red")
	txt.draw(win2)
	t1.draw(win2)
	m=-1
	cirr=[]
	coll="brown"
	bor_left=Rectangle(Point(0,0),Point(20,600))
	bor_top=Rectangle(Point(0,0),Point(750,20))
	bor_right=Rectangle(Point(730,0),Point(750,600))
	bor_down=Rectangle(Point(0,580),Point(750,600))
	bor_left.setOutline(coll)
	bor_top.setOutline(coll)
	bor_right.setOutline(coll)
	bor_down.setOutline(coll)
	bor_left.setFill(coll)
	bor_top.setFill(coll)
	bor_right.setFill(coll)
	bor_down.setFill(coll)
	bor_left.draw(win2)
	bor_top.draw(win2)
	bor_right.draw(win2)
	bor_down.draw(win2)
	time.sleep(1.5)
	for i in range(500):
		if(i%28==0):
			if(l1<=len(st1)):
				l1+=1
				txt1.setText(st1[0:l1])
			
		if(i%5==0):
			m+=1
			if(m<9):
				line.append(Line(Point(255+m*30,200),Point(255+m*30,440)))
				line[-1].setOutline("red")
				line[-1].draw(win2)
			if(m>=9 and m<18):
				line.append(Line(Point(255,200+(m-9)*30),Point(495,200+(m-9)*30)))
				line[-1].setOutline("red")
				line[-1].draw(win2)
			if(m==18):
				for i1 in range(64):
					box1.append(0)
				for i1 in range(8):
					for j in range(8):
						box1[k]=Rectangle(Point(255+(30*j),200+(30*i1)),Point(285+(30*j),230+(30*i1)))
						box1[k].setOutline("red")
						box1[k].draw(win2)
						k+=1
			if(m>18 and m<83):
				if(n%8==0 and k1==0):
					k1=1
				elif(n%8==0 and k1==1):
					k1=0			
				box1[m-19].setOutline("red")
				box1[m-19].setWidth(1)
				if(k1==0):
					box1[m-19].setFill("light green")
					k1=1
				else:
					box1[m-19].setFill("yellow")
					k1=0
				n+=1
			if(m==84):
				cirr.append(Circle(Point(360,305),13))
				cirr[-1].setFill("black")
				cirr[-1].draw(win2)
			if(m==86):
				cirr.append(Circle(Point(390,305),13))
				cirr[-1].setFill("white")
				cirr[-1].draw(win2)
			if(m==85):
				cirr.append(Circle(Point(390,335),13))
				cirr[-1].setFill("black")
				cirr[-1].draw(win2)
			if(m==87):
				cirr.append(Circle(Point(360,335),13))
				cirr[-1].setFill("white")
				cirr[-1].draw(win2)
		txt.undraw()
		t1.undraw()
		l.append(Line(Point(125+i,500),Point(125+i,550)))
		#if(i%5==0):
		l[-1].setOutline("white")
		l[-1].draw(win2)
		if(i%5==0):
			load+=1
		txt=Text(Point(375,525),load)
		t1=Text(Point(403,525),"%")
		txt.setTextColor("red")
		txt.setSize(16)
		txt.setStyle("bold italic")
		txt.draw(win2)
		t1.setTextColor("red")
		t1.setSize(16)
		t1.setStyle("bold italic")
		t1.draw(win2)	
		time.sleep(0.01)
	time.sleep(1)
	rect2=[]
	for i in range(0,601,5):
		rect2.append(Rectangle(Point(0,0),Point(750,i)))
		rect2[-1].setOutline(color_rgb(50,0,0))
		rect2[-1].setFill(color_rgb(50,0,0))
		rect2[-1].draw(win2)
		time.sleep(0.01)
	time.sleep(0.5)
	win2.close()
	graphics_main()
opening_screen()
#graphics_main()