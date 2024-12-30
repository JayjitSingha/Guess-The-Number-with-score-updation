import random
def game():
    l=[]
    for i in range(1,101):
        l.append(i)
    comp=random.choice(l)
    sum=0
    while True:
        you=int(input(f'guess the number : '))
        sum+=1
        if(comp==you):
            print(f'congrats you guessed the number in {sum} tries')
            break
        elif(comp>you):
            print('The number you guessed is lesser than the number computer has thought')
        else:
            print('The number you guessed is greater than the number computer has thought')
    return sum
def num(a):
    indx=a.find('->')
    rindx=a.find('    ')
    return int(a[indx+3:rindx])
def name(b):
    indx=b.find('    ')
    return b[indx+4:].strip()
playerName=input('Enter your name : ')
score = 100000-5000*game()
scrmin=20000
with open('score.txt','r') as f:
    l=f.readlines()
    with open('score.txt','w') as t:
        if score >= scrmin:
            sum=1
            if len(l)==0:
                t.write(f'1 -> {score}    {playerName}')
            for i in range(len(l)):
                sum2=0
                if i+1==len(l) and sum==2:
                    t.write(f'\n{i+sum} -> {num(l[i])}    {name(l[i])}')
                elif score>=int(num(l[i])) and sum==1:                 
                    if i==0: 
                        t.write(f'{i+sum} -> {score}    {playerName}')
                        sum+=1
                        t.write(f'\n{i+sum} -> {num(l[i])}    {name(l[i])}')
                    else:
                        t.write(f'\n{i+sum} -> {score}    {playerName}')
                        sum+=1
                        t.write(f'\n{i+sum} -> {num(l[i])}    {name(l[i])}')        
                elif i+1==len(l):
                    if(i==0):
                        t.write(l[i])
                    else:
                        t.write('\n'+l[i])
                    sum+=1
                    t.write(f'\n{i+sum} -> {score}    {playerName}')
                else:
                    if i==0:
                        t.write(f'{i+sum} -> {num(l[i])}    {name(l[i])}')
                    else:
                        t.write(f'\n{i+sum} -> {num(l[i])}    {name(l[i])}')
with open('score.txt') as f1:
    print('Leaderboard\n'+f1.read())
