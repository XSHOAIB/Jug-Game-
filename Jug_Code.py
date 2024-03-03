def fill_jugA():
    A_jug=4
    print('jug A filled')
    return A_jug
def fill_jugB():
    B_jug=3
    print('jug B filled')
    return B_jug
    
def empty_jug(s):
    s=0
    print(f'jug {s} is empty')
    return s
def transfer_partialA(A_jug,B_jug):
    if B_jug==3:
        print("empty the jug B")
    count=B_jug
    while count <3:
        if A_jug == 0:
            break
        B_jug += 1
        A_jug -= 1
        count += 1
    print('transfered A to B')
    return A_jug, B_jug
    
def transfer_partialB(A_jug,B_jug):
    if A_jug==4:
        print("empty the jug A")
    count=A_jug
    while count < 4:
        if B_jug == 0:
            break
        A_jug += 1
        B_jug -= 1
        count += 1
    print('transfered B to A')
    return A_jug, B_jug
    
A_jug=0
B_jug=0

print('Question :\n        There are two jugs A B of 4 litre and 3 liter respectively. You can only either fill the whole jug or empty the whole jug with water or you can transfer the water from one jug to another. Now the task is to fill the jug B with 2 liter with the given conditions.  ')
while B_jug != 2:
    print('\n',A_jug,B_jug)
    print("\n\n 1. fill jug A \n 2. fill jug B \n 3. transfer  jug A to B \n 4. transfer jug B to A \n 5. empty jug A \n 6. empty jug B")
    prompt=int(input('enter number : '))
    if prompt == 1:
        A_jug=fill_jugA()
    elif prompt == 2:
        B_jug=fill_jugB()
    elif prompt == 3:
        A_jug, B_jug = transfer_partialA(A_jug,B_jug)
    elif prompt == 4:
        A_jug, B_jug = transfer_partialB(A_jug,B_jug)
    elif prompt == 5:
        A_jug=empty_jug(A_jug)
    elif prompt == 6:
        B_jug=empty_jug(B_jug)
    else:
        pass
print('\n\njug B is left with 2 liter of water, problem solved')
