# -*- coding: utf-8 -*-
import urllib
import urllib2
import time
import json
import subprocess
import os,sys  
import zipfile
import shutil
import xlwt
import xlsxwriter
import MyUtil
import datetime
sn = MyUtil.Getsn()
def changeNumToChar(toSmallChar=None, toBigChar=None):  
  #n = toSmallChar and toSmallChar or toBigChar  
  #c = toSmallChar and ord('A')-1 or ord('a')-1  
  init_number = 0  
  increment = 0  
  res_char = ''  
  if not toSmallChar and not toBigChar:  
     return ''  
  else:  
      if toBigChar:  
        init_number = toBigChar  
        increment = ord('A') - 1  
      else:  
        init_number = toSmallChar  
        increment = ord('a') - 1  
  
  shang,yu = divmod(init_number, 26)  
  char = chr(yu + increment)  
  res_char = char*(shang + 1)  
  #for i in range(shang + 1):  
  #   char = chr(yu + increment)  
  #  res_char += char  
  
  return res_char  

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList
def memoryprocrank():
    time.sleep(1800)
##    sn=" -s 101100000011101A "
    if os.path.isdir("D:\\script\\memoryresult"):
        shutil.rmtree("D:\\script\\memoryresult")
##    strtime = str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    os.system("adb -s "+sn+" shell \"busybox pkill sh")
    os.system("adb -s "+sn+" pull /sdcard/memoryresult  memoryresult")
    time.sleep(30)

    
   #save  memoryresult
    listzip = GetFileList('D:\\script\\memoryresult',[])
    dicmemory = {}
    timelist = []
    timefirstflag = True
    if len(listzip) ==0 :
      return 0
    for e in listzip:
        print "###########################"
        print e
        f = open(e,'r')
        memoryresult = f.readline()
        memoryresult = f.readline()
        firstlineflag = True
        pssmemory = []
        flag=False
        while(len(memoryresult) >0):
            listmemory = memoryresult.split('  ')
            for l in listmemory :
              if '' == l:
                listmemory.remove(l)
                
            print listmemory
            if timefirstflag:
                timelist.append(listmemory[0])
            if len(listmemory) < 3:
                flag=True
                break
            pssmemory .append(int(listmemory[4].replace('K','').strip()))
            memoryresult = f.readline()

        print len(pssmemory)
        print len(timelist)
        f.close()    
        timefirstflag = False
        if flag ==  False:
            basename = os.path.basename(e)
            dicmemory[basename.split('.log')[0]]= pssmemory

    
##    keylist=[]
##    printstr = "<html><table  border=\"1\" cellspacing=\"1\" > <th  style=\"word-break:break-all\" width=\"400\">"+"Time  <th/>"
##    for key in dicmemory:
##        printstr += "<th  style=\"word-break:break-all\" width=\"400\"  >"+key+"  "+"<th/>"
##        keylist.append(key)
##
##    print keylist
##    i=0    
##    for t in timelist:
##        printstr += "<tr> <td  width=\"400\" >"+ t+"<td/>"
##        for k in keylist:
##            printstr += "<td   width=\"400\" >"+ dicmemory[k][i] + "<td/>"
##
##        printstr += "</tr>"
##        i+=1
##
##    printstr += "<table/><html/>"
##    f = open('c:\\test.html','w')
##    f.write(printstr)
##    f.close()
##    print "######################################################"
##    print printstr
        
    apknamelist=[]
    apknamelist.append("Time")
    
    for key in dicmemory:
        apknamelist.append(key)

    print apknamelist

    #xlwt
    #创建workbook和sheet对象
