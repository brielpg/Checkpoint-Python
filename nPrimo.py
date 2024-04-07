def numero_primo(N):
    for num in range(N, 1, -1):
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            return num
