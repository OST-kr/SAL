import pygame # spacebar_code == 32, esc_code == 27, enter_code == 13
import random
import time
import sys # eye_open - 1 / eye_closed - 2 / walk - 3 / right - 4 / left - 5 / rest - 6
import pyautogui
from gtts import gTTS
import playsound
import winsound
from winsound import Beep

# pygame 초기화
pygame.init()

# 창 크기 설정
scr_width = 2560
scr_height = 1440
screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
white = (255, 255, 255)
clock = pygame.time.Clock()

# 이미지
img_width = scr_width/2
img_height = scr_width/2
endImg = pygame.image.load("C:/Users/OST/Desktop/pg1/Stimulus_generator/picture/end.png")
endImg = pygame.transform.scale(endImg, (img_width, img_height))

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
        

        setting_screen.blit(txt_surface, (500, 850))

        setting_screen.fill(white)
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
    speak("안녕하십니까. 잠시 후 실험이 시작되오니. 몸을 편하게 해주시고 잠시후 신호가 시작되고 난 후 안내되는 방송에 집중해서 행동해주시기 바랍니다.", "start")
    speak(f"낮은 소리가 들리면 오른 팔을 {expose}초간 돌려주세요", "right")
    Beep(300, 1000)
    speak(f"높은 소리가 들리면 왼 팔을 {expose}초간 돌려주세요", "left")
    Beep(1000, 1000)
    speak(f"소리가 두번 들리면 다리를 {expose}초간 들어 올려주세요", "foot")
    Beep(800, 500)
    Beep(800, 500)
    pygame.display.update()

# walk 화면
def foot_Screen():
    font = pygame.font.Font('Maplestory Bold.ttf', 40)
    global num
    epoch_num = font.render(f'{num}', True, (0,0,0))

    Beep(800, 500)
    Beep(800, 500)
    start_time = time.time()
    pyautogui.platformModule._keyDown('1')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"키보드 입력에 걸린 시간: {elapsed_time} 초")

    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    screen.fill(white)
    screen.blit(epoch_num, (scr_width/2, 0))
    pygame.display.update()

# right 화면
def right_Screen():
    font = pygame.font.Font('Maplestory Bold.ttf', 40)
    global num
    epoch_num = font.render(f'{num}', True, (0,0,0))

    Beep(300, 1000)
    start_time = time.time()
    pyautogui.platformModule._keyDown('2')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"키보드 입력에 걸린 시간: {elapsed_time} 초")

    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    screen.fill(white)
    screen.blit(epoch_num, (scr_width/2, 0))
    pygame.display.update()

# left 화면
def left_Screen():
    font = pygame.font.Font('Maplestory Bold.ttf', 40)
    global num
    epoch_num = font.render(f'{num}', True, (0,0,0))

    Beep(1000, 1000)
    start_time = time.time()
    pyautogui.platformModule._keyDown('3')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"키보드 입력에 걸린 시간: {elapsed_time} 초")

    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    screen.fill(white)
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
    speak(f"{rest}초간 휴식을 취해 주세요", "rest")
    start_time = time.time()
    pyautogui.platformModule._keyDown('6')
    # pyautogui.platformModule._keyUp('6')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"키보드 입력에 걸린 시간: {elapsed_time} 초")
    screen = pygame.display.set_mode((scr_width, scr_height), pygame.FULLSCREEN)
    screen.fill(white)
    pygame.display.update()

def speak(text, name):

     tts = gTTS(text=text, lang='ko')
     filename=f'{name}.mp3'
     playsound.playsound(filename)

mainmenu()
setting_screen()
stimul = [1, 2, 3]
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
        foot_Screen()
        print("foot")
        time.sleep(expose)
        rest_Screen()
        print("rest")
        time.sleep(rest)
    elif i == 2:
        right_Screen()
        print("right")
        time.sleep(expose)
        rest_Screen()
        print("rest")
        time.sleep(rest)
    else :
        left_Screen()
        print("left")
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