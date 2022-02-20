import os
import re 
import sys

unlock = "other internal script"






os.system('acidiag verifyapic > 6.txt')

file = open('/tmp/6.txt','r')
f = file.read()
SN = f.find('SN')
PID = f.find('PID')
realSN = ''
realPID =''
for x in range (3,14):
    ##print(f[SN+x])
    realSN = realSN + f[SN+x]



for x in range(4,18):
    realPID = realPID +f[PID+x]




verify ='openssl req -nodes -newkey rsa:2048 -keyout /tmp/{}.key -out /tmp/{}.csr -subj "/serialNumber=PID:{} SN:{}/CN={}"'.format(realSN,realSN,realPID,realSN,realSN)


os.system(verify)

csr = realSN +'.csr'


CsrFile = open(csr,'r')

csr_content = CsrFile.read()
print('########################## CSR file contents ################################')
print(csr_content)
print('#############################################################################')
SN_PID ='##########     SN:    {}      ######      PID:      {}     ##################'.format(realSN,realPID)
print(SN_PID)
print('###################### Paste the new certificate here then press (Ctrl + D) #######################')

oo = sys.stdin.readlines() 
new_crt=''.join(oo)

cer_file ='touch /tmp/{}.cer'.format(realSN)
os.system(cer_file)
dd = '/tmp/{}.cer'.format(realSN)
file_2=open(dd,'w')
file_2.write(new_crt)
file_2.close
os.system('\cp /securedata/ssl/server.crt /securedata/ssl/server.crt.backup')
os.system('\cp /securedata/ssl/server.key /securedata/ssl/server.key.backup')
mv_op='\mv /tmp/{}.key /securedata/ssl/server.key'.format(realSN)
os.system(mv_op)
os.system('echo > /securedata/ssl/server.crt')
file_4=open('/securedata/ssl/server.crt','w')
file_4.write(new_crt)
file_4.close



os.system('touch /tmp/unlock.sh')
file_3= open('/tmp/unlock.sh','w')
file_3.write(unlock)
file_3.close
os.system('chmod u+x /tmp/unlock.sh')
print('complete command to be run : /tmp/unlock.sh ')

   





