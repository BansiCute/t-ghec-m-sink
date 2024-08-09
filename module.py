import cv2
import numpy as np
import os
import time

def cap():
    os.system("adb -s emulator-5554 exec-out screencap -p > name.png")

def click(img):
    time.sleep(1)
    cap()
    #variables
    img1 = cv2.imread('name.png')
    img2 = cv2.imread(img)


    #gray
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    #find
    result = cv2.matchTemplate(img1_gray, img2_gray, cv2.TM_CCOEFF_NORMED)

    #pos
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    #scale
    top_left = max_loc
    bottom_right = (top_left[0] + img2.shape[1], top_left[1] + img2.shape[0])
    center_x = top_left[0] + img2.shape[1] // 2
    center_y = top_left[1] + img2.shape[0] // 2
    cv2.rectangle(img1, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imshow('Detected', img1)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    # #in
    # print(f"Vị trí phát hiện: ({center_x}, {center_y})")

    #click
    os.system(f'adb -s emulator-5554 shell input tap {center_x} {center_y}')
    print("clicked "+img)

def find(img1, img2):
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    result = cv2.matchTemplate(img1_gray, img2_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > 0.8:  
        return max_loc
    else:
        return None
def encounter_main():
    time.sleep(2)
    os.system("adb -s emulator-5554 exec-out screencap -p > name.png")
    img1 = cv2.imread('name.png')
    img2 = cv2.imread('isvang.png')
    img3 = cv2.imread('iswater.png')

    if img1 is None or img2 is None or img3 is None:
        print("Không thể mở một hoặc nhiều ảnh.")
        return

    
    location_img2 = find(img1, img2)
    
    if location_img2:
        #vang
        click("isvang.png")
        top_left = location_img2
        bottom_right = (top_left[0] + img2.shape[1], top_left[1] + img2.shape[0])
        center_x = top_left[0] + img2.shape[1] // 2
        center_y = top_left[1] + img2.shape[0] // 2
        os.system(f'adb -s emulator-5554 shell input tap {center_x} {center_y}')
        #print("da bam img2")
        click("isvang_value.png")
        click("confirm_act.png")
        click("recgained.png")
        click("isvang.png")
        click("alright.png")
        click("confirm.png")
        
    else:
        location_img3 = find(img1, img3)
        
        if location_img3:
            #water
            click("iswater.png")
            top_left = location_img3
            bottom_right = (top_left[0] + img3.shape[1], top_left[1] + img3.shape[0])
            center_x = top_left[0] + img3.shape[1] // 2
            center_y = top_left[1] + img3.shape[0] // 2
            
            os.system(f'adb -s emulator-5554 shell input tap {center_x} {center_y}')
            #print("da bam img3")
            click("iswater_value.png")
            click("confirm_act.png")
            click("recgained.png")
            click("iswater.png")
            click("alright.png")
            click("confirm.png")
            
            
        else:
            print("404 not found")
    click("back.png")

def scroll(x1, y1, x2, y2, duration=500):
    os.system(f"adb shell input swipe {x1} {y1} {x2} {y2} {duration}")





click("resume.png")
time.sleep(3)
scroll(200, 500, 1000, 500)
scroll(250, 800, 250, 400)
click("enconter.png")
encounter_main()
time.sleep(1)



click("resume.png")
time.sleep(3)
scroll(1000, 500, 200, 500)
scroll(250, 800, 250, 400)
click("enconter.png")
encounter_main()
time.sleep(1)



click("resume.png")
time.sleep(3)
click("next_day.png")
time.sleep(10)

click("day.png")
click("skip.png")
click("confirm2.png")
click("next_day.png")
time.sleep(8)

click("base.png")
click("upgrade.png")
click("upgrade2.png")
time.sleep(2)
click("back.png")
click("back.png")
click("back.png")
time.sleep(1)


click("day.png")
click("skip.png")
click("confirm2.png")
time.sleep(1)
click("next_day.png")
time.sleep(8)

click("survived.png")
time.sleep(5)
click("start_today.png")
time.sleep(2)

















































