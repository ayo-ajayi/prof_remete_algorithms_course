# Ayomide
def sqr_mod(x, y, mod_div):
    res = 1
    x = x % mod_div
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % mod_div
        x = (x * x) % mod_div
        y //= 2
    return res


def miller_rabin(a, p):
    d = p-1
    s = 0
    while (d % 2 == 0):
        d /= 2
        s += 1
    print("s: ", s, ", d: ", d)
    b = [sqr_mod(a, (2**i)*d, p) for i in range(0, s+1)]
    return b


print(miller_rabin(3, 915479))
# determine if it is pseudo-prime with list
# def decision():
