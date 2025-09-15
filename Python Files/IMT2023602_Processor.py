def list_string(L): #Converts integer list to string
    s = list(map(str,L))
    return ''.join(s)
def integer(n,ans=0,c=0): #converts binary string or list to integer
    if len(n)==0:
        return ans
    elif len(n)==1:
        return integer(n[:-1],ans-((2**c)*int(n[-1])),c+1)
    else:
        return integer(n[:-1],ans+((2**c)*int(n[-1])),c+1)
def binary(n,size): #converts integer to 2's complement binary (List)
    recurse = lambda n: [n] if n<=1 else recurse(n//2) + [n%2]
    L = recurse(abs(n))
    if n<0:
        for i in range(len(L)):
            if L[i]==1: L[i]=0
            else: L[i]=1
        a = recurse(integer(L)+1)
        L[-len(a):]=a
        ans = [1]*size
        ans[-len(L):]=L
        return ans
    else:
        ans = [0]*size
        ans[-len(L):]=L
        return ans
def isint(n):
    for i in range(len(n)):
        if (not n[i].isdecimal()) and (i!=0 or n[i]!='-'):
            return False
    return True
from IMT2023602_assembler import Main_memory as x
from IMT2023602_assembler import d as D
for i in range(len(x),1000):
    x.append(None)
OP_dict={}
for i in D.items(): OP_dict[i[1]]=i[0]
Main_memory = x
Main_memory[96] = [0]*39 + [1]
Main_memory[93] = [0]*39 + [1]
AC = [0]*40
MQ = [0]*40
IBR=[0]*20
MBR=[0]*40
PC=0
number_of_commands = 26
flag = True
def INPUT(a):
    global AC,MBR,PC,IBR,flag
    n = input("Enter a number : ")
    if not isint(n):
        print("you did not enter an integer")
        PC = number_of_commands-2
        IBR = [0]*20
        flag =  False
    elif int(n)<=0:
        PC = number_of_commands-2
        IBR = [0]*20
        flag =  False
        print("You entered an invalid integer")
    else:
        MBR = binary(int(n),40)
        AC = MBR[:]    
def NOP():
    #print("No operation")
    #print()
    return
def MAX(a):
    #print("MAX instruction is executed")
    global AC,MBR
    MBR = Main_memory[integer(a)][:]
    cmp1=integer(MBR)
    #print("MBR=",list_string(MBR),"Value=",cmp1)
    cmp2 = integer(AC)
    #print("AC=",list_string(AC),"Value=",cmp2)
    if cmp1>cmp2:
        #print("As MBR value is more, AC is replaced by MBR value")
        AC = MBR[:]
    #else:
        #print("AC value is more than MBR value, hence AC remains same")
    #print()
def MIN(a):
    #print("MIN instruction is executed")
    global AC,MBR
    MBR = Main_memory[integer(a)][:]
    cmp1 = integer(MBR)
    #print("MBR=",list_string(MBR),"Value=",cmp1)
    cmp2 = integer(AC)
    #print("AC=",list_string(AC),"Value=",cmp2)
    if cmp1 < cmp2:
        #print("As MBR value is less, AC is replaced by MBR value")
        AC = MBR[:]
    #else:
        #print("AC value is less than MBR value, hence AC remains same")
    #print()
def MULT(a):
    #print("MULT instruction is executed")
    global AC,MBR
    p1 = integer(AC)
    #print("AC=",list_string(AC),"Value=",p1)
    MBR = Main_memory[integer(a)][:]
    p2 = integer(MBR)
    #print("MBR=",list_string(MBR),"Value=",p2)
    ans = p2 * p1
    AC = binary(ans,40)
    #print("AC=",list_string(AC),"product is",integer(AC))
    #print()
def LTHAN0(a):
    #print("LTHAN0 instruction is executed")
    global AC,MBR
    MBR = Main_memory[integer(a)][:]
    v=integer(MBR)
    #print("MBR=",list_string(MBR),"Value=",v)
    if v<=0:
        AC = binary(1,40)
        #print("As MBR<=0, AC =",list_string(AC),"Which corresponds to 1")
    else:
        AC = binary(-1,40)
        #print("As MBR is not <=0, AC =",list_string(AC),"Which corresponds to -1")
    #print()
def EQ0(a):
    #print("EQ0 instruction is executed")
    global AC,MBR
    MBR = Main_memory[integer(a)][:]
    v=integer(MBR)
    #print("MBR=",list_string(MBR),"Value=",v)
    if v==0:
        AC = binary(1,40)
        #print("As MBR==0, AC =",list_string(AC),"Which corresponds to 1")
    else:
        AC = binary(-1,40)
        #print("As MBR is not=0, AC =",list_string(AC),"Which corresponds to -1")
    #print()
def LOAD_MQ(a):
    global MQ
    global AC
    AC = MQ[:]
def LOAD(a):
    #print("LOAD instruction is executed")
    global AC,MBR
    location = integer(a)
    #print("Memory location",location,"contains",list_string(Main_memory[location]))
    #print("This corresponds to the value",integer(Main_memory[location]))
    #print("This is sent to MBR, and is loaded in AC")
    MBR = Main_memory[integer(a)][:]
    AC = MBR[:]
    #print("AC=",list_string(AC),"Value=",integer(AC))
    #print()
def STOR(a):
    #print("STOR instruction is executed")
    global Main_memory,MBR
    location = integer(a)
    #print("AC=",list_string(AC),"Value=",integer(AC))
    #print("location to be stored in is", location )
    MBR = AC[:]
    Main_memory[location] = MBR[:]
    #print("AC is stored in The required memory location")
    #print()
def STOR_8_19(a):
    global Main_memory,MBR
    Main_memory[integer(a)][8:20] = AC[-12:]
def STOR_28_39(a):
    global Main_memory,MBR
    Main_memory[integer(a)][28:40] = AC[-12:]
def JUMP_0_19(a):
    #print("JUMP(0:19) instruction is executed")
    global PC,IBR
    location = integer(a)
    #print("Memory location to be jumped to is",location)
    PC = location-1
    #print("Hence, new PC value is",PC)
    IBR = [0]*20
    #print("As this is a left jump, IBR is erased")
    #print()
def JUMP_20_39(a):
    #print("JUMP(0:19) instruction is executed")
    global PC,IBR
    PC = integer(a)
    #print("New PC value is",PC)
    IBR = Main_memory[PC][20:40]
    #print("As this is right jump, IBR is loaded with the right instruction")
    #print("IBR=",list_string(IBR))
    #print()
def JUMPPOS_0_19(a):
    #print("JUMP+(0:19) instruction is executed")
    #print("AC=",list_string(AC),"Value=",integer(AC))
    if integer(AC)>=0:
        global PC,IBR
        location = integer(a)
        #print("Memory locattion to be jumped to is",location)
        PC = location-1
        #print("Hence, new PC value is",PC)
        IBR = [0]*8
        #print("As this is a left jump, IBR is erased")
    #else:
        #print("AC is less than 0, Hence no jump")
    #print()
def JUMPPOS_20_39(a):
    #print("JUMP+(20:39) instruction is executed")
    #print("AC=",list_string(AC),"Value=",integer(AC))
    if integer(AC)>=0:
        global PC,IBR
        PC = integer(a)
        #print("New PC value is",PC)
        IBR = Main_memory[PC][20:40]
        #print("As this is right jump, IBR is loaded with the right instruction")
        #print("IBR=",list_string(IBR))
    #else:
        #print("AC is less than 0, Hence no jump")
    #print()
def ADD(a):
    #print("ADD instruction is executed")
    global AC,MBR
    MBR = Main_memory[integer(a)][:]
    v1 = integer(MBR)
    v2 = integer(AC)
    #print("MBR =",list_string(MBR),"Value =",v1)
    #print("AC =",list_string(AC),"Value =",v2)
    ans = integer(MBR) + integer(AC)
    AC = binary(ans,40)
    #print("Result AC =",list_string(AC),"Value =",integer(AC))
    #print()
def SUB(a):
    global AC,MBR
    MBR = Main_memory[integer(a)][:]
    #print("initial AC",integer(AC))
    #print("to be subtracted by",integer(MBR))
    ans = binary(integer(AC) - integer(MBR))
    AC = binary(ans,40)
    #print("answer",integer(AC))
def MUL(a): #treats AC and MQ as a single 80 bit register
    global AC,MQ,MBR
    MBR = Main_memory[integer(a)][:]
    ans = integer(MBR) * integer(AC)
    ANS = binary(ans)
    if ans>0:
        if len(ANS)<=40:
            MQ = [0]*(40-len(ANS)) + ANS
            AC = [0]*40
        elif len(ANS)<=80:
            MQ = ANS[-40:]
            AC = [0]*(40-len(ANS[0:-40])) + ANS[0:-40]
    else:
        if len(ANS)<=40:
            MQ = [1]*(40-len(ANS)) + ANS
            AC = [1]*40
        elif len(ANS)<=80:
            MQ = ANS[-40:]
            AC = [1]*(40-len(ANS[0:-40])) + ANS[0:-40]
def DIV(a):
    #print("DIV instruction is executed")
    global AC,MQ,MBR
    MBR = Main_memory[integer(a)][:]
    ac = integer(AC)
    #print("AC =",list_string(AC),"Value =",ac)
    A = integer(MBR)
    #print("MBR =",list_string(MBR),"Value =",A)
    quotient = ac//A
    remainder = ac%A
    MQ = binary(quotient,40)
    AC = binary(remainder,40)
    #print("Operation AC/MBR is done")
    #print("Quotient MQ =",list_string(MQ),"Value =",integer(MQ))
    #print("Remainder AC =",list_string(AC),"Value =",integer(AC))
    #print()
d={}
d['00000000'] = NOP
d['00001010'] = LOAD_MQ
d['00000001'] = LOAD
d['00100001'] = STOR
d['00010010'] = STOR_8_19
d['00010011'] = STOR_28_39
d['00001101'] = JUMP_0_19
d['00001110'] = JUMP_20_39
d['00001111'] = JUMPPOS_0_19
d['00010000'] = JUMPPOS_20_39
d['00000101'] = ADD
d['00000110'] = SUB
d['00001011'] = MUL
d['00001100'] = DIV
d['00010110'] = MAX
d['00010111'] = MIN
d['00011000'] = LTHAN0
d['00011001'] = MULT
d['00011010'] = EQ0
d['00011011'] = INPUT
while PC <= number_of_commands:
    if sum(IBR)==0:
        #print("There is no next instruction in IBR, hence MAR is loaded")
        MAR = binary(PC,12)
        #print("MAR=",list_string(MAR),"PC value in MAR= ",PC)
        MBR = Main_memory[integer(MAR)][:]
        #print("MBR=",list_string(MBR))
        IBR = MBR[20:40]
        IR = MBR[0:8]
        MAR = MBR[8:20]
        #print("IBR=",list_string(IBR))
        #print("IR=",list_string(IR),"Which corresponds to", OP_dict[list_string(IR)])
        #print("MAR=",list_string(MAR),"Hence memory to be accessed is",integer(MAR))
        #print()
        d[list_string(IR)](MAR)
    if sum(IBR)!=0:
        #print("Next instruction is there in IBR, hence it is loaded")
        #print("IBR=",list_string(IBR))
        IR = IBR[0:8]
        MAR = IBR[8:20]
        IBR = [0]*20
        #print("IBR is emptied, IBR=",list_string(IBR))
        #print("IR=",list_string(IR),"Which corresponds to", OP_dict[list_string(IR)])
        #print("MAR=",list_string(MAR),"Hence memory to be accessed is",integer(MAR))
        #print()
        d[list_string(IR)](MAR)
    PC = PC + 1
    if sum(Main_memory[PC])==40:
        #print("Both instructions are STOP, Hence the processor stops running")
        break
if flag:
    print("HCF =",integer(Main_memory[100]))
    print("LCM =",integer(Main_memory[94]))

