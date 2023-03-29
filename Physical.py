# Import Modules
import os
import pygame as pg
import time
import random

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

WIDTH, HEIGHT = 2000, 1125
FPS = 60
SlideNum = 36
setupParameters = {}
practiceParameters = {}
actualParameters = {}
timeLen = 5 #time length of how long you get to shift-click, is universal (for now?)
actualAmount = 5 #number of real trials
countDownTime = 0.5

# Initialize Pygame and create a window
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
#screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

pg.font.init()
font = pg.font.SysFont('Arial', 50)


def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pg.mixer.Sound(fullname)

    return sound

class MySlide(pg.Surface):
    def __init__(self, size, name):
        self.name = name
        pg.Surface.__init__(self,size)  # call Surface initializer
        self.image, self.rect = load_image(f"SlidesPhysical/Slide{i}.png")
        
        
slides = []
for i in range(0,2):
    name = f"slide_{i}"
    sld = MySlide((WIDTH,HEIGHT), name)
    slides.append(sld)

for i in range(1,SlideNum+1):
    name = f"slide_{i}"
    sld = MySlide((WIDTH,HEIGHT), name)
    slides.append(sld)
    


    
    #slides[i].image,slides[i].rect = load_image(f"Slides/Slide{i}")
# k = []
# k = slides[0]
# k.append(slides[1])
# for i in range(1,SlideNum+1):
#     k.extend = slides[i]
# slides = k

