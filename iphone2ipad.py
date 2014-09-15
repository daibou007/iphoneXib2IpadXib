#coding:UTF-8
# -*- coding:utf-8 -*-
 
import re
import sys
import os
reload(sys) 
sys.setdefaultencoding('utf8') 
 
#修改尺寸320 480
def traslateFrame(filestr):
    filestr2=filestr.replace("320","768")
    filestr2=filestr2.replace("480","1024")
    return filestr2

#修改 iOS.CocoaTouch.iPad
def traslateTouch(filestr):
    filestr2 = filestr.replace("iOS.CocoaTouch","iOS.CocoaTouch.iPad")
    return filestr2

#修改 .xib
def traslateXib(filestr):
    filestr2 = filestr.replace("com.apple.InterfaceBuilder3.CocoaTouch.XIB","com.apple.InterfaceBuilder3.CocoaTouch.iPad.XIB")
    return filestr2

#修改 IBCocoaTouchFramework
def  traslateFramework(filestr):
    filestr2 = filestr.replace("IBCocoaTouchFramework","IBIPadFramework")
    return filestr2

#修改@2x.png
def translateImage2(filestr):
    filestr2=filestr.replace(".png","@2x.png")
    return filestr2
 
#修改png尺寸
def translateImage1(filestr):
    filestr2=filestr;
    reobj = re.compile(r'<string key="(\w+).png">{(\d+),\s+(\d+)}</string>')
    for match in reobj.finditer(filestr):  
        newSize1=int(match.group(2))*2
        newSize2=int(match.group(3))*2
        newstr='<string key="'+match.group(1)+'.png">{'+str(newSize1)+", "+str(newSize2)+"}</string>"
        print(match.group(0))
        print(newstr)
        filestr2,number=re.subn(match.group(0),newstr, filestr2)
    return filestr2
 
#修改字体大小
def translateNSSize(filestr):
    filestr2=filestr;
    reobj = re.compile(r'<double key="NSSize">(\d+)</double>')
    for match in reobj.finditer(filestr):  
        newSize=int(match.group(1))*2
        newstr='<double key="NSSize">'+str(newSize)+'</double>'
        print(match.group(0))
        print(newstr)
        filestr2,number=re.subn(match.group(0),newstr, filestr2)
    return filestr2
 
#修改字体大小
def translatePointSize(filestr):
    filestr2=filestr;
    reobj = re.compile(r'<double key="pointSize">(\d+)</double>')
    for match in reobj.finditer(filestr):  
        newSize=int(match.group(1))*2
        newstr='<double key="pointSize">'+str(newSize)+'</double>'
        print(match.group(0))
        print(newstr)
        filestr2,number=re.subn(match.group(0),newstr, filestr2)
    return filestr2
 
 
#转换<string key="NSFrameSize">{393, 136}</string>
def translateFrameSize(filestr):
    filestr2=filestr;    
    reobj = re.compile(r'key="NSFrameSize">{(\d+),\s+(\d+)}<')
    for match in reobj.finditer(filestr):  
        print(match.group(0))
        newSize1=int(match.group(1))*2
        newSize2=int(match.group(2))*2
        newstr='key="NSFrameSize">{'+str(newSize1)+', '+str(newSize2)+'}<'
        print(match.group(0))
        print(newstr)
        filestr2,number=re.subn(match.group(0),newstr, filestr2)
    return filestr2
 
 
#修改位置大小
def translateXYSize(filestr):
    filestr2=filestr;
    reobj = re.compile(r"{(\d+),\s?(\d+)},\s?{(\d+),\s?(\d+)}")
    for match in reobj.finditer(filestr):
        newstr="{"+str(int(match.group(1))*2)+", "+str(int(match.group(2))*2)+"},{"+str(int(match.group(3))*2)+", "+str(int(match.group(4))*2)+"}"
        filestr2, number = re.subn(match.group(0),newstr, filestr2)
    return filestr2        
 
 
def translateFile(filename):
    f=open(filename,"r")
    filestr=f.read()
    filestr2=traslateXib(filestr)
    filestr2=traslateFrame(filestr2)
    filestr2=traslateTouch(filestr2)
    filestr2=traslateFramework(filestr2)
    filestr2=translateXYSize(filestr2)
    filestr2=translateFrameSize(filestr2)
    filestr2=translateNSSize(filestr2)
    filestr2=translatePointSize(filestr2)
    filestr2=translateImage1(filestr2)
    filestr2=translateImage2(filestr2)
    f.close()
    filename=filename.replace(".xib","_iPad.xib")
    f=open(filename,"w")
    f.write(filestr2)
    f.close()
     
def translateAll():
    sStr2 = '.xib'
    sStr3 = '_iPad.xib'    
    for files in os.walk(os.getcwd()):
        for name in files:
            for name1 in name:
                if name1.find(sStr2)>-1:
                    if name1.find(sStr3)==-1:
                        translateFile(name1)
 
 
if __name__=="__main__":
    translateAll()