# -*- encoding: UTF-8 -*-

import os,sys
import xlrd
import xlwt
from pyExcelerator import *
from xlutils.copy import copy

#fn = 'auto_test_20170211_13_23_19.log'
w = Workbook()
ws = w.add_sheet('move')
global m
m = 0
title = [u'地点',u'光源',u'测试人',u'性别',u'手势',u'背景',u'亮度',u'区域',u'距离',u'左右手',u'画面人数',u'动作',u'主观手势稳定时间',u'算法取帧时间',u'算法取帧与主观时间差',u'算法计算时间',u'算法识别到手势时间',u'丢失次数',u'向上',u'向下',u'向左',u'向右',u'静止',u'平均']


y1 = ['jsf_sun_970lx_wood_lirun_male_right1_palm_3m_area3',
      'jsf_sun_970lx_wood_lirun_male_letf1_palm_3m_area3',
      'jsf_sun_970lx_white-curtain_lirun_male_right1_palm_3m_area3',
      'jsf_sun_970lx_white-curtain_lirun_male_left1_palm_3m_area3',
      'hlab_surface_400lx_white-wall_lirun_male_right1_palm_3m_area3',
      'hlab_surface_400lx_wood_lirun_male_right1_palm_3m_area3',
      'jds_point_80lx_complex_lirun_male_right1_palm_3m_area3',
      'jds_point_80lx_complex_lirun_male_right1_palm_3m_area3'

      'jsf_sun_970lx_wood_lirun_male_right1_fist_3m_area3',
      'jsf_sun_970lx_wood_lirun_male_letf1_fist_3m_area3',
      'jsf_sun_970lx_white-curtain_lirun_male_right1_fist_3m_area3',
      'jsf_sun_970lx_white-curtain_lirun_male_left1_fist_3m_area3',
      'hlab_surface_400lx_white-wall_lirun_male_right1_fist_3m_area3',
      'hlab_surface_400lx_wood_lirun_male_right1_fist_3m_area3',
      'jds_point_80lx_complex_lirun_male_right1_fist_3m_area3',
      'jds_point_80lx_complex_lirun_male_right1_fist_3m_area3'
      ]


if m == 0:
    for n in range(len(title)):                            
        ws.write(m,n,title[n])
        w.save("smartcontrol_test.xls")

        

ys = {'jsf':u'健身房','plab':u'图像实验室','hlab':u'硬件实验室',
      'xjs':u'宣讲室','jds':u'接待室',
      'sun':u'阳光','point':u'点光源','surface':u'平面光源',
      'male':u'男','female':u'女',
      'wood':u'木色背景','white-wall':u'白墙背景',
      'white-curtain':u'白色窗帘','complex':u'复杂背景',
      'right1':u'右手','left1':u'左手',
      'palm':u'手掌','fist':u'拳头',
      'up':u'向上移动','down':u'向下移动','static':u'静止识别',
      'left':u'向左移动','right':u'向右移动',
      'lirun':u'姜立润','lijiao':u'李跤','yanmei':u'邱燕梅','fengtao':u'冯涛',
      'xiaoyu':u'吴李接','shouqian':u'韩守谦',
      'zhijia':u'林志嘉','wenjuan':u'张雯娟'
      }


def Logfile(str):

    lirun = open("smartcontrol.log","a+")
    lirun.write(str + "\n")
    lirun.flush()
    lirun.close()   
    print(str)

def Errlog(str):

    Logfile(str)
    global m
    m = m + 1
    ws.write(m,0,str)
    w.save("smartcontrol_test.xls")



def test():

    at = []

    #jds_sun_300lx_complex_lirun_female_right1_palm_3m_area3_right_5_25_30
    #jsf_sun_300lx_white-curtain_1_area2

    for fn in os.listdir(os.getcwd()+"\\log\\"):
        if os.path.splitext(fn)[1] == '.log':

            f = open(os.getcwd()+"\\log\\"+fn).read()
            log = f.split("============================")
            d = len(log)

            if d > 1:#是否有需要的log
                for i in range(1,d):

                    lk = log[i].split("testing /mnt/sdcard/test/video/")
                    
                    if len(lk) > 1:#是否找到测试文件名

                        testfn = lk[1].split(".mp4")[0]
                        s1 = testfn.split('_')
                        
                        
                        if s1[0].isdigit() == True:#文件名数字开始
                            s = y1[int(s1[0])].split("_") + s1[1:]
                            name = s[10]
                            time1 = 1
                            t1 = 1#录视频前，手势已经做好准备，第一帧已经有手势
                            fps = 30
                            t11 = 1000 * t1/fps
                            

                            Logfile("test file: " + testfn + "\n")

                            check = log[i].split("hand found, idx:")
                            
                            if len(check) > 1:#是否发现手势

                                idx1 = int(check[1].split(",")[0])

                                t = int(log[i].split("hiarsiRun use")[1].split("ms")[0])
                                t2 = (1000 * idx1)/fps
                                t3 = t2 + t

                                Logfile("find hand frame: %d, time is %d ms, algorithm run time: %d ms, total time is:%d"%(idx1,t2,t,t3 - t11))

                                Logfile("except frame is: %d , time is: %d"%(t1,t11))

                                lost = log[i].count("hand lost,")

                                Logfile("lost hand: " + str(lost) + " times")
                                 
                                
                                res2 = [str(t2) + ' ms',str(t2 - t11) + ' ms',str(t) + ' ms',str(t3 - t11) + ' ms',lost]

                                res4 = []
                                for u in range(0,5):
                                    cc = log[i].split("==" + s[7])[1].split('\r\n')[0].split()[u]
                                    it = cc.split(":")
                                    res4.append(it[1])
                                    Logfile(s[7] + " " + it[0] + " " + it[1] + " times")
                                    if it[0] == s[10]:
                                        pass
                                        

                            if len(check) == 0:#未发现手势

                                Logfile("can not find hand in log.")
                                res2 = ['can not find hand in log.'] + 6 * ['']
                                
                            res1 = [ys[s[0]],ys[s[1]],ys[s[4]],ys[s[5]],ys[s[7]],ys[s[3]],s[2],s[9],s[8],ys[s[6]],s[11],ys[s[10]],str(t11) + ' ms']
                            res = res1 + res2 + res4

                            at.append(res)



                        if len(s1) == 6:

                            pass
                            #头肩检测，待完善

                        if s1[0].isdigit() == False:#文件名不对
                            Errlog("test video name is wrong: " + testfn)         

                    else:
                        Errlog("can not find test video name in log.")

                global m
                m = m + 1        
                at1 = sorted(at)                   

                if m > 0:
                    for k in range(len(at1)):

                        for n in range(len(at1[0])):
                            ws.write(m,n,at1[k][n])
                            if m % 10 == 0:
                                print("write m: " + str(m)+" n:" +str(n))
                            w.save("smartcontrol_test.xls")
                        m = m + 1
                        
            else:
                Errlog("invalid log.")
            



if __name__ == '__main__':


    test()
