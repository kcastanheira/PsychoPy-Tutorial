from psychopy import visual, core, event, sound
import os
import pygame
import sys
import pandas as pd
import random
import numpy

Data_PID = []
Data_Practice = []
Data_RT = []
Data_Reward = []
Data_Repeat = []
Data_Color = []
Data_Number =[]
Data_Key = []
Data_Correct = []
Data_Bonus = []
Data_RunOrder = []
Data_Counterbalance = []
Bonus = 0

def show_me(str, color=(1,1,1), height=0.2):
        win.flip()
        text= visual.TextStim(win=win, text=str,color=color, height=height)

        text.draw()
        win.flip()
        
def show_me_2lines(str1, str2, color=(1,1,1), height=0.2):
        win.flip()
        text1= visual.TextStim(win=win, text=str1,color=color, height=height, pos=(0, 0.1))
        text2 =visual.TextStim(win=win, text=str2,color=color, height=height, pos=(0, -0.1))
        text1.draw()
        text2.draw()
        win.flip()

def quitSequence():
    win.close()
    core.quit()

def Practice():        
    Practice_data = pd.read_csv(dir_path+"/Switch_stimuli_0_1.csv")
    Practice_data.sample(frac=1)
    Numbers = Practice_data["Number"].tolist()
    Colors = Practice_data["Colour"].tolist()
    Repeat = Practice_data["Repeat"].tolist()
    Rewards = Practice_data["Reward"].tolist()
    for ind in range(0, len(Numbers)):
            if Rewards[ind] == "High":
                reward_stim = visual.ImageStim(win=win, image=dir_path+"/Images/quarter.png")
            else:
                reward_stim = visual.ImageStim(win=win, image=dir_path+"/Images/Cent.png")
            reward_stim.draw()
            win.flip()
            core.wait(2)
            show_me("+")
            core.wait(1)
            left_button = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/l.png", pos=(-0.3, -0.3))
            right_button = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/r.png", pos=(0.3,-0.3))
            if Colors[ind]=="blue":
                color = (0,0,1)
            elif Colors[ind]=="red":
                color= (1,0,0)
            question = visual.TextStim(win=win, text=str(Numbers[ind]), color=color, height=0.2)
                
            question.draw() 
            left_button.draw()
            right_button.draw()

            win.flip()
            stimulusOnset = core.MonotonicClock()
            buttons = event.waitKeys(maxWait=5, keyList=["left", "right", "escape"])
                
            if ((counterbalance ==1) & (Colors[ind]=="red"))  | ((counterbalance ==0) & (Colors[ind]=="blue")):
                if Numbers[ind] % 2 == 0:
                    answer = "right"
                else:
                    answer = "left"
            elif ((counterbalance ==1) & (Colors[ind]=="blue")) | ((counterbalance ==0) & (Colors[ind]=="red")):
                if Numbers[ind] > 5:
                    answer = "right"
                else:
                    answer = "left"

            if buttons is not None:
                    if(buttons[0]=="escape"):
                        quitSequence()
                    Data_RT.append(stimulusOnset.getTime())
                    Data_Key.append(buttons[0])
                    if (buttons[0] =="left"):
                            if (answer=="left"):
                                    Data_Correct.append(True)
                                    left_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/lg.png", pos=(-0.3, -0.3))
                                    right_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/r.png", pos=(0.3, -0.3))

                                    audio = sound.Sound(dir_path+'/Audio/ka-ching.wav')
                            else:
                                Data_Correct.append(False)
                                left_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/lr.png", pos=(-0.3, -0.3))
                                right_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/r.png", pos=(0.3, -0.3))
                                audio = sound.Sound(dir_path+'/Audio/Silent.wav')
                    elif buttons[0] =="right":
                            if (answer=="right"):
                                Data_Correct.append(True)
                                right_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/rg.png", pos=(0.3, -0.3))
                                left_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/l.png", pos=(-0.3, -0.3))
                                audio = sound.Sound(dir_path+'/Audio/ka-ching.wav')
                            else:
                                Data_Correct.append(False)
                                right_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/rr.png", pos=(0.3, -0.3))
                                left_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/l.png", pos=(-0.3, -0.3))
                                audio = sound.Sound(dir_path+'/Audio/Silent.wav') 
                        
            else:
                    Data_Key.append("None")
                    Data_RT.append(5)
                    Data_Correct.append(False)
                    right_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/rr.png", pos=(0.3, -0.3))
                    left_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/lr.png", pos=(-0.3, -0.3))
                    audio = sound.Sound(dir_path+'/Audio/Silent.wav')
        
            question.draw() 
            left_button.draw()
            right_button.draw()
            left_response.draw()
            right_response.draw()
            win.flip()
            audio.play()
            core.wait(1)
                
            Data_PID.append(PID)
            Data_Practice.append(True)
            Data_Reward.append(Rewards[ind])
            Data_Repeat.append(Repeat[ind])
            Data_Color.append(Colors[ind])
            Data_Number.append(Numbers[ind])
            Data_Bonus.append(Bonus)
            Data_RunOrder.append(RunOrder)
            Data_Counterbalance.append(counterbalance)
            show_me("+")
            core.wait(1.0)

