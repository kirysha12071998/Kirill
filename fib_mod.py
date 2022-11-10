def fib_mod(n, m):
    P = list()
    P.append(0)
    P.append(1)
    period = 0
    i = 2
    if i >= n + 1:
        return P[n]
    else:
        while i < n + 1:
            P.append((P[i - 1] + P[i - 2]) % m)
            if P[i - 1] == 0 and P[i] == 1:
                period = i - 1
                break
            i += 1
        if period == 0:
            return P[n]
        else:
            return P[n % period]
    


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


    main()
