# -*- coding: UTF-8 -*-

import os,sys,time
from useriface import device
from useriface import hostpc
from useriface import logger

testtime = 1000
SN = '0123456789ABCDEF'
dev = device.Device(SN)
ui = dev.uidevice
pc = hostpc.Host(SN)
log = logger.Logger(__file__)
log.addLog2file('Click_all_camera_items.log')


def WatcherButton():
    
    log.info("button watcher")
    ui.watcher("button").when(resourceId='com.android.gallery3d:id/right_btn').when(className='android.widget.Button').when(text='确定').click(text='确定')


def Normal():

    log.info("Capture in Normal")

    ui.press.home()
    time.sleep(3)
    ui(className='android.widget.TextView')[2].click()
    time.sleep(3)
    ui(className='android.widget.TextView')[2].click()
    time.sleep(20)
    ui(resourceId='com.android.gallery3d:id/mode_photo').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/onscreen_gesture_shot_picker').click()
    time.sleep(5)
    ui(resourceId='com.android.gallery3d:id/shutter_button_photo').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/onscreen_gesture_shot_picker').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/shutter_button_photo').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/onscreen_smile_shot_picker').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/shutter_button_photo').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/onscreen_smile_shot_picker').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/shutter_button_photo').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/onscreen_hdr_picker').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/shutter_button_photo').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/onscreen_hdr_picker').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/shutter_button_photo').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/lomo_effect_indicator').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/textureview')[0].click()   
    time.sleep(3)  


def Panorama():

    log.info("Capture in Panorama")

    ui.press.home()
    time.sleep(3)
    ui(className='android.widget.TextView')[2].click()
    time.sleep(3)
    ui(className='android.widget.TextView')[2].click()
    time.sleep(10)
    ui(resourceId='com.android.gallery3d:id/mode_panorama').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/shutter_button_photo').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/btn_cancel').click()
    time.sleep(3)

   


def Angle():

    log.info("Capture in Angle")
   
    ui.press.home()
    time.sleep(3)
    ui(className='android.widget.TextView')[2].click()
    time.sleep(3)
    ui(className='android.widget.TextView')[2].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/mode_mav').click()
    time.sleep(10)
    ui(resourceId='com.android.gallery3d:id/shutter_button_photo').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/btn_cancel').click()
    time.sleep(3)
    


def Setting1():

    log.info("Check Setting1")
    
    ui.press.back()
    ui.press.home()
    time.sleep(3)
    ui(className='android.widget.TextView')[2].click()
    time.sleep(3)
    ui(className='android.widget.TextView')[2].click()
    time.sleep(5)
    ui(resourceId='com.android.gallery3d:id/mode_photo').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_indicator').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch',className='android.widget.Switch').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch',className='android.widget.Switch').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title')[1].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title',text='关闭').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title')[2].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title',text='+2').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title')[3].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title',text='自动').click()   
    time.sleep(3)
    ui.swipe(400,400,400,100,30)
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title')[1].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title',text='日光').click()   
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title')[2].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/radio3')[0].click()
    time.sleep(1)
    ui(resourceId='com.android.gallery3d:id/radio3')[1].click()
    time.sleep(1)
    ui.swipe(400,360,400,130,30)
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/radio1')[0].click()
    time.sleep(1)
    ui(resourceId='com.android.gallery3d:id/radio1')[1].click()
    time.sleep(1)
    ui.press.back()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title')[3].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title',text='关').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title')[4].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/rotate_dialog_button2').click()
    time.sleep(3)



def Setting2():

    log.info("Check Setting2")

    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_indicator').click()
    time.sleep(3)
#    ui(index='1',className='android.widget.ImageView').click()
    ui.swipe(600,300,180,300,30)
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch')[0].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch')[0].click()
    time.sleep(3)    
    ui(resourceId='com.android.gallery3d:id/setting_switch')[1].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch')[1].click()
    time.sleep(3)       
    ui(resourceId='com.android.gallery3d:id/setting_switch')[2].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch')[2].click()
    time.sleep(3) 
    ui(resourceId='com.android.gallery3d:id/title')[3].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/radio')[1].click()
    time.sleep(3) 
    ui(resourceId='com.android.gallery3d:id/title')[4].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/radio')[1].click()
    time.sleep(3)
    ui.swipe(420,420,420,120,30)
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title')[2].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/radio')[0].click()
    time.sleep(3) 
    ui(resourceId='com.android.gallery3d:id/title')[3].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/radio')[0].click()
    time.sleep(3) 
    ui(resourceId='com.android.gallery3d:id/title')[4].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/radio')[2].click()
    time.sleep(3)
    ui.press.back()


def Setting3():

    log.info("Check Setting3")

    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_indicator').click()
    time.sleep(3)
#    ui(className='android.widget.ImageView',index='2').click()
    ui.swipe(600,300,180,300,30)
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch')[0].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch')[0].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch')[1].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch')[1].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch')[2].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/setting_switch')[2].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title')[3].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/radio')[0].click()
    time.sleep(3)
    ui.swipe(420,420,420,120,30)
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title')[3].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/radio')[2].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/title')[4].click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/radio')[2].click()
    time.sleep(3)
    ui.press.back()
    time.sleep(3)

    log.info("Recording video")
    
    ui(resourceId='com.android.gallery3d:id/shutter_button_video').click()
    time.sleep(15)
    ui(resourceId='com.android.gallery3d:id/shutter_button_photo').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/btn_pause_resume').click()
    time.sleep(5)
    ui(resourceId='com.android.gallery3d:id/btn_pause_resume').click()
    time.sleep(5)
    ui(resourceId='com.android.gallery3d:id/shutter_button_video').click()
    time.sleep(8)
    ui.press.back()


def Deleteall():

    log.info("Delete all pictures\n")

    time.sleep(3)
    ui.press.home()
    time.sleep(3)
    ui(className='android.widget.TextView')[0].click()
    time.sleep(5)
    ui(className='android.widget.ImageButton').click()
    time.sleep(3)
    ui(resourceId='android:id/title').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/selection_menu').click()
    time.sleep(3)
    ui(resourceId='android:id/text1').click()
    time.sleep(3)
    ui(resourceId='com.android.gallery3d:id/action_delete').click()
    time.sleep(3)
    ui(resourceId='android:id/button1').click()
    time.sleep(15)
    ui.press.home()
    
    
'''
ui(resourceId='com.android.gallery3d:id/btn_done'全景

'''


if __name__ == '__main__':

    for i in range(1,testtime):

        log.info("+++++++++++ testtime: %d ++++++++++" %i)

        WatcherButton()
        Normal()
        Panorama()
        Angle()
        Setting1()
        Setting2()
        Setting3()
        Deleteall()



    
    
