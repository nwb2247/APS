#1019, Book Page

import sys

def my_func(N) :

    dividend = N
    div_list = []
    mod_list = []

    while True :
        div, mod = divmod(dividend, 10)
        if div == 0 and mod == 0 :
            break
        div_list.append(div)
        mod_list.append(mod)
        dividend = div

    digit_count = [0 for _ in range(10)]

    for digit in range(10) :
        for i in range(len(mod_list)) :

            digit_count[digit] += div_list[i] * 10 ** i

            if mod_list[i] > digit : 
                digit_count[digit] += 10 ** i

            elif mod_list[i] == digit :
                digit_count[digit] += N % (10 ** i) + 1

            # 2315일 떄 1에 대해, 23*100 + (5 + 1) (2310 ~ 2316)

    for i in range(len(mod_list)) : # 0, 0100, 01314 등의 경우를 빼줌
        digit_count[0] -= 10 ** i

    sol = " ".join(map(str, digit_count))

    return sol

N = int(sys.stdin.readline())

print(my_func(N))