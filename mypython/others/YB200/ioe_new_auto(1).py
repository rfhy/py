# -*- encoding: UTF-8 -*-

import os,sys
from datetime import datetime
import xlrd
import xlwt

s = [u'定格1',u'定格2',u'定格3',u'定格4',u'定格5']
t = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_")
global f
f = xlwt.Workbook()
w1 = []
w2 = []
w3 = []
w4 = []
w5 = []
a23 = []
a24 = []
a25 = []

x = []
for r in range(2,12):
  for u in range(4,9):
    v = (r,u)
    x.append(v)

x2 = []
for r in range(12,22):
  for u in range(4,9):
    v = (r,u)
    x2.append(v)

x3 = []
for r in range(22,32):
  for u in range(4,9):
    v = (r,u)
    x3.append(v)

y = []
for r in range(2,42):
  for u in range(13,18):
    v = (r,u)
    y.append(v)

z = []
for r in range(2,30):
  for u in range(22,27):
    v = (r,u)
    z.append(v)


fn = 'dir_video_zhangqiwen151_350_19700101_08_12_31.txt' #log名
event = ['no move','up','down','left','right']
motion = ['palm ','fist ']


def Logfile(str):
    logs = open(t + u"手势头肩log.txt","a+") 
    logs.write(str+"\n")
    logs.flush()
    logs.close()
    print(str)


#excel格式
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



