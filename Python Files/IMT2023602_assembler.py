F=open("IMT2023602_Assembly_Code.txt","r")
L=[]
for i in F.readlines():
    L.append(i.split())
F.close()
binary = lambda n: n%2 if n==1 else binary(n//2)*10 + n%2
integer = lambda n,ans=0,c=0: ans if len(n)==0 else integer(n[:-1],ans+((2**c)*int(n[-1])),c+1) 
d={}
d['NOP'] = '00000000'
d['LOAD_MQ'] = '00001010'
d['LOAD'] = '00000001'
d['STOR'] = '00100001'
d['STOR(0:19)'] = '00010010'
d['STOR(20:39)'] = '00010011'
d['JUMP(0:19)'] = '00001101'
d['JUMP(20:39)'] = '00001110'
d['JUMP+(0:19)'] = '00001111'
d['JUMP+(20:39)'] = '00010000'
d['ADD'] = '00000101'
d['SUB'] = '00000110'
d['MUL'] = '00001011'
d['DIV'] = '00001100'
d['MAX'] = '00010110'
d['MIN'] = '00010111'
d['LTHAN0'] = '00011000'
d['MULT'] = '00011001'
d['EQ0'] = '00011010'
d['INPUT'] = '00011011'
d['STOP'] = '11111111'
Main_memory=[]
for i in L:
    s=''
    for j in i:
        #print(j)
        if j.isdecimal():
            a = str(binary(int(j)))
            a = '000000000000' + a
            s = s + a[-12:]
        elif j=='STOP':
            s = s + d[j] + '111111111111'
        elif j=='NOP' or j=='INPUT':
            s = s + d[j] + '000000000000'
        else: s = s + d[j]
    Main_memory.append(list(map(int,s)))

