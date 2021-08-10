def main():
    #escribe tu código abajo de esta línea
    for i in range(3):
        n=int(input("Dame un numero="))

        if n < 0:
            print(str(n)+"!=Error!")
        else:
            p=1
            f=1
            while p <= n:
                f = f * p
                p=p+1
            print(str(n)+"!="+str(f))

if __name__=='__main__':
    main()
