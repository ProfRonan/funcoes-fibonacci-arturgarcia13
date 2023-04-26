n_termo = int(input('Digite o termo que deseja: '))
if n_termo < 0:
    raise ValueError("n tem que ser maior do que zero")
    
def fibonacci(termo):
    num = 0
    num_Prev = 0
    num2_Prev = 1
    for id in range(0,termo):
        if num==num_Prev:
            num += num2_Prev
        elif num > num_Prev:
            num2_Prev = num
            num += num_Prev
            num_Prev = num
    return print(num_Prev)

fibonacci(n_termo)
