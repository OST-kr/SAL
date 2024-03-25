import pygame # spacebar_code == 32, esc_code == 27, enter_code == 13
import random
import time
import sys # eye_open - 1 / eye_closed - 2 / walk - 3 / right - 4 / left - 5 / rest - 6
import pyautogui

# pygame 초기화
pygame.init()

# 창 크기 설정
scr_width = 2560
scr_height = 1440
screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
white = (255, 255, 255)

# 자극 이미지
img_width = scr_width/2
img_height = scr_width/2

leftImg = pygame.image.load("C:/Users/OST/Desktop/pg1/Stimulus_generator/picture/left.jpg")
leftImg = pygame.transform.scale(leftImg, (img_width, img_height))
rightImg = pygame.image.load("C:/Users/OST/Desktop/pg1/Stimulus_generator/picture/right.jpg")
rightImg = pygame.transform.scale(rightImg, (img_width, img_height))
walkImg = pygame.image.load("C:/Users/OST/Desktop/pg1/Stimulus_generator/picture/walk.jpg")
walkImg = pygame.transform.scale(walkImg, (img_width, img_height))
cEyeImg = pygame.image.load("C:/Users/OST/Desktop/pg1/Stimulus_generator/picture/closed_eye.png")
cEyeImg = pygame.transform.scale(cEyeImg, (img_width, img_height))
oEyeImg = pygame.image.load("C:/Users/OST/Desktop/pg1/Stimulus_generator/picture/open_eye.png")
oEyeImg = pygame.transform.scale(oEyeImg, (img_width, img_height))
endImg = pygame.image.load("C:/Users/OST/Desktop/pg1/Stimulus_generator/picture/end.png")
endImg = pygame.transform.scale(endImg, (img_width, img_height))
restImg = pygame.image.load("C:/Users/OST/Desktop/pg1/Stimulus_generator/picture/rest.png")
restImg = pygame.transform.scale(restImg, (img_width, img_height))

clock = pygame.time.Clock()
# Button 클래스
class Button:
    def __init__ (self, img_in, x, y, width, height, action = None):
        click = pygame.mouse.get_pressed()
        if click[0] and action != None:
            time.sleep(1)
            action()
        else:
            screen.blit(img_in,(x, y))

# 메인 화면
def mainmenu():
    # 화면 크기
    start_screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)

    pygame.font.init()
    font = pygame.font.Font('Maplestory Bold.ttf', 40)
    start_message = font.render('Press the Space Bar to Start.', True, (0,0,0))
    ment_font = pygame.font.Font('Maplestory Bold.ttf', 90)
    ment_message= ment_font.render('시청각 자극 발생기 (feat. SAL)', True, (0,0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
        start_screen.fill(white)
        start_screen.blit(start_message, (600, 750))
        start_screen.blit(ment_message, (600, 600))
        pygame.display.update()

# setting 화면
expose = 0
rest = 0
cycle = 0
def setting_screen():
    pygame.font.init()

    setting_screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)

    setting_screen.fill(white)

    input_box = pygame.Rect(490, 850, 800, 40)

    text = ''
    global expose
    global rest
    global cycle
    expose = 0
    rest = 0
    cycle = 0

    font = pygame.font.Font('Maplestory Bold.ttf', 40)
    description_font = pygame.font.Font('Maplestory Bold.ttf', 25)
    
    txt_surface = font.render(text, True, (0,0,0))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP:
                    expose += 1
                    print(expose)
                if event.key == pygame.K_LEFT:
                    rest += 1
                if event.key == pygame.K_DOWN:
                    cycle += 1
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                txt_surface = font.render(text, True, (0,0,0))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
        
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        
        setting_screen.fill(white)
        setting_screen.blit(txt_surface, (500, 850))

        setting_message = font.render('This Page is Setting Page.', True, (0,0,0))
        setting_screen.blit(setting_message, (250, 250))
        
        exposed_message = font.render(f'자극 노출 시간 :  {expose}초', True, (0,0,0))
        setting_screen.blit(exposed_message, (250, 400))

        exposed_ment_message = description_font.render('(자극에 노출되어 있는 시간)', True, (0,0,0))
        setting_screen.blit(exposed_ment_message, (250, 450))
        
        rest_message = font.render(f'휴식 시간 :  {rest}초', True, (0,0,0))
        setting_screen.blit(rest_message, (250, 550))

        rest_ment_message = description_font.render('(자극 후 휴식 시간)', True, (0,0,0))
        setting_screen.blit(rest_ment_message, (250, 600))

        cycle_message = font.render(f'반복횟수 :  {cycle}번', True, (0,0,0))
        setting_screen.blit(cycle_message, (250, 700))

        image_message = font.render('이미지 URL : ', True, (0,0,0))
        setting_screen.blit(image_message, (250, 850))

        pygame.display.update()

# 시작전 로딩화면
def loading_Screen(): 
    loading_Screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    loading_Screen.fill(white)
    pygame.display.update()

# eye_open 화면
def eye_open_Screen():
    start_time = time.time()
    pyautogui.platformModule._keyDown('1')
    #pyautogui.platformModule._keyUp('1')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"키보드 입력에 걸린 시간: {elapsed_time} 초")

    font = pygame.font.Font('Maplestory Bold.ttf', 40)
    global num
    epoch_num = font.render(f'{num}', True, (0,0,0))

    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    screen.fill(white)
    screen.blit(oEyeImg, (scr_width/2 - img_width/2, scr_height/2 - img_height/2))
    screen.blit(epoch_num, (scr_width/2, 0))
    pygame.display.update()

# eye_closed 화면
def eye_closed_Screen():
    start_time = time.time()
    pyautogui.platformModule._keyDown('2')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"키보드 입력에 걸린 시간: {elapsed_time} 초")

    font = pygame.font.Font('Maplestory Bold.ttf', 40)
    global num
    epoch_num = font.render(f'{num}', True, (0,0,0))

    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    screen.fill(white)
    screen.blit(cEyeImg, (scr_width/2 - img_width/2, scr_height/2 - img_height/2))
    screen.blit(epoch_num, (scr_width/2, 0))
    pygame.display.update()

