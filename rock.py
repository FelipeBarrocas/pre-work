from random import randint

def round(a,b):
    if a == b:
        return 0
    if a == 'r':
        if b == 'p':
            return -1
        if b == 's':
            return 1

    if a == 'p':
        if b == 's':
            return -1
        if b == 'r':
            return 1

    if a == 's':
        if b == 'r':
            return -1
        if b == 'p':
            return 1

def pc(a):
    if a == 1:
        return 's'
    if a == 2:
        return 'r'
    if a == 3:
        return 'p'

def win_condition(a):
    return a/2

print('quantos jogos deseja jogar')
jogos = int(input())

cpu_score = 0
player_score = 0
n = 1

while cpu_score < win_condition(jogos) and player_score < win_condition(jogos) and n < jogos + 1:
    print('coloque input')
    p = input()
    result = round(p, pc(randint(1,3)))
    if result == 1:
        player_score += 1
        print('you won')
        n +=1
    if result == -1:
        cpu_score += 1
        print('you lose')
        n +=1
    if result == 0:
        print ('draw')
        n +=1

if player_score > cpu_score:
    print('won match')

if player_score < cpu_score:
    print('lost match')

if player_score == cpu_score:
    print ('draw match')