def Result(sheet1,my):

  #建立excel
  row1 = [u'测试项',u'左右手',u'距离']  + s
  row2 = [u'测试项',u'距离',u'动作']  + s
  row3 = [u'测试项',u'距离',u'角度'] + s

  c1 = [u'手掌识别',u'拳头识别',u'掌变拳']
  c2 = 3 * [u'右手',u'左手']
  c3 = 6 * ['1m','2m','3m','4m','5m']
    
  c10 = [u'右手移动',u'左手移动']
  c11 = 2 * ['1m','2m','3m','4m','5m']
  c12 = 10 * [u'向上',u'向下',u'向左',u'向右']
    
  c19 = [u'头肩识别']
  c20 = ['1m','2m','3m','4m','5m','6m','7m']
  c21 = 7 * [u'0度',u'90度',u'180度',u'270度']


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
  while i < 28*len(c19):
      sheet1.write_merge(i,i+27,19,19,c19[j],set_style())      
      i += 28
      j += 1
        
  i, j = 2, 0        
  while i < 4*len(c20):

      sheet1.write_merge(i,i+3,20,20,c20[j],set_style())      
      i += 4
      j += 1

  for i in range(0,len(c21)):
      sheet1.write(2+i,21,c21[i],set_style())


  f1 = open(fn).read()
  log = f1.split("===========start,")
  d = len(log)



  if 0 < d < 451:
    for i in range(1,d):

      name = log[i].split(".mp4")[0].split("/")[-1]
      run = int(name)

      if run in range(1,51):
      
        a7 = []
        a8 = []
        a9 = []
        a10 = []
        lk = log[i].split("====loop,")
        for a in range(1,len(lk)):
          Logfile("============== %d -- %d"%(run,a))
          a6 = [20000]

          for rr in range(1,10):
            if lk[a].find("head:%d"%rr) != -1:
              ab = lk[a].split("head:%d"%rr)[0].split("): ")[-1].split(",")[0].split()[0]
              a6.append(int(ab))
              Logfile("find %d head time: %s" %(rr,ab))
          a10.append(min(a6))

          if a10[-1] != 20000:
            a7.append(a10[-1])
          if a10[-1] == 20000:
            a9.append(a10[-1])      
        w1.append(len(a7)/float(len(lk)-1))
        a25.append(len(a9))
        a24.append(sum(a7))
        a23.append(len(a7))


      if run in range(51,101):
        a11 = []
        a12 = []
        a13 = []
        a14 = []
        lk = log[i].split("====loop,")
        for a in range(1,len(lk)):
          Logfile("============== %d -- %d"%(run,a))

          if i <= 1000:
            if lk[a].find("fist:1") == -1:
              a11.append(10000)
              Logfile("find fist time: max")
            else:
              aa = lk[a].split("fist:1")[0].split("): ")[-1].split(",")[0].split()[0]
              a11.append(int(aa))
              Logfile("find fist time: %s" %aa)

            if lk[a].find("palm:1") != -1:
              Logfile("***** recognition fail")
            if lk[a].find("head:1") == -1:
              Logfile("find head time: max")
            if lk[a].find("palm to fist") != -1:
              Logfile("## find palm to fist")

          if a11[-1] <= 5000:
            a12.append(a11[-1])
            if a11[-1] <= 2000:
              a13.append(a11[-1])
          if a11[-1] > 5000:
            a14.append(a11[-1])     
        w2.append(len(a12)/float(len(lk)-1))
        
      if run in range(101,151):
        a15 = []
        a16 = []
        lk = log[i].split("====loop,")
        for a in range(1,len(lk)):
          Logfile("============== %d -- %d"%(run,a))

          if lk[a].find("head:1") == -1:
            Logfile("find head time: max")
          if lk[a].find("palm:1") == -1:
            Logfile("find palm time: max")
          if lk[a].find("palm to fist") == -1:
            a15.append(15000)
            a16.append(a15[-1])
            Logfile("find palm-fist time: max")
          else:
            aa = lk[a].split("palm to fist")[0].split("): ")[-1].split(",")[0].split()[0]
            a15.append(int(aa))
            Logfile("find palm-fist time: %s" %aa)

          if lk[a].find("palm:1") == -1:
            Logfile("find palm time: max")
          else:
            aa = lk[a].split("palm:1")[0].split("): ")[-1].split(",")[0].split()[0]
            Logfile("find palm time: %s" %aa)   
        w3.append(len(a16)/float(len(lk)-1))

      if run in range(151,351):
        ar = []
        a31 = []
        a32 = []
        a33 = []
        a34 = []
        a35 = []
        a36 = []
        a37 = []
        a38 = []
        a39 = []
        a40 = []
        lk = log[i].split("====loop,")
        for a in range(1,len(lk)):
          m =[a31,a32,a33,a34,a35,a36,a37,a38,a39,a40]
          Logfile("============== %d -- %d"%(run,a))
              
          if lk[a].find("palm to fist") != -1:
            Logfile("## find palm to fist")
          if lk[a].find("head:1") == -1:
            Logfile("find head time: max")
          if lk[a].find("palm:1") == -1:
            Logfile("find palm time: max")
          if lk[a].find("fist:1") != -1:
            Logfile("***** recognition fail")
            
          for s1 in motion:
            for s2 in event:              
              ev = lk[a].count(s1 + s2)
              ar.append(ev)
              Logfile(s1 + s2 + " : %d"%ev)
          
          for t in range(0,10):
            m[t].append(ar[t])

        co = run % 20  
        if 10 < co < 16:
          r = float(sum(m[1]))/float(len(m[1]))
          w4.append(r)
          
        if 15 < co < 20 or co == 0:
          r = float(sum(m[2]))/float(len(m[2]))
          w4.append(r)
        if 0 < co < 6:
          r = float(sum(m[3]))/float(len(m[3]))
          w4.append(r)          
        if 5 < co < 11:
          r = float(sum(m[4]))/float(len(m[4]))
          w4.append(r)
          
      if run in range(351,451):
        a46 = [10000]
        a47 = []
        a48 = []
        a49 = []
        a50 = []
        lk = log[i].split("====loop,")
        for a in range(1,len(lk)):
          Logfile("============== %d -- %d"%(run,a))

          for i1 in range(1,10):
            if lk[a].find("head:%d"%i1) != -1:
              ab = lk[a].split("head:%d"%i1)[0].split("): ")[-1].split(",")[0].split()[0]
              a46.append(int(ab))
              Logfile("find %d head time: %s" %(i1,ab))
          a50.append(min(a46))
            

          if 0 < a50[-1] <= 5000:
            a47.append(a50[-1])
            if a50[-1] <= 2000:
              a48.append(a50[-1])
          if a50[-1] == 10000:
            a49.append(a50[-1])      
        w5.append(len(a47)/float(len(lk)-1))
         

  Logfile("\n-----: %s" %fn)
  Logfile("total time: %d" %sum(a24))
  Logfile("total count: %d" %sum(a23))
  Logfile("can no find head times: %d"%sum(a25))
          
  if sum(a23) != 0:
    ave = float(sum(a24))/sum(a23)
    Logfile("average time: %.2f" %ave)
  

  
  for i in range(0,len(w1)):
    sheet1.write(x[i][0],x[i][1],w1[i],set_style())

  for i in range(0,len(w2)):
    sheet1.write(x2[i][0],x2[i][1],w2[i],set_style())

  for i in range(0,len(w3)):
    sheet1.write(x3[i][0],x3[i][1],w3[i],set_style())

  for i in range(0,len(w4)):
    sheet1.write(y[i][0],y[i][1],w4[i],set_style())
    
  for i in range(0,len(w5)):
    sheet1.write(z[i][0],z[i][1],w5[i],set_style())  
          
    
 
if __name__ == '__main__':
  
  Result('sheet1','lirun')
  f.save(t + u'手势算法测试.xls')