def slide0(): #this is the function for getting user ID and handedness
    dog = 1
    bunny = False
    rabbit = False
    user_input = ''
    user_input2 = ''
    prompt_surf = font.render("Patient-ID?", True, (255, 255, 255))
    prompt_rect = prompt_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2-90))

    screen.fill((0,0,0))
    
    while not bunny:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                bunny = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                elif event.key == pg.K_RETURN:
                    bunny = True
                elif event.key == pg.K_BACKSPACE:
                    user_input = user_input[:-1]
                    screen.fill((0,0,0))
                else:
                    user_input = user_input + event.unicode
                    screen.fill((0,0,0))
            dog = 1
        if dog == 1:
            screen.blit(prompt_surf, prompt_rect)
            mellow = font.render(user_input, True, (255, 255, 255))
            kk = mellow.get_rect(center=(WIDTH // 2, HEIGHT // 2-30))
            screen.blit(mellow,kk)
            pg.display.flip()
            dog = 0
    prompt_surf2 = font.render("Handedness? ('Right' or 'Left')", True, (255, 255, 255))
    prompt_rect2 = prompt_surf.get_rect(center=(WIDTH // 2-200, HEIGHT // 2+30))
    while not rabbit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                bunny = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                elif event.key == pg.K_RETURN:
                    if user_input2 == 'Right' or user_input2 == 'Left':
                        return (user_input, user_input2)
                    else:
                        user_input2 = ''
                elif event.key == pg.K_BACKSPACE:
                    user_input2 = user_input2[:-1]
                    screen.fill((0,0,0))
                else:
                    user_input2 = user_input2 + event.unicode
                    screen.fill((0,0,0))
            dog = 1
        if dog == 1:
            screen.blit(prompt_surf, prompt_rect)
            screen.blit(prompt_surf2, prompt_rect2)
            screen.blit(mellow,kk)
            mellow2 = font.render(user_input2, True, (255, 255, 255))
            kk2 = mellow2.get_rect(center=(WIDTH // 2, HEIGHT // 2+90))
            screen.blit(mellow2,kk2)
            pg.display.flip()
            dog = 0
    return

def slide1(): #this is a good generic function for slides where the user has to press enter/return to proceed and no data is collected
    bunny = False
    while not bunny:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                bunny = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                elif event.key == pg.K_RETURN:
                    bunny = True
                elif event.key == pg.K_RIGHT and pg.key.get_mods() & pg.KMOD_CTRL:
                    bunny = True
                elif event.key == pg.K_LEFT and pg.key.get_mods() & pg.KMOD_CTRL:
                    return 'back'             
                elif event.key == pg.K_w:
                    return 'bark'
    return
        
def slide16(hand, domorweak, timeLen):
    bunny = False
    shift_count = 0
    if (hand == 'Right' and domorweak == 'dom') or (hand == 'Left' and domorweak == 'weak'):
        water = pg.K_RSHIFT
    else:
        water = pg.K_LSHIFT
    timestart = time.time()
    while not bunny:
        # keys = pg.key.get_pressed()
    
        # # Check if either shift key is pressed
        # if keys[pg.K_RSHIFT]:
        #     shift_count += 1

        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                bunny = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                elif event.key == water:
                    shift_count += 1

        if (time.time() - timestart) >= timeLen:
            bunny = True
    return shift_count

def slide24(surface):
    dog = 0
    bunny = False
    select = 0
    while not bunny:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                bunny = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                elif event.key == pg.K_RETURN:
                    if select != 0:
                        bunny = True
                elif event.key == pg.K_LEFT:
                    if (event.key == pg.K_LEFT and pg.key.get_mods() & pg.KMOD_CTRL):
                        return 'back'
                    else:
                        select = -1
                        dog = 1
                elif event.key == pg.K_RIGHT:
                    select = 1
                    dog = 1
            
        if dog == 1:
            screen.fill((0,0,0))
            new = surface.copy()
            color = (255,0,0)
            pg.draw.rect(new, color, pg.Rect(704+select*409, 498, 593, 424),  10)
            #screen.blit(pr.Rect(200+select*40, 30, 60, 60), 2)
            screen.blit(new, (20, 75))
            pg.display.flip()
            dog = 0
    return select

trialType = 0 #0 is baseline, 1 is practice, 2 is actual
baselineNum = 1
practiceNum = 1
actualNum = 1
countdown = 3
done = False
current_slide = 0
bank = {}
bank['practice'] = 0
bank['actual'] = 0
while not done:
    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
            elif event.key == pg.K_RIGHT and pg.key.get_mods() & pg.KMOD_CTRL:
                current_slide = (current_slide + 1)
            elif event.key == pg.K_LEFT and pg.key.get_mods() & pg.KMOD_CTRL:
                current_slide = (current_slide - 1)
        melon = 1
                
    if current_slide == 0 and melon == 0:
        bum = slide0()
        #setupParameters.append(bum) # output from slide 0 (ID and handedness) is index 0's two subindices (setupParameters[0][0:1])
        setupParameters['ID'] = bum[0] # making a dictionary
        setupParameters['handedness'] = bum[1]
        #current_slide = 1
        if setupParameters['handedness'] == 'Right':
                current_slide = 2
        elif setupParameters['handedness'] == 'Left':
                current_slide = 3
        melon = 1
        
    if current_slide == 1 and melon == 0:
        bum = slide1()
        if bum == 'back':
            current_slide = 0
        elif bum == 'bark':
            current_slide = 19
        else:
            if setupParameters['handedness'] == 'Right':
                current_slide = 2
            elif setupParameters['handedness'] == 'Left':
                current_slide = 3
        melon = 1

    if (2 <= current_slide <= 15) and melon == 0:
        if countdown == 3: #i.e. countdown is ready to go to the "3" slide next
            bum = slide1()
            if bum == 'back': ##need to take this out
                current_slide = current_slide
            elif baselineNum == 1 or baselineNum == 2:
                if setupParameters['handedness'] == 'Right':
                    current_slide = 10
                elif setupParameters['handedness'] == 'Left':
                    current_slide = 11
            elif baselineNum == 3 or baselineNum == 4:
                if setupParameters['handedness'] == 'Right':
                    current_slide = 11
                elif setupParameters['handedness'] == 'Left':
                    current_slide = 10

            countdown = 2
            melon = 1

        if countdown == 2 and melon == 0: 
            time.sleep(countDownTime)
            if trialType == 0:
                if baselineNum == 1 or baselineNum == 2:
                    if setupParameters['handedness'] == 'Right':
                        current_slide = 12
                    elif setupParameters['handedness'] == 'Left':
                        current_slide = 13
                elif baselineNum == 3 or baselineNum == 4:
                    if setupParameters['handedness'] == 'Right':
                        current_slide = 13
                    elif setupParameters['handedness'] == 'Left':
                        current_slide = 12
            elif trialType == 1:
                if (setupParameters['handedness'] == 'Right') and (practiceParameters[f"practice #{practiceNum}"][1] == "easy task"):
                    current_slide = 12
                if (setupParameters['handedness'] == 'Left') and (practiceParameters[f"practice #{practiceNum}"][1] == "hard task"):
                    current_slide = 12
                if (setupParameters['handedness'] == 'Right') and (practiceParameters[f"practice #{practiceNum}"][1] == "hard task"):
                    current_slide = 13
                if (setupParameters['handedness'] == 'Left') and (practiceParameters[f"practice #{practiceNum}"][1] == "easy task"):
                    current_slide = 13

            elif trialType == 2:
                if (setupParameters['handedness'] == 'Right') and (actualParameters[f"actual #{actualNum}"][1] == "easy task"):
                    current_slide = 12
                if (setupParameters['handedness'] == 'Left') and (actualParameters[f"actual #{actualNum}"][1] == "hard task"):
                    current_slide = 12
                if (setupParameters['handedness'] == 'Right') and (actualParameters[f"actual #{actualNum}"][1] == "hard task"):
                    current_slide = 13
                if (setupParameters['handedness'] == 'Left') and (actualParameters[f"actual #{actualNum}"][1] == "easy task"):
                    current_slide = 13

            countdown = 1
            melon = 1

        if countdown == 1 and melon == 0:
            time.sleep(countDownTime)
            if trialType == 0:
                if baselineNum == 1 or baselineNum == 2:
                    if setupParameters['handedness'] == 'Right':
                        current_slide = 14
                    elif setupParameters['handedness'] == 'Left':
                        current_slide = 15
                elif baselineNum == 3 or baselineNum == 4:
                    if setupParameters['handedness'] == 'Right':
                        current_slide = 15
                    elif setupParameters['handedness'] == 'Left':
                        current_slide = 14

            elif trialType == 1:
                if (setupParameters['handedness'] == 'Right') and (practiceParameters[f"practice #{practiceNum}"][1] == "easy task"):
                    current_slide = 14
                if (setupParameters['handedness'] == 'Left') and (practiceParameters[f"practice #{practiceNum}"][1] == "hard task"):
                    current_slide = 14
                if (setupParameters['handedness'] == 'Right') and (practiceParameters[f"practice #{practiceNum}"][1] == "hard task"):
                    current_slide = 15
                if (setupParameters['handedness'] == 'Left') and (practiceParameters[f"practice #{practiceNum}"][1] == "easy task"):
                    current_slide = 15

            elif trialType == 2:
                if (setupParameters['handedness'] == 'Right') and (actualParameters[f"actual #{actualNum}"][1] == "easy task"):
                    current_slide = 14
                if (setupParameters['handedness'] == 'Left') and (actualParameters[f"actual #{actualNum}"][1] == "hard task"):
                    current_slide = 14
                if (setupParameters['handedness'] == 'Right') and (actualParameters[f"actual #{actualNum}"][1] == "hard task"):
                    current_slide = 15
                if (setupParameters['handedness'] == 'Left') and (actualParameters[f"actual #{actualNum}"][1] == "easy task"):
                    current_slide = 15

            countdown = 0
            melon = 1
        if countdown == 0 and melon == 0:
            time.sleep(countDownTime)
            if trialType == 0:
                if baselineNum == 1 or baselineNum == 2:
                    if setupParameters['handedness'] == 'Right':
                        current_slide = 16
                    elif setupParameters['handedness'] == 'Left':
                        current_slide = 17
                elif baselineNum == 3 or baselineNum == 4:
                    if setupParameters['handedness'] == 'Right':
                        current_slide = 17
                    elif setupParameters['handedness'] == 'Left':
                        current_slide = 16
            elif trialType == 1:
                if (setupParameters['handedness'] == 'Right') and (practiceParameters[f"practice #{practiceNum}"][1] == "easy task"):
                    current_slide = 16
                if (setupParameters['handedness'] == 'Left') and (practiceParameters[f"practice #{practiceNum}"][1] == "hard task"):
                    current_slide = 16
                if (setupParameters['handedness'] == 'Right') and (practiceParameters[f"practice #{practiceNum}"][1] == "hard task"):
                    current_slide = 17
                if (setupParameters['handedness'] == 'Left') and (practiceParameters[f"practice #{practiceNum}"][1] == "easy task"):
                    current_slide = 17
            elif trialType == 2:
                if (setupParameters['handedness'] == 'Right') and (actualParameters[f"actual #{actualNum}"][1] == "easy task"):
                    current_slide = 16
                if (setupParameters['handedness'] == 'Left') and (actualParameters[f"actual #{actualNum}"][1] == "hard task"):
                    current_slide = 16
                if (setupParameters['handedness'] == 'Right') and (actualParameters[f"actual #{actualNum}"][1] == "hard task"):
                    current_slide = 17
                if (setupParameters['handedness'] == 'Left') and (actualParameters[f"actual #{actualNum}"][1] == "easy task"):
                    current_slide = 17

            melon = 1


    if (current_slide == 16 or current_slide == 17) and melon == 0:
        if trialType == 0:
            if baselineNum == 1 or baselineNum == 2:
                domorweak = 'dom'
            elif baselineNum == 3 or baselineNum == 4:
                domorweak = 'weak'
        elif trialType == 1:
            if (practiceParameters[f"practice #{practiceNum}"][1] == "easy task"):
                domorweak = 'dom'
            elif (practiceParameters[f"practice #{practiceNum}"][1] == "hard task"):
                domorweak = 'weak'
        elif trialType == 2:
            if (actualParameters[f"actual #{actualNum}"][1] == "easy task"):
                domorweak = 'dom'
            elif (actualParameters[f"actual #{actualNum}"][1] == "hard task"):
                domorweak = 'weak'

        bum = slide16(setupParameters['handedness'], domorweak, timeLen)

        if trialType == 0:
            #setupParameters.append(f"baseline trial #{baselineNum} shift-hits: {bum}") #output from slide 16/17 is index 1's value for practice run 1, index 2's value for PR2, and index 3's value for PR3
            setupParameters[f"baseline trial#{baselineNum} shift-hits"] = bum
        elif trialType == 1:
            if practiceParameters[f"practice #{practiceNum}"][1] == "hard task":
                if bum >= round(0.8 * sum([setupParameters[f"baseline trial#{i} shift-hits"] for i in range(3, 5)]) / 2):
                    #practiceParameters[f"practice #{practiceNum}"][2] == ["success", bum]
                    practiceParameters[f"practice #{practiceNum}"].append(["success", bum])
                    if practiceParameters[f"practice #{practiceNum}"][0] == "gain trial":
                        bank['practice'] += 450
                        next_slide = 32
                    elif practiceParameters[f"practice #{practiceNum}"][0] == "risk trial":
                        bank['practice'] += 0
                        next_slide = 34
                else:
                    #practiceParameters[f"practice #{practiceNum}"][2] == ["fail", bum]
                    practiceParameters[f"practice #{practiceNum}"].append(["fail", bum])
                    if practiceParameters[f"practice #{practiceNum}"][0] == "gain trial":
                        bank['practice'] += 0
                        next_slide = 37
                    elif practiceParameters[f"practice #{practiceNum}"][0] == "risk trial":
                        bank['practice'] -= 450
                        next_slide = 36
            elif practiceParameters[f"practice #{practiceNum}"][1] == "easy task":
                if bum >= round(0.4 * sum([setupParameters[f"baseline trial#{i} shift-hits"] for i in range(1, 3)]) / 2):
                    #practiceParameters[f"practice #{practiceNum}"][2] == ["success", bum]
                    practiceParameters[f"practice #{practiceNum}"].append(["success", bum])
                    if practiceParameters[f"practice #{practiceNum}"][0] == "gain trial":
                        bank['practice'] += 100
                        next_slide = 33
                    elif practiceParameters[f"practice #{practiceNum}"][0] == "risk trial":
                        bank['practice'] += 0
                        next_slide = 34
                else:
                    #practiceParameters[f"practice #{practiceNum}"][2] == ["fail", bum]
                    practiceParameters[f"practice #{practiceNum}"].append(["fail", bum])
                    if practiceParameters[f"practice #{practiceNum}"][0] == "gain trial":
                        bank['practice'] += 0
                        next_slide = 37
                    elif practiceParameters[f"practice #{practiceNum}"][0] == "risk trial":
                        bank['practice'] -= 100
                        next_slide = 35
        elif trialType == 2:
            if actualParameters[f"actual #{actualNum}"][1] == "hard task":
                if bum >= round(0.8 * sum([setupParameters[f"baseline trial#{i} shift-hits"] for i in range(3, 5)]) / 2):
                    #actualParameters[f"actual #{actualNum}"][2] == ["success", bum]
                    actualParameters[f"actual #{actualNum}"].append(["success", bum])
                    if actualParameters[f"actual #{actualNum}"][0] == "gain trial":
                        bank['actual'] += 450
                        next_slide = 32
                    elif actualParameters[f"actual #{actualNum}"][0] == "risk trial":
                        bank['actual'] += 0
                        next_slide = 34
                else:
                    #actualParameters[f"actual #{actualNum}"][2] == ["fail", bum]
                    actualParameters[f"actual #{actualNum}"].append(["fail", bum])
                    if actualParameters[f"actual #{actualNum}"][0] == "gain trial":
                        bank['actual'] += 0
                        next_slide = 37
                    elif actualParameters[f"actual #{actualNum}"][0] == "risk trial":
                        bank['actual'] -= 450
                        next_slide = 36
            elif actualParameters[f"actual #{actualNum}"][1] == "easy task":
                if bum >= round(0.5 * sum([setupParameters[f"baseline trial#{i} shift-hits"] for i in range(1, 3)]) / 2):
                    #actualParameters[f"actual #{actualNum}"][2] == ["success", bum]
                    actualParameters[f"actual #{actualNum}"].append(["success", bum])
                    if actualParameters[f"actual #{actualNum}"][0] == "gain trial":
                        bank['actual'] += 100
                        next_slide = 33
                    elif actualParameters[f"actual #{actualNum}"][0] == "risk trial":
                        bank['actual'] += 0
                        next_slide = 34
                else:
                    #actualParameters[f"actual #{actualNum}"][2] == ["fail", bum]
                    actualParameters[f"actual #{actualNum}"].append(["fail", bum])
                    if actualParameters[f"actual #{actualNum}"][0] == "gain trial":
                        bank['actual'] += 0
                        next_slide = 37
                    elif actualParameters[f"actual #{actualNum}"][0] == "risk trial":
                        bank['actual'] -= 100
                        next_slide = 35

        #print(setupParameters)
        current_slide = 18
        melon = 1

    if (current_slide == 18) and melon == 0:
        time.sleep(2)
        if trialType == 0:
            if baselineNum == 1:
                if setupParameters['handedness'] == 'Right':
                    current_slide = 4
                elif setupParameters['handedness'] == 'Left':
                    current_slide = 5
            if baselineNum == 2:
                if setupParameters['handedness'] == 'Right':
                    current_slide = 6
                elif setupParameters['handedness'] == 'Left':
                    current_slide = 7
            if baselineNum == 3:
                if setupParameters['handedness'] == 'Right':
                    current_slide = 8
                elif setupParameters['handedness'] == 'Left':
                    current_slide = 9
            if baselineNum == 4:
                if setupParameters['handedness'] == 'Right':
                    current_slide = 19
                elif setupParameters['handedness'] == 'Left':
                    current_slide = 20
                trialType = 1
            baselineNum += 1
            countdown = 3
        elif trialType == 1:
            practiceNum += 1
            #if not((practiceNum >= 4) and ((practiceNum - 1) % 3 == 0)):
            current_slide = next_slide

        elif trialType == 2:
            actualNum += 1
            #if not((actualNum >= 4) and ((actualNum - 1) % 3 == 0)):
            current_slide = next_slide
        melon = 1

    if (current_slide == 19 or current_slide == 20) and melon == 0:
        bum = slide1()
        if bum == 'back':
            current_slide = 1
        else:
            if setupParameters['handedness'] == 'Right':
                current_slide = 21
            elif setupParameters['handedness'] == 'Left':
                current_slide = 22
        melon = 1

    if (current_slide == 21 or current_slide == 22) and melon == 0:
        bum = slide1()
        if bum == 'back':
            if setupParameters['handedness'] == 'Right':
                current_slide = 19
            elif setupParameters['handedness'] == 'Left':
                current_slide = 20
        else:
            if setupParameters['handedness'] == 'Right':
                current_slide = random.randint(12,13)*2
            elif setupParameters['handedness'] == 'Left':
                current_slide = random.randint(12,13)*2+1
            if current_slide == 24 or current_slide == 25:
                #practiceParameters.append(f"gainTrial#{practiceNum}")
                practiceTrialType = "gain trial"
            elif current_slide == 26 or current_slide == 27:
                #practiceParameters.append(f"riskTrial#{practiceNum}")
                practiceTrialType = "risk trial"
        melon = 1

    if current_slide == 23 and melon == 0:
        bum = slide24(slides[current_slide].image)
        if bum == 1:
            trialType = 2
            if setupParameters['handedness'] == 'Right':
                current_slide = random.randint(14,15)*2
            elif setupParameters['handedness'] == 'Left':
                current_slide = random.randint(14,15)*2+1
            if current_slide == 28 or current_slide == 29:
                #practiceParameters.append(f"gainTrial#{practiceNum}")
                actualTrialType = "gain trial"
            elif current_slide == 30 or current_slide == 31:
                #practiceParameters.append(f"riskTrial#{practiceNum}")
                actualTrialType = "risk trial"
            melon = 1
        elif bum == -1:
            if setupParameters['handedness'] == 'Right':
                current_slide = random.randint(12,13)*2
            elif setupParameters['handedness'] == 'Left':
                current_slide = random.randint(12,13)*2+1
            if current_slide == 28 or current_slide == 29:
                #practiceParameters.append(f"gainTrial#{practiceNum}")
                practiceTrialType = "gain trial"
            elif current_slide == 30 or current_slide == 31:
                #practiceParameters.append(f"riskTrial#{practiceNum}")
                practiceTrialType = "risk trial"
            melon = 1


    if (24 <= current_slide <= 27) and melon == 0:
        bum = slide24(slides[current_slide].image)
        if bum == 'back' and practiceNum == 1:
            if setupParameters['handedness'] == 'Right':
                current_slide = 21
            elif setupParameters['handedness'] == 'Left':
                current_slide = 22
            melon = 1
        elif bum == 1:
            if setupParameters['handedness'] == 'Right':
                current_slide = 10
                #practiceParameters.append('easyTask')
                practiceParameters[f"practice #{practiceNum}"] = [practiceTrialType,"easy task"]
            if setupParameters['handedness'] == 'Left':
                current_slide = 10
                # practice.Parameters.append('hardTask')
                practiceParameters[f"practice #{practiceNum}"] = [practiceTrialType,"hard task"]
            melon = 1
        elif bum == -1:
            if setupParameters['handedness'] == 'Right':
                current_slide = 11
                # practiceParameters.append('hardTask')
                practiceParameters[f"practice #{practiceNum}"] = [practiceTrialType,"hard task"]
            if setupParameters['handedness'] == 'Left':
                current_slide = 11
                # practiceParameters.append('easyTask')
                practiceParameters[f"practice #{practiceNum}"] = [practiceTrialType,"easy task"]
            melon = 1
        countdown = 2

    if (28 <= current_slide <= 31) and melon == 0:
        bum = slide24(slides[current_slide].image)
        #print(bum)
        if bum == 1:
            if setupParameters['handedness'] == 'Right':
                current_slide = 10
                #practiceParameters.append('easyTask')
                #print('buffalo')
                actualParameters[f"actual #{actualNum}"] = [actualTrialType,"easy task"]
            if setupParameters['handedness'] == 'Left':
                current_slide = 10
                # practice.Parameters.append('hardTask')
                actualParameters[f"actual #{actualNum}"] = [actualTrialType,"hard task"]
            melon = 1
        elif bum == -1:
            if setupParameters['handedness'] == 'Right':
                current_slide = 11
                # practiceParameters.append('hardTask')
                actualParameters[f"actual #{actualNum}"] = [actualTrialType,"hard task"]
            if setupParameters['handedness'] == 'Left':
                current_slide = 11
                # practiceParameters.append('easyTask')
                actualParameters[f"actual #{actualNum}"] = [actualTrialType,"easy task"]
            melon = 1
        #print(actualParameters)
        countdown = 2

    if (32 <= current_slide <= 37) and melon == 0:
        time.sleep(3)
        if trialType == 1:
            if practiceNum < 4:
                if setupParameters['handedness'] == 'Right':
                    current_slide = random.randint(12,13)*2
                elif setupParameters['handedness'] == 'Left':
                    current_slide = random.randint(12,13)*2+1
                if current_slide == 24 or current_slide == 25:
                    #practiceParameters.append(f"gainTrial#{practiceNum}")
                    practiceTrialType = "gain trial"
                elif current_slide == 26 or current_slide == 27:
                    #practiceParameters.append(f"riskTrial#{practiceNum}")
                    practiceTrialType = "risk trial"
                #elif (practiceNum >= 4) and ((practiceNum - 1) % 3 == 0):
            elif (practiceNum >= 4):
                current_slide = 23
        elif trialType == 2:
            #if not((actualNum >= 4) and ((actualNum - 1) % 3 == 0)):
            if actualNum < actualAmount+1:
                if setupParameters['handedness'] == 'Right':
                    current_slide = random.randint(14,15)*2
                elif setupParameters['handedness'] == 'Left':
                    current_slide = random.randint(14,15)*2+1
                if current_slide == 28 or current_slide == 29:
                    #actualParameters.append(f"gainTrial#{actualNum}")
                    actualTrialType = "gain trial"
                elif current_slide == 30 or current_slide == 31:
                    #actualParameters.append(f"riskTrial#{actualNum}")
                    actualTrialType = "risk trial"
            elif actualNum == actualAmount+1:
                print(setupParameters)
                print(practiceParameters)
                print(actualParameters)
                pg.quit()
        melon = 1

    if current_slide == (SlideNum+1):
        current_slide = SlideNum

    # Draw the current slide to the screen (only if melon is set to 1, lets computer update only if prompted to)
    if melon == 1:
        screen.blit(slides[current_slide].image, (20, 75))
        melon = 2
        print(current_slide)

    # Update the display (only if melon is set to 2, resets melon back to 0)
    if melon == 2:
        pg.display.flip()
        melon = 0

    # Limit the frame rate
    clock.tick(FPS)

# Clean up
pg.quit()
