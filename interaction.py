import pygame


def click(size):
    
    x = -1
    y = -1

    if pygame.mouse.get_pressed(3)[0] == True:
        pos = pygame.mouse.get_pos()
        i=1
        j=1
        
        while i <= 9:

            if pos[0] <= (size[0]*i)/9 and pos[0] >= (size[0]*(i-1))/9:
                x = i
                break
            else:
                i+=1
            
        while j <= 9:
            
            if pos[1] <= (size[1]*j)/9 and pos[1] >= (size[1]*(j-1))/9:
                y=j
                break
            else:
                j+=1

    if x != -1 and y != -1:
        x-=1
        y-=1
        return x,y
    else:
        return False   