# walk 화면
def walk_Screen():
    start_time = time.time()
    pyautogui.platformModule._keyDown('3')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"키보드 입력에 걸린 시간: {elapsed_time} 초")

    font = pygame.font.Font('Maplestory Bold.ttf', 40)
    global num
    epoch_num = font.render(f'{num}', True, (0,0,0))

    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    screen.fill(white)
    screen.blit(walkImg, (scr_width/2 - img_width/2, scr_height/2 - img_height/2))
    screen.blit(epoch_num, (scr_width/2, 0))
    pygame.display.update()

# right 화면
def right_Screen():
    start_time = time.time()
    pyautogui.platformModule._keyDown('4')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"키보드 입력에 걸린 시간: {elapsed_time} 초")

    font = pygame.font.Font('Maplestory Bold.ttf', 40)
    global num
    epoch_num = font.render(f'{num}', True, (0,0,0))

    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    screen.fill(white)
    screen.blit(rightImg, (scr_width/2 - img_width/2, scr_height/2 - img_height/2))
    screen.blit(epoch_num, (scr_width/2, 0))
    pygame.display.update()

# left 화면
def left_Screen():
    start_time = time.time()
    pyautogui.platformModule._keyDown('5')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"키보드 입력에 걸린 시간: {elapsed_time} 초")

    font = pygame.font.Font('Maplestory Bold.ttf', 40)
    global num
    epoch_num = font.render(f'{num}', True, (0,0,0))

    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    screen.fill(white)
    screen.blit(leftImg, (scr_width/2 - img_width/2, scr_height/2 - img_height/2))
    screen.blit(epoch_num, (scr_width/2, 0))
    pygame.display.update()

# end 화면
def end_Screen():
    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    screen.fill(white)
    screen.blit(endImg, (scr_width/2 - img_width/2, scr_height/2 - img_height/2))
    pygame.display.update()

# rest 화면
def rest_Screen():
    start_time = time.time()
    pyautogui.platformModule._keyDown('6')
    # pyautogui.platformModule._keyUp('6')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"키보드 입력에 걸린 시간: {elapsed_time} 초")
    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    screen.fill(white)
    screen.blit(restImg, (scr_width/2 - img_width/2, scr_height/2 - img_height/2))
    pygame.display.update()


mainmenu()
setting_screen()
stimul = [1, 2, 3, 4, 5]
# 각각 몇번씩 진행할지 정하기
test_stimul = stimul * cycle
random.shuffle(test_stimul)
print(test_stimul)

print(f"자극 노출시간 : {expose}초")
print(f"반복 : {cycle}번")
print(f"휴식시간 : {rest}초")
loading_Screen()
time.sleep(3)
num = 1
for i in test_stimul:
    if i == 1:
        right_Screen()
        print("right")
        time.sleep(expose)
        rest_Screen()
        print("rest")
        time.sleep(rest)
    elif i == 2:
        eye_closed_Screen()
        print("eye_closed")
        time.sleep(expose)
        rest_Screen()
        print("rest")
        time.sleep(rest)
    elif i == 3:
        eye_open_Screen()
        print("eye_open")
        time.sleep(expose)
        rest_Screen()
        print("rest")
        time.sleep(rest)
    elif i == 4:
        left_Screen()
        print("left")
        time.sleep(expose)
        rest_Screen()
        print("rest")
        time.sleep(rest)
    else :
        walk_Screen()
        print("walk")
        time.sleep(expose)
        rest_Screen()
        print("rest")
        time.sleep(rest)
    print(f"지금은 {num}번째 이미지")
    num += 1

end_Screen()
print("end")
time.sleep(2)
pygame.quit()