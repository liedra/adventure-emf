### Author: @liedra
### Description: A short adventure in which you may wish to kick orcs.
### Category: Games
### License: MIT
### reboot-before-run: True
### Appname : Adventure! 

#this code is really ugly, I'm not a good progammer, I'm sorry
 
import ugfx
import buttons
import pyb
 
ugfx.init()
buttons.init()
bz=pyb.Pin(pyb.Pin.cpu.D12, pyb.Pin.OUT_PP) # music comes from here
buttons.enable_menu_reset()

room = 1

haskey1=0
haskey2=0
hp=50
orc1=10
orc2=10
orc3=20
btn_a_presses=0


	
def setup_right_menu():
	ugfx.set_default_font(ugfx.FONT_SMALL)

	if room==1:
		if (haskey1==0):
			ugfx.text(190, 30, "The gate is locked.", ugfx.RED)
			ugfx.text(190, 50, "Maybe you should ", ugfx.RED)
			ugfx.text(190, 70, "find a key.", ugfx.RED)
		elif (haskey1==1):
			ugfx.text(190, 30, "The key fits the lock!", ugfx.RED)
			ugfx.text(190, 50, "A: Escape the Castle", ugfx.RED)
			
	if room==2:
		if orc1:
			ugfx.text(190, 30, "An orc is here.", ugfx.RED)
			ugfx.text(190, 50, "A: Kick", ugfx.RED)
			ugfx.text(190, 70, "B: Punch", ugfx.RED)
			
	if room==5:
		if orc2:
			ugfx.text(190, 30, "A slightly bigger", ugfx.RED) 
			ugfx.text(190, 50, "orc is here.", ugfx.RED)
			ugfx.text(190, 70, "A: Kick", ugfx.RED)
			ugfx.text(190, 90, "B: Tell it a joke", ugfx.RED)
	if room==6:
		ugfx.text(190, 30, "A fountain", ugfx.RED) 
		ugfx.text(190, 50, "is here.", ugfx.RED)
		ugfx.text(190, 70, "A: Drink", ugfx.RED)
		ugfx.text(190, 90, "B: Look in", ugfx.RED)
		
	if room==8:
		if orc3:
			ugfx.text(190, 30, "A humongous", ugfx.RED) 
			ugfx.text(190, 50, "orc is here.", ugfx.RED)
			ugfx.text(190, 70, "A: Kick", ugfx.RED)
			ugfx.text(190, 90, "B: Sneak past", ugfx.RED)
			
			
	if room==9:
		ugfx.text(190, 30, "A key is here.", ugfx.RED)
		ugfx.text(190, 50, "A: Take", ugfx.RED)
		ugfx.text(190, 70, "B: Eat", ugfx.RED)
		
	ugfx.text(30, 200, "HP: "+str(hp), ugfx.BLUE)

def build_room_walls(north, east, south, west):
	#0 closed 1 open
	if north==0:
		ugfx.thickline(6,30,183,30,ugfx.WHITE,7,0)
	if north==1:
		ugfx.thickline(6,30,90,30,ugfx.WHITE,7,0)
		ugfx.thickline(110,30,183,30,ugfx.WHITE,7,0)
	if east==0:
		ugfx.thickline(180,30,180,180,ugfx.WHITE,7,0)
	if east==1:
		ugfx.thickline(180,27,180,100,ugfx.WHITE,7,0)
		ugfx.thickline(180,120,180,180,ugfx.WHITE,7,0)	
	if south==0:
		ugfx.thickline(6,180,183,180,ugfx.WHITE,7,0)
	if south==1:
		ugfx.thickline(10,176,90,176,ugfx.WHITE,7,0)
		ugfx.thickline(110,176,180,176,ugfx.WHITE,7,0)
	if west==0:
		ugfx.thickline(10,30,10,180,ugfx.WHITE,7,0)
	if west==1:
		ugfx.thickline(10,27,10,100,ugfx.WHITE,7,0)
		ugfx.thickline(10,120,10,180,ugfx.WHITE,7,0)
				
			

