import math

def trialDiv(num):
    answer = []
    if num <= 1:
        print("Число меньше 1")
        return answer
    ds = math.ceil(math.sqrt(num))
    lst = get_nearest_prime(ds)
    k = 0
    p_lst = []
    while k != len(lst):
        if num == 1:
            break
        q = num // lst[k]
        r = num % lst[k]
        if r == 0:
            p_lst.append(lst[k])
            num = q
            continue
        if q >lst[k]:
            k += 1
        else:
            p_lst.append(num)
            break
    str_answer = ""
    str_answer+=str(p_lst[0])
    for i in range(1,len(p_lst)):
        str_answer+=("*"+str(p_lst[i]))
    return str_answer


def get_nearest_prime(n):
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)

    while True:
        n+=1
        if n % 2 == 0:
            continue
        flag = False
        for i in range(3, math.ceil(n ** 0.5) + 1, 2):

            if n % i == 0:

                flag = True
                break
        if flag == True:
            continue
        lst.append(n)
        break
    lst.remove(2)
    return lst

print(trialDiv(973))