def hang(n):
    l1=["_____","|    |","|    ","|    ","|    ","|","|___"]
    l2=["_____","|    |","|    0","|    ","|    ","|","|___"]
    l3=["_____","|    |","|    0","|    | ","|    ","|","|___"]
    l4=["_____","|    |","|    0","|   /| ","|    ","|","|___"]
    l5=["_____","|    |","|    0","|   /|\ ","|    ","|","|___"]
    l6=["_____","|    |","|    0","|   /|\ ","|   /  ","|","|___"]
    l7=["_____","|    |","|    0","|   /|\ ","|   / \ ","|","|___"]
    l=[l1,l2,l3,l4,l5,l6,l7]
    for i in l:
        if i==l[n-1]:
            for j in i:
                print(j)
cat=input("enter category")
print("Enter %s to be guessed:"%(cat))
word=input()
word=word.upper()
print("\n"*50)
k=[]
for x in word:
    if x==" ":
        k.append('/')
    else:
        k.append(x)
#print(k)
p=[]
cnt=0
for i in range(len(k)):
    if k[i]=='/':
        p+='/'
        cnt+=1
    else:
        p+='_'
print(p)
for q in p:
    print(q,end=" ")
print("\n")
t=1
fl=0
mn=0
#cp=0
e=[]
for d in range(65,91):
    e.append(chr(d))
while t<=7 and fl<(len(p)-cnt):
    print(e)
    mn=0
    cp=0
    ot=input("Guess a letter: ")
    ot=ot.upper()
    if ot not in e:
        print("letter already guessed or invalid choice")
        continue
    else:
        for y in range(len(k)):
            if ot[0]==k[y]:
                p[y]=ot[0]
                for q in p:
                    print(q,end=" ")
                print("\n")
                fl+=1
                cp=1
        if cp==0:
            mn+=1
        
    if mn==1:
        hang(t)
        t+=1
    for b in range(len(e)+1):
        if e[b]==ot:
            del e[b]
            break
if t>7:
    print("u dead\nur %s is"%(cat),word)
else:
    print("u win") 

