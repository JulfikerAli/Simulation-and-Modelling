# Pseudo random number generator
# Linear congruential method (LCM)

def LCM(x0,a,c,m,n):
    random_num = [0]*n
    r = [0]*n
    random_num[0] = x0
    for i in range(1,n):
        random_num[i] = (a*random_num[i-1] + c)%m
        r[i] = random_num[i]/m
    return random_num,r
def main():
    # require input 
    print("Enter the value of seed,multiplier,increment,modulus and Number of random value: ")
    x0,a,c,m,n = int(input()),int(input()),int(input()),int(input()),int(input())
    #generate pseudo random number  
    print(LCM(x0,a,c,m,n))
if __name__ == "__main__":  
    main()


