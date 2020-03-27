
def main():
    a=input()
    global l,k,m,n,j
    if a=='i':
        l+=1
        k+=1
        if(k==2):
            print("you have used I 2 times you have losed ")
            exit()
        if(l==4):
            print("you wins")
            exit()
        print("you are right but if you use it more than once you will lose ")
        return main()
    if a=='s':
        l+=1
        m+=1
        if(m==2):
            print("you have used S 2 times you have losed")
            exit()
        if(l==4):
            print("you wins")
            exit()
        print("you are right but if you use more than one time you lose")
        return main()
    if a=='h':
        l+=1
        n+=1
        if(n==2):
            print("you have used H 2 times you have losed")
            exit()
        if(l==4):
            print("you wins")
            exit()
        print("you are right but if use than one time you will lose it")
        return main()
    if a=='u':
        l+=1
        j+=1
        if(j==2):
            print("you have used U two times you have lose the game ")
            exit()
        if(l==4):
            print("you wins")
            exit()
        print("you are right but if use than one time you will lose it")
        return main()
    else:
        print("you are wrong")
        global t
        t-=1
        if(t==5):
            print("you have 5 more chances left")
            return main()
        if(t==4):
            print("you have 4 more chances left")
            return main()
        if(t==3):
            print("you have 3 more chances left")
            return main()
        if(t==2):
            print("you have 2 more chances left to guess ")
            return main()
        if(t==1):
            print("you have 1 more chance left")
            return main()
        if(t==0):
            print("you lose")
            exit()
l=0
t=6
k=0
m=0
n=0
j=0
main()

    