def room_1():
	### Room 1 - exit north
	room=1
	
	ugfx.clear(ugfx.BLACK)
	setup_right_menu()
	
	build_room_walls(1,0,0,0)

	
	#corridor N
	ugfx.thickline(90,34,90,0,ugfx.WHITE,7,0)
	ugfx.thickline(110,34,110,0,ugfx.WHITE,7,0)

	#door
	ugfx.thickline(90,180,110,180,ugfx.BLUE,7,0)
	#PC
	ugfx.fill_circle(100,150,5,ugfx.YELLOW)
	
	
def room_2():
	###Room 2 - exits south, west, east
	room=2
	
	ugfx.clear(ugfx.BLACK)
	setup_right_menu()
	build_room_walls(0,1,1,1)
	

	ugfx.fill_circle(100,150,5,ugfx.YELLOW)
	if orc1>0:
		ugfx.fill_circle(130,70,10,ugfx.GREEN)
	else:
		ugfx.fill_circle(130,70,10,ugfx.RED)

def room_3():
	###Room 3 - exits north, east
	room=3
	ugfx.clear(ugfx.BLACK)
	setup_right_menu()
	build_room_walls(1,1,0,0)
	ugfx.fill_circle(100,150,5,ugfx.YELLOW)

def room_4():
	###Room 4 - exits west
	room=4
	print ("here")
	ugfx.clear(ugfx.BLACK)
	setup_right_menu()
	build_room_walls(0,0,0,1)
	ugfx.fill_circle(100,150,5,ugfx.YELLOW)
	
def room_5():
	###Room 5 - exits ES
	room=5
	global btn_a_presses
	btn_a_presses=0
	ugfx.clear(ugfx.BLACK)
	setup_right_menu()
	build_room_walls(0,1,1,0)
	ugfx.fill_circle(100,150,5,ugfx.YELLOW)
	if orc2>0:
		ugfx.fill_circle(70,70,10,ugfx.GREEN)
	else:
		ugfx.fill_circle(70,70,10,ugfx.RED)

def room_6():
	###Room 6 - exits EW
	room=6
	ugfx.clear(ugfx.BLACK)
	setup_right_menu()
	build_room_walls(0,1,0,1)
	ugfx.area(90,100,20,20,ugfx.BLUE)
	
	ugfx.fill_circle(80,100,5,ugfx.YELLOW)
	

def room_7():
	###Room 7 - exits EW
	room=7
	ugfx.clear(ugfx.BLACK)
	setup_right_menu()
	build_room_walls(0,1,0,1)	
	ugfx.fill_circle(100,150,5,ugfx.YELLOW)
	

def room_8():
	###Room 8 - exits WS
	global btn_a_presses
	btn_a_presses=0
	room=8
	ugfx.clear(ugfx.BLACK)
	setup_right_menu()
	build_room_walls(0,0,1,1)
	ugfx.fill_circle(100,150,5,ugfx.YELLOW)
	
	if orc3>0:
		ugfx.fill_circle(70,70,20,ugfx.GREEN)
	else:
		ugfx.fill_circle(70,70,30,ugfx.RED)
	
def room_9():
	###Room 9 - exits NES
	room=9
	ugfx.clear(ugfx.BLACK)
	setup_right_menu()
	build_room_walls(1,0,0,0)
	ugfx.fill_circle(100,150,5,ugfx.YELLOW)
	
	if not haskey1==1:
		ugfx.fill_circle(100,165,5,ugfx.GREEN)
	
	
	
def game_over(reason):
	ugfx.clear(ugfx.BLACK)
	ugfx.set_default_font(ugfx.FONT_TITLE)
	
	ugfx.text(80,40,"Game Over!",ugfx.WHITE)
	ugfx.text(20,100,reason,ugfx.RED)
	playing=0
	
def orc_kicking(strength, orc, hp):
	ugfx.area(190,30,300,180, ugfx.BLACK)
	damage_orc = (pyb.rng()%6)
	ugfx.text(190, 30, "You kick the orc!", ugfx.WHITE)
	ugfx.text(190, 50, "The orc takes", ugfx.WHITE)
	ugfx.text(190, 70, str(damage_orc)+" damage.", ugfx.WHITE)
	orc = orc-damage_orc
	tone(155.563,250,30)
	pyb.delay(1000)
	damage = (pyb.rng()%strength)
	ugfx.text(190, 100, "The orc kicks you!", ugfx.WHITE)
	ugfx.text(190, 120, "You take "+str(damage)+" damage.", ugfx.WHITE)
	hp = hp-damage
	tone(174.614,250,30)
	
	ugfx.text(190, 150, "A: Kick again", ugfx.RED)
	ugfx.text(190, 170, "B: Run away", ugfx.RED)
	
	ugfx.area(30,200,180,250, ugfx.BLACK)
	ugfx.text(30, 200, "HP: "+str(hp), ugfx.BLUE)
	return orc,hp


