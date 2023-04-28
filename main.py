def fibonacci(termo):
    if termo < 0:
        raise ValueError("n tem que ser maior do que zero")
    elif termo == 0:
        #print(termo)
        return 0
    num = 1
    num_Prev = 0
    num2_Prev = 1
    for id in range(1,termo):
        if num==num_Prev:
            num += num2_Prev
        elif num > num_Prev:
            num2_Prev = num
            num += num_Prev
            num_Prev = num
    #print(num)
    return num

if __name__ == "__main__":
    n_termo = int(input('Digite o termo que deseja: '))
    fibonacci(n_termo)
