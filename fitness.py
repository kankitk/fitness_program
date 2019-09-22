
import pygame
import time
import datetime
collect = open("log.txt", "a")
collect.write("\n\n\n\n\nDATE:-  "+str(datetime.datetime.now().date())+"\n\n")
collect.close()

print("start:-  ", datetime.datetime.now().time())

def water_Reminder():
    pygame.mixer.init()
    pygame.mixer.music.load('pani.mp3')
    pygame.mixer.music.play()
    collect = open("log.txt", "a")
    collect.write("\nTime to Drink Water:-  "+str(datetime.datetime.now().time())+"\n")
    w=input('type "drank" after you drink water: ')
    if w == "drank":
        pygame.mixer.music.stop()
        collect.write("Drank at:-  "+str(datetime.datetime.now().time())+"\n")
        collect.close()




def eye_Remainder():
    pygame.mixer.init()
    pygame.mixer.music.load('eye.mp3')
    pygame.mixer.music.play()
    collect = open("log.txt", "a")
    collect.write("\nTime to Eye exercise:-  "+str(datetime.datetime.now().time())+"\n")
    w=input('type "eye done" after eye exercise: ')
    if w == 'eye done':
        pygame.mixer.music.stop()
        collect.write("Eye exercise done at:-  "+str(datetime.datetime.now().time())+"\n")
        collect.close()

def physic_Remainder():
    pygame.mixer.init()
    pygame.mixer.music.load('exercise.mp3')
    pygame.mixer.music.play()
    collect = open("log.txt", "a")
    collect.write("\nTime to do Physical exercise:-  "+str(datetime.datetime.now().time())+"\n")
    w = input('type "exercise done" after eye exercise: ')
    if w == 'exercise done':
        pygame.mixer.music.stop()
        collect.write("Physical Exercise done at:-  "+str(datetime.datetime.now().time())+"\n")
        collect.close()


to_do_list=[False,False,False]
fun=[water_Reminder,eye_Remainder,physic_Remainder]
for i in range(32):
    start=time.time()
    while True:
        if int(start-(time.time())) % 900 == 0:
            for i in range(3):
                if to_do_list[i]:
                    to_do_list[i]=False
                    print(datetime.datetime.now().time())
                    fun[i]()

        if int(start-time.time()) % 3600 == 0 and int(time.time()-start) > 0:
            to_do_list[0]=True

        if int(start-time.time()) % 1800 == 0 and int(time.time()-start) > 0:
            to_do_list[1]=True


        if int(start-time.time()) % 2700 == 0 and int(time.time()-start) > 0:
            to_do_list[2]=True