##    datetime = time.strftime('%Y%m%d%H%M%S')
##    workbook = xlwt.Workbook() #注意Workbook的开头W要大写
##    sheet1 = workbook.add_sheet('Sheet1',cell_overwrite_ok=True)
##    style = xlwt.easyxf('align: wrap on')  #自动换行
##    alignment = xlwt.Alignment()
##    alignment.horz = xlwt.Alignment.HORZ_LEFT
##    alignment.vert = xlwt.Alignment.VERT_JUSTIFIED
##    style.alignment = alignment 
##    # add title
##    for column in range(len(apknamelist)):
##        col = sheet1.col(column)
##        col.width = 256*20
##        sheet1.write(0,column,apknamelist[column],style)
##        
##    # add value     
##    for row in  range (len(timelist)):
##       
##        for column in range(len(apknamelist)):
##           
##            if column == 0:
##                sheet1.write(row+1,column,timelist[row],style)
##            else:
##                sheet1.write(row+1,column,dicmemory[apknamelist[column]][row],style)
##                
##   
##          
##
##    #保存该excel文件,有同名文件时直接覆盖
##   
##    workbook.save('D:\\www\\memoryresult.xls')
##    time.sleep(5)
    #tuxiang
    
    xlsxwriterworkbook = xlsxwriter.Workbook('D:\\www\\memoryresult.xls')
    xlsxwriterworksheet1 = xlsxwriterworkbook.add_worksheet()
    style = xlsxwriterworkbook.add_format()
    style.set_text_wrap()
    for column in range(len(apknamelist)):
        xlsxwriterworksheet1.set_column(0,column,20)
        if 'com.roobo.boot' in apknamelist[column]:
          xlsxwriterworksheet1.write_url(0,column,"internal:'boot'!A1",style,apknamelist[column])
        elif 'com.roobo.coreserver' in apknamelist[column]:
          xlsxwriterworksheet1.write_url(0,column,"internal:'coreserver'!A1",style,apknamelist[column])
        elif 'com.juan.voiceservice' in apknamelist[column]:
          xlsxwriterworksheet1.write_url(0,column,"internal:'voiceservice'!A1",style,apknamelist[column])
        elif 'com.roobo.voice' in apknamelist[column]:
          xlsxwriterworksheet1.write_url(0,column,"internal:'voice'!A1",style,apknamelist[column])
        elif 'com.roobo.logmanager' in apknamelist[column]:
          xlsxwriterworksheet1.write_url(0,column,"internal:'logmanager'!A1",style,apknamelist[column])
        elif 'com.roobo.updater' in apknamelist[column]:
          xlsxwriterworksheet1.write_url(0,column,"internal:'updater'!A1",style,apknamelist[column])
        elif 'com.roobo.videoservice' in apknamelist[column]:
          xlsxwriterworksheet1.write_url(0,column,"internal:'videoservice'!A1",style,apknamelist[column])
          
        else:
          xlsxwriterworksheet1.write(0,column,apknamelist[column],style)
    # add value     
    for row in  range (len(timelist)):
        print row
        for column in range(len(apknamelist)):
            print apknamelist[column]
            print column
            if column == 0:
                xlsxwriterworksheet1.write(row+1,column,timelist[row],style)
            else:
                xlsxwriterworksheet1.write(row+1,column,dicmemory[apknamelist[column]][row],style)


    columncount = len(apknamelist)
    rowcount = len(timelist)+1
    flagcoreserver = 0
    flagvoiceservice = 0
    flagvoice = 0
    flagupdater = 0
    flaglogmanager = 0
    flagvideoservice = 0
    flagboot = 0
     #创建线性图
    for column in range(2,columncount+1):