def Run_Task():
        global Bonus   
        global RunOrder   
        win.flip()    
        Practice_data = pd.read_csv(dir_path+"/Switch_stimuli_"+str(RunOrder)+"_1.csv")
        
        Numbers = Practice_data["Number"].tolist()
        Colors = Practice_data["Colour"].tolist()
        Repeat = Practice_data["Repeat"].tolist()
        Rewards = Practice_data["Reward"].tolist()
        for ind in range(0, len(Numbers)):
                if Rewards[ind] == "High":
                    reward_stim = visual.ImageStim(win=win, image=dir_path+"/Images/quarter.png")
                else:
                    reward_stim = visual.ImageStim(win=win, image=dir_path+"/Images/Cent.png")
                reward_stim.draw()
                win.flip()
                core.wait(2)
                show_me("+")
                core.wait(1)
                left_button = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/l.png", pos=(-0.3, -0.3))
                right_button = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/r.png", pos=(0.3,-0.3))
                if Colors[ind]=="blue":
                    color = (0,0,1)
                elif Colors[ind]=="red":
                    color= (1,0,0)
                question = visual.TextStim(win=win, text=str(Numbers[ind]), color=color, height=0.2)

                question.draw() 
                left_button.draw()
                right_button.draw()

                win.flip()
                stimulusOnset = core.MonotonicClock()
                buttons = event.waitKeys(maxWait=5, keyList=["left", "right", "escape"])
                
                if ((counterbalance ==1) & (Colors[ind]=="red"))  | ((counterbalance ==0) & (Colors[ind]=="blue")):
                    if Numbers[ind] % 2 == 0:
                        answer = "right"
                    else:
                        answer = "left"
                elif ((counterbalance ==1) & (Colors[ind]=="blue")) | ((counterbalance ==0) & (Colors[ind]=="red")):
                    if Numbers[ind] > 5:
                        answer = "right"
                    else:
                        answer = "left"

                if ((counterbalance ==1) & (Colors[ind]=="red"))  | ((counterbalance ==0) & (Colors[ind]=="blue")):
                    if Numbers[ind] % 2 == 0:
                        answer = "right"
                    else:
                        answer = "left"
                elif ((counterbalance ==1) & (Colors[ind]=="blue")) | ((counterbalance ==0) & (Colors[ind]=="red")):
                    if Numbers[ind] > 5:
                        answer = "right"
                    else:
                        answer = "left"

                if buttons is not None:
                        if(buttons[0]=="escape"):
                            quitSequence()
                        Data_RT.append(stimulusOnset.getTime())
                        Data_Key.append(buttons[0])
                        if (buttons[0] =="left"):
                                if (answer=="left"):
                                        Data_Correct.append(True)
                                        left_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/lg.png", pos=(-0.3, -0.3))
                                        right_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/r.png", pos=(0.3, -0.3))
                                        audio = sound.Sound(dir_path+'/Audio/ka-ching.wav')
                                        if Rewards[ind]=="High":
                                            Bonus = Bonus +0.10
                                        else:
                                            Bonus = Bonus + 0.01
                                            
                                else:
                                    Data_Correct.append(False)
                                    left_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/lr.png", pos=(-0.3, -0.3))
                                    right_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/r.png", pos=(0.3, -0.3))
                                    audio = sound.Sound(dir_path+'/Audio/Silent.wav')
                        elif buttons[0] =="right":
                                if (answer=="right"):
                                    Data_Correct.append(True)
                                    right_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/rg.png", pos=(0.3, -0.3))
                                    left_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/l.png", pos=(-0.3, -0.3))
                                    audio = sound.Sound(dir_path+'/Audio/ka-ching.wav')
                                    if Rewards[ind]=="High":
                                            Bonus = Bonus +0.10
                                    else:
                                            Bonus = Bonus + 0.01
                                else:
                                    Data_Correct.append(False)
                                    right_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/rr.png", pos=(0.3, -0.3))
                                    left_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/l.png", pos=(-0.3, -0.3))
                                    audio = sound.Sound(dir_path+'/Audio/Silent.wav') 
                        
                else:
                        Data_Key.append("None")
                        Data_RT.append(5)
                        Data_Correct.append(False)
                        right_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/rr.png", pos=(0.3, -0.3))
                        left_response = visual.ImageStim(win=win, image=dir_path+"/Images/keyboard_keys/lr.png", pos=(-0.3, -0.3))
                        audio = sound.Sound(dir_path+'/Audio/Silent.wav')
        
                question.draw() 
                left_button.draw()
                right_button.draw()
                left_response.draw()
                right_response.draw()
                win.flip()
                audio.play()
                core.wait(1)
                
                Data_PID.append(PID)
                Data_Practice.append(True)
                Data_Reward.append(Rewards[ind])
                Data_Repeat.append(Repeat[ind])
                Data_Color.append(Colors[ind])
                Data_Number.append(Numbers[ind])
                Data_Bonus.append(Bonus)
                Data_RunOrder.append(RunOrder)
                Data_Counterbalance.append(counterbalance)
                show_me("+")
                core.wait(1.0)
        
