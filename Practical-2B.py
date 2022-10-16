#Write a program to solve the tower of Hanoi problem

def tower_of_hanoi(disks,source,auxilary,target):
    if(disks == 1):
        print('Move disk 1 from rod {} to rod {}.'.format(source,target))
        return
#Function call itself 
    tower_of_hanoi(disks - 1,source,target,auxilary)
    print('Move disk {} from rod {} to rod {}.'.format(disks,source,target))
    tower_of_hanoi(disks - 1,auxilary,source,target)
    
disks = int(input('Enter the number of disks:'))
#We are referring source as A, auxilary as B, and target as C
tower_of_hanoi(disks,'A','B','C') #Calling the function