##      print column
##      print apknamelist[column-1]
##      print changeNumToChar(toBigChar=(column))
      if 'com.roobo.coreserver' in apknamelist[column-1]:
        if flagcoreserver ==0 :
          xlsxwriterworksheet = xlsxwriterworkbook.add_worksheet('coreserver')
          lineChart1 = xlsxwriterworkbook.add_chart({'type':'line'})
        reschar = changeNumToChar(toBigChar=(column))
        lineChart1.add_series({                             
                            'name':'=Sheet1!$'+reschar+'$1',                                #每个线的名字   
                            'categories':'=Sheet1!$A$2:$A'+str(rowcount),               #X轴 值
                            'values':    '=Sheet1!$'+reschar+'$2:$'+reschar+'$'+str(rowcount),  })  #item的值
        
        lineChart1.set_title ({'name': 'Memory Result'})
        lineChart1.set_x_axis({'name': 'Time'})
        lineChart1.set_y_axis({'name': 'PSS(KB)'})            
        xlsxwriterworksheet.insert_chart('A1', lineChart1)
        flagcoreserver = 1
      elif 'com.juan.voiceservice' in apknamelist[column-1]:
        if flagvoiceservice ==0 :
          xlsxwriterworksheet = xlsxwriterworkbook.add_worksheet('voiceservice')
          lineChart2 = xlsxwriterworkbook.add_chart({'type':'line'})
        reschar = changeNumToChar(toBigChar=(column))
        lineChart2.add_series({                             
                            'name':'=Sheet1!$'+reschar+'$1',                                #每个线的名字   
                            'categories':'=Sheet1!$A$2:$A'+str(rowcount),               #X轴 值
                            'values':    '=Sheet1!$'+reschar+'$2:$'+reschar+'$'+str(rowcount),  })  #item的值
        
        lineChart2.set_title ({'name': 'Memory Result'})
        lineChart2.set_x_axis({'name': 'Time'})
        lineChart2.set_y_axis({'name': 'PSS(KB)'})           
        xlsxwriterworksheet.insert_chart('A1', lineChart2)
        flagvoiceservice = 1
      elif 'com.roobo.voice' in apknamelist[column-1]:
        if flagvoice == 0:
          xlsxwriterworksheet = xlsxwriterworkbook.add_worksheet('voice')
          lineChart3 = xlsxwriterworkbook.add_chart({'type':'line'})
        reschar = changeNumToChar(toBigChar=(column))
        lineChart3.add_series({                             
                            'name':'=Sheet1!$'+reschar+'$1',                                #每个线的名字   
                            'categories':'=Sheet1!$A$2:$A'+str(rowcount),               #X轴 值
                            'values':    '=Sheet1!$'+reschar+'$2:$'+reschar+'$'+str(rowcount),  })  #item的值
        
        lineChart3.set_title ({'name': 'Memory Result'})
        lineChart3.set_x_axis({'name': 'Time'})
        lineChart3.set_y_axis({'name': 'PSS(KB)'})          
        xlsxwriterworksheet.insert_chart('A1', lineChart3)
        flagvoice = 1
      elif 'com.roobo.updater' in apknamelist[column-1]:
        if flagupdater == 0:
          xlsxwriterworksheet = xlsxwriterworkbook.add_worksheet('updater')
          lineChart4 = xlsxwriterworkbook.add_chart({'type':'line'})
        reschar = changeNumToChar(toBigChar=(column))
        lineChart4.add_series({                             
                            'name':'=Sheet1!$'+reschar+'$1',                                #每个线的名字   
                            'categories':'=Sheet1!$A$2:$A'+str(rowcount),               #X轴 值
                            'values':    '=Sheet1!$'+reschar+'$2:$'+reschar+'$'+str(rowcount),  })  #item的值
        
        lineChart4.set_title ({'name': 'Memory Result'})
        lineChart4.set_x_axis({'name': 'Time'})
        lineChart4.set_y_axis({'name': 'PSS(KB)'})            
        xlsxwriterworksheet.insert_chart('A1', lineChart4)
        flagupdater = 1
      elif 'com.roobo.logmanager' in apknamelist[column-1]:
        if flaglogmanager == 0:
          xlsxwriterworksheet = xlsxwriterworkbook.add_worksheet('logmanager')
          lineChart5 = xlsxwriterworkbook.add_chart({'type':'line'})
        reschar = changeNumToChar(toBigChar=(column))
        lineChart5.add_series({                             
                            'name':'=Sheet1!$'+reschar+'$1',                                #每个线的名字   
                            'categories':'=Sheet1!$A$2:$A'+str(rowcount),               #X轴 值
                            'values':    '=Sheet1!$'+reschar+'$2:$'+reschar+'$'+str(rowcount),  })  #item的值
        
        lineChart5.set_title ({'name': 'Memory Result'})
        lineChart5.set_x_axis({'name': 'Time'})
        lineChart5.set_y_axis({'name': 'PSS(KB)'})           
        xlsxwriterworksheet.insert_chart('A1', lineChart5)
        flaglogmanager = 1
      elif 'com.roobo.videoservice' in apknamelist[column-1]:
##        print "&&&&"+apknamelist[column-1]
        if flagvideoservice == 0:
          xlsxwriterworksheet = xlsxwriterworkbook.add_worksheet('videoservice')
          lineChart6 = xlsxwriterworkbook.add_chart({'type':'line'})
        reschar = changeNumToChar(toBigChar=(column))
        lineChart6.add_series({                             
                            'name':'=Sheet1!$'+reschar+'$1',                                #每个线的名字   
                            'categories':'=Sheet1!$A$2:$A'+str(rowcount),               #X轴 值
                            'values':    '=Sheet1!$'+reschar+'$2:$'+reschar+'$'+str(rowcount),  })  #item的值
        
        lineChart6.set_title ({'name': 'Memory Result'})
        lineChart6.set_x_axis({'name': 'Time'})
        lineChart6.set_y_axis({'name': 'PSS(KB)'})           
        xlsxwriterworksheet.insert_chart('A1', lineChart6)
        flagvideoservice = 1
        
      elif 'com.roobo.boot' in apknamelist[column-1]:

        if flagboot == 0:
          xlsxwriterworksheet = xlsxwriterworkbook.add_worksheet('boot')
          lineChart7 = xlsxwriterworkbook.add_chart({'type':'line'})
        reschar = changeNumToChar(toBigChar=(column))
        lineChart7.add_series({                             
                          'name':'=Sheet1!$'+reschar+'$1',                                #每个线的名字   
                          'categories':'=Sheet1!$A$2:$A'+str(rowcount),               #X轴 值
                          'values':    '=Sheet1!$'+reschar+'$2:$'+reschar+'$'+str(rowcount),  })  #item的值

        lineChart7.set_title ({'name': 'Memory Result'})
        lineChart7.set_x_axis({'name': 'Time'})
        lineChart7.set_y_axis({'name': 'PSS(KB)'})           
        xlsxwriterworksheet.insert_chart('A1', lineChart7)
        flagboot = 1
      else:
        print "no defend"
          
      
          
                                    
                  
    xlsxwriterworkbook.close()
    time.sleep(5)  
    
memoryprocrank()        
        
     
            
            
    
    
    