def tone(f,t,b=0):
    global bz
    p = int(1000000/f)
    t1 = pyb.millis()+t
    while pyb.millis() < t1:
        bz.high()
        pyb.udelay(p)
        bz.low()
        pyb.udelay(p)
    if b!=0: pyb.delay(b)
    
def play_theme():
    bp=250 # millis
    pp=30
    # g g g E f f f D
    g=195.998
    ef=155.563
    f=174.614
    d=146.832
    tone(d,bp,pp)
    tone(d,bp,pp)
    tone(d,bp,pp)
    tone(g,bp*4,pp)
    
    tone(d,bp,pp)
    tone(d,bp,pp)
    tone(d,bp,pp)
    tone(g,bp*4,pp)

	
			

ugfx.set_default_font(ugfx.FONT_TITLE)

ugfx.clear(ugfx.BLACK)
ugfx.text(80,40,"Adventure!",ugfx.WHITE)
ugfx.text(20,100,"Escape from the Castle!",ugfx.RED)
play_theme()
pyb.delay(2000)
room_1()
###start at this room


while True:
	playing=1

	while playing:
	
		if buttons.is_triggered("JOY_UP"):
			if room == 1:
				room=2
				room_2()
			elif room == 3:
				room=5
				room_5()
			elif room==9:
				room=8
				room_8()

		if buttons.is_triggered("JOY_DOWN"):
			if room == 2:
				room=1
				room_1()
			elif room==8:
				room=9
				room_9()
			elif room==5:
				room=3
				room_3()
		if buttons.is_triggered("JOY_LEFT"):
			if room == 2:
				if orc1>0:
					game_over("The orc killed you!")
					break
				else:
					room=3
					room_3()
			elif room == 4:
				room=2
				room_2()
			elif room==8:
				room=7
				room_7()
			elif room==7:
				room=6
				room_6()
			elif room==6:
				room=5
				
				room_5()
		if buttons.is_triggered("JOY_RIGHT"):
			if room == 2:
				if orc1 >0:
					game_over("The orc gobbled you up!")
					break
				else:
					room=4
					room_4()

			elif room == 3:
				room=2
				room_2()
			elif room==5:
				if orc2 >0:
					game_over("The orc gobbled you up!")
					break
				else:
					room=6
					room_6()
		
			elif room==6:
				room=7
				room_7()
			elif room==7:
				room=8
				room_8()
		if buttons.is_triggered("BTN_A"):
			btn_a_presses+=1
			if room == 2:
				ugfx.area(190,30,300,180, ugfx.BLACK)
				if btn_a_presses==1:
					ugfx.text(190, 30, "With which leg?", ugfx.RED)
					ugfx.text(190, 50, "A: Left", ugfx.RED)
					ugfx.text(190, 70, "B: Right", ugfx.RED)
					ugfx.text(190, 90, "Joy Press: Middle", ugfx.RED)
				
				elif (btn_a_presses>1 and orc1 > 0 and hp >0):
					orc1,hp=orc_kicking(6, orc1, hp)
					if orc1<=0:
						ugfx.fill_circle(130,70,10,ugfx.RED)	
				
				elif (orc1<=0 and hp>0):
					ugfx.text(190, 30, "The orc is dead.", ugfx.RED)
					ugfx.text(190, 50, "It would be mean ", ugfx.RED)
					ugfx.text(190, 70, "to kick it again.", ugfx.RED)
				elif (hp>=0):
					game_over("Arrogance is death!")
					break
			elif room==5:
				ugfx.area(190,30,300,180, ugfx.BLACK)
				if btn_a_presses==1:
					ugfx.text(190, 30, "With which leg?", ugfx.RED)
					ugfx.text(190, 50, "A: Left", ugfx.RED)
					ugfx.text(190, 70, "B: Right", ugfx.RED)
					ugfx.text(190, 90, "Joy Press: Middle", ugfx.RED)
				
				elif (btn_a_presses>1 and orc2 > 0 and hp >0):
					orc2,hp=orc_kicking(6, orc2, hp)
					if orc2<=0:
						ugfx.fill_circle(70,70,10,ugfx.RED)	
				
				elif (orc2<=0 and hp>0):
					ugfx.text(190, 30, "The orc is dead.", ugfx.RED)
					ugfx.text(190, 50, "It would be mean ", ugfx.RED)
					ugfx.text(190, 70, "to kick it again.", ugfx.RED)
				elif (hp>=0):
					game_over("Arrogance is death!")
					break
			elif room==6:
				ugfx.area(190,30,300,180, ugfx.BLACK)
				ugfx.text(190, 30, "You feel a lot", ugfx.RED)
				ugfx.text(190, 50, "better!", ugfx.RED)	
				ugfx.text(190, 70, "A: Drink more", ugfx.RED)
				ugfx.text(190, 90, "B: Look in", ugfx.RED)
				hp+=10

				ugfx.area(30,200,180,250, ugfx.BLACK)
				ugfx.text(30, 200, "HP: "+str(hp), ugfx.BLUE)
				if hp>50:
					ugfx.area(190,30,300,180, ugfx.BLACK)
					ugfx.text(190, 30, "You feel really", ugfx.RED)
					ugfx.text(190, 50, "full!", ugfx.RED)	
					pyb.delay(1000)
					ugfx.text(190, 70, "You burst!", ugfx.RED)
					pyb.delay(2000)
					
					game_over("Moderation is key!")
			elif room==8:
				ugfx.area(190,30,300,180, ugfx.BLACK)
				if btn_a_presses==1 and orc3>0:
					ugfx.text(190, 30, "With which leg?", ugfx.RED)
					ugfx.text(190, 50, "A: Left", ugfx.RED)
					ugfx.text(190, 70, "B: Right", ugfx.RED)
					ugfx.text(190, 90, "Joy Press: Middle", ugfx.RED)
				
				elif (btn_a_presses>1 and orc3 > 0 and hp >0):
					orc3,hp=orc_kicking(6, orc3, hp)
					if orc3<=0:
						ugfx.fill_circle(70,70,20,ugfx.RED)	
				
				elif (orc3<=0 and hp>0):
					ugfx.text(190, 30, "The orc is dead.", ugfx.RED)
					ugfx.text(190, 50, "It would be mean ", ugfx.RED)
					ugfx.text(190, 70, "to kick it again.", ugfx.RED)
				elif (hp>=0):
					game_over("Arrogance is death!")
					break	
			elif room==9:
				ugfx.fill_circle(100,165,5,ugfx.BLACK)
				ugfx.area(190,30,300,180, ugfx.BLACK)
				ugfx.text(190, 30, "You take the key.", ugfx.RED)
				ugfx.text(190, 50, "You put it in", ugfx.RED)
				ugfx.text(190, 70, "your pocket.", ugfx.RED)
				haskey1=1
			if room==1 and haskey1==1:
				game_over("Well done! You escaped!")
				
				

		if buttons.is_triggered("BTN_B"):
			if room == 2:
				if btn_a_presses==1 and orc1>0:
					#right kick
					orc1,hp=orc_kicking(6, orc1, hp)
					if orc1<=0:
						ugfx.fill_circle(130,70,10,ugfx.RED)
				elif btn_a_presses==0 and orc1>0:
					#punch
					ugfx.text(190, 110, "Why would you want", ugfx.RED)
					ugfx.text(190, 130, "to punch it when", ugfx.RED)
					ugfx.text(190, 150, "you can kick it?", ugfx.RED)
				elif btn_a_presses>1 and orc1>0:
					#running away
					ugfx.area(190,30,300,180, ugfx.BLACK)
					ugfx.text(190, 110, "You run back to ", ugfx.RED)
					ugfx.text(190, 130, "safety.", ugfx.RED)
					pyb.delay(1000)
					room=1
					room_1()
			if room == 5:
				if btn_a_presses==1 and orc2>0:
					#right kick
					orc2,hp=orc_kicking(6, orc2, hp)
					if orc2<=0:
						ugfx.fill_circle(130,70,10,ugfx.RED)
				elif btn_a_presses==0 and orc2>0:
					#tell a joke
					ugfx.area(190,30,300,180, ugfx.BLACK)
					
					ugfx.text(190, 30, "Why do orcs belch", ugfx.WHITE)
					ugfx.text(190, 50, "so much?", ugfx.WHITE)
					pyb.delay(3000)
					
					ugfx.text(190, 70, "Because they're", ugfx.WHITE)
					ugfx.text(190, 90, "always goblin!", ugfx.WHITE) #thanks davidc
					orc2=0
					pyb.delay(1000)
					ugfx.text(80, 50, "Ha", ugfx.WHITE)
					pyb.delay(1000)
					
					ugfx.text(100, 50, "ha", ugfx.WHITE)
					pyb.delay(1000)
					
					ugfx.text(120, 50, "ha...", ugfx.WHITE)
					pyb.delay(1000)
					
					ugfx.fill_circle(70,70,10,ugfx.RED)	
					pyb.delay(1000)
					
					ugfx.text(190, 110, "The orc dies ", ugfx.RED)
					ugfx.text(190, 130, "of laughter.", ugfx.RED)
					
					
				elif btn_a_presses>1 and orc2>0:
					#running away
					ugfx.area(190,30,300,180, ugfx.BLACK)
					ugfx.text(190, 110, "You run back to ", ugfx.RED)
					ugfx.text(190, 130, "safety.", ugfx.RED)
					pyb.delay(1000)
					room=1
					room_1()
				
			elif room==6:
				ugfx.area(190,30,300,180, ugfx.BLACK)
				ugfx.text(190, 30, "You stare into", ugfx.RED)
				ugfx.text(190, 50, "the depths.", ugfx.RED)
				pyb.delay(1000)
				ugfx.text(190, 70, "You fall in!", ugfx.RED)	
				pyb.delay(1000)
				
				game_over("Drowned in a fountain.")
			if room == 8:
				if btn_a_presses==1 and orc3>0:
					#right kick
					orc3,hp=orc_kicking(6, orc3, hp)
					if orc3<=0:
						ugfx.fill_circle(70,70,20,ugfx.RED)
				elif btn_a_presses==0 and orc3>0:
					#sneak
					ugfx.text(190, 110, "You try to sneak", ugfx.RED)
					ugfx.text(190, 130, "past the giant orc", ugfx.RED)
					pyb.delay(1000)
					
					ugfx.text(190, 150, "It doesn't work.", ugfx.RED)
					pyb.delay(1000)
					game_over("Never sneak past an orc!")
				elif btn_a_presses>1 and orc3>0:
					#running away
					ugfx.area(190,30,300,180, ugfx.BLACK)
					ugfx.text(190, 110, "You run back to ", ugfx.RED)
					ugfx.text(190, 130, "safety.", ugfx.RED)
					pyb.delay(1000)
					room=1
					room_1()		
			elif room==9:
				ugfx.fill_circle(100,172,5,ugfx.BLACK)
				ugfx.area(190,30,300,180, ugfx.BLACK)
				ugfx.text(190, 30, "You take the key.", ugfx.RED)
				ugfx.text(190, 50, "You swallow it.", ugfx.RED)
				pyb.delay(1000)
				ugfx.text(190, 70, "You choke to death.", ugfx.RED)	
				pyb.delay(1000)
				
				game_over("Choked to death on key.")			
		
		if buttons.is_triggered("JOY_CENTER"):
			if room == 2:
				if btn_a_presses==1:
					#middle kick
					orc1,hp=orc_kicking(6, orc1, hp)
					if orc1<=0:
						ugfx.fill_circle(130,70,10,ugfx.RED)
			if room == 5:
				if btn_a_presses==1:
					#middle kick
					orc2,hp=orc_kicking(6, orc2, hp)
					if orc2<=0:
						ugfx.fill_circle(130,70,10,ugfx.RED)
			if room == 8:
				if btn_a_presses==1:
					#middle kick
					orc3,hp=orc_kicking(8, orc3, hp)
					if orc3<=0:
						ugfx.fill_circle(130,70,10,ugfx.RED)
		
	pyb.wfi() 
	