def showInstructions(End=False):
    if End== True: 
        instruct= visual.ImageStim(win=win, image=dir_path+"/Instructions/Slide6.jpeg")
        instruct.draw()
        win.flip()
        event.clearEvents()
        buttons=[]
        buttons= event.waitKeys(keyList=["space"])
        if len(buttons)<0:
            if buttons[0]:
                quitSequence()
    else:
        if counterbalance==1:
            slides = [1,2,3,5]
        else:
            slides = [1,2,4,5]
        for i in slides: 
                instruct = visual.ImageStim(win=win, image=dir_path+"/Instructions/Slide"+str(i)+".jpeg")
                instruct.draw()
                win.flip()
                buttons= event.waitKeys(keyList=["space"])
                        
def setOutputDir():
        global PID
        global dir_path
        global outputDirectory
        global counterbalance
        global RunOrder
        counterbalance = random.sample([0, 1], 1)[0]
        RunOrder = random.sample([1, 2, 3], 1)[0]
        dir_path= os.path.dirname(os.path.realpath(__file__))
        PID= input("Particiapnt ID (e.g. 001):\n")
        PID = str(PID)
        outputDirectory=dir_path+"/DATA/"+PID
        if os.path.isdir(outputDirectory):
            exists= True
            while exists:
                n= len(PID)
                PID= int(PID)+1
                PID= str(PID)
                outputDirectory= outputDirectory[:-n]+PID
                exists= os.path.isdir(outputDirectory)
                print("PID already exists, setting PID to: %d" %(int(PID)))     
        os.mkdir(outputDirectory)
	


if __name__ == '__main__':			
    setOutputDir()
    pygame.init()

        
    xc= 1280
    yc=800
    win = visual.Window((xc, yc), fullscr=True, color=(-1,-1,-1), winType="pygame")
    win.mouseVisible = False
    event.Mouse(visible=False)

            
    showInstructions(End=False)
    Practice()
    show_me_2lines("Any Questions?", "Press SPACE to being the task")
    buttons = event.waitKeys(keyList=["space"])
    Run_Task()
    show_me("Congratulations! You won $" + str(Bonus))
    core.wait(5)
    showInstructions(End=True)

    output_data = {'PID':Data_PID,'RT':Data_RT, "Reward":Data_Reward, "Practice":Data_Practice, "Color":Data_Color, "Number":Data_Number, "Key":Data_Key, "Correct":Data_Correct, "Bonus":Data_Bonus, "RunOrder":Data_RunOrder, "Counterbalance":Data_Counterbalance}
    output_data = pd.DataFrame(output_data)
    output_data.to_csv(outputDirectory+"/"+PID+"_Switch_data.csv", mode="a", index=False, na_rep="NA", header=True)
    win.close()
    quitSequence()



