# -*- encoding: UTF-8 -*-

import os,sys
from datetime import datetime
import xlrd
import xlwt

s = [u'定格1',u'定格2',u'定格3',u'定格4',u'定格5']
t = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_")
global f
f = xlwt.Workbook()


def set_style(name='Times New Roman',height=220,bold=False):
  style = xlwt.XFStyle() # 初始化样式

  alignment = xlwt.Alignment()
  alignment.horz = xlwt.Alignment.HORZ_CENTER
  alignment.vert = xlwt.Alignment.VERT_CENTER
 
  font = xlwt.Font() # 为样式创建字体
  font.name = name # 'Times New Roman'
  font.bold = bold
  font.color_index = 4
  font.height = height
 
  borders= xlwt.Borders()
  borders.left= 1
  borders.right= 1
  borders.top= 1
  borders.bottom= 1

  style.font = font
  style.borders = borders
  style.alignment = alignment
 
  return style


def creat_xlsx(sheet1,my):

    row1 = [u'测试项',u'左右手',u'距离']  + s
    row2 = [u'测试项',u'距离',u'动作']  + s
    row3 = [u'测试项',u'距离',u'角度'] + s

    c1 = [u'手掌识别',u'拳头识别']
    c2 = 2 * [u'右手',u'左手']
    c3 = 4 * ['1m','2m','3m','4m','5m']
    
    c10 = [u'右手移动',u'左手移动']
    c11 = 2 * ['1m','2m','3m','4m','5m']
    c12 = 10 * [u'向上',u'向下',u'向左',u'向右']
    
    c19 = [u'头肩识别']
    c20 = ['1m','2m','3m','4m','5m']
    c21 = 5 * [u'0度',u'90度',u'180度',u'270度']


    sheet1 = f.add_sheet(my,cell_overwrite_ok=True)

    for i in range(0,len(row1)):
        sheet1.write(1,i+1,row1[i],set_style())
    for i in range(0,len(row1)):
        sheet1.write(1,i+10,row2[i],set_style())
    for i in range(0,len(row1)):
        sheet1.write(1,i+19,row3[i],set_style())

    i, j = 2, 0
    while i < 10*len(c1):
        sheet1.write_merge(i,i+9,1,1,c1[j],set_style())      
        i += 10
        j += 1
        
    i, j = 2, 0        
    while i < 5*len(c2):
        sheet1.write_merge(i,i+4,2,2,c2[j],set_style())      
        i += 5
        j += 1

    for i in range(0,len(c3)):
        sheet1.write(2+i,3,c3[i],set_style())

        
    i, j = 2, 0
    while i < 20*len(c10):
        sheet1.write_merge(i,i+19,10,10,c10[j],set_style())      
        i += 20
        j += 1
        
    i, j = 2, 0        
    while i < 4*len(c11):

        sheet1.write_merge(i,i+3,11,11,c11[j],set_style())      
        i += 4
        j += 1

    for i in range(0,len(c12)):
        sheet1.write(2+i,12,c12[i],set_style())

    i, j = 2, 0
    while i < 20*len(c19):
        sheet1.write_merge(i,i+19,19,19,c19[j],set_style())      
        i += 20
        j += 1
        
    i, j = 2, 0        
    while i < 4*len(c20):

        sheet1.write_merge(i,i+3,20,20,c20[j],set_style())      
        i += 4
        j += 1

    for i in range(0,len(c21)):
        sheet1.write(2+i,21,c21[i],set_style())
    

 
if __name__ == '__main__':
  #generate_workbook()
  #read_excel()
  creat_xlsx('sheet1','lirun')
  creat_xlsx('sheet2','qq')
  creat_xlsx('sheet3','lijiao')
  sheet1 = 'sheet4'
  my = 'wenjuan'
  creat_xlsx(sheet1,my)

  sheet1 = 'sheet5'
  my = '11'
  creat_xlsx(sheet1,my)
  
  f.save(t + u'手势算法测试.xls')
