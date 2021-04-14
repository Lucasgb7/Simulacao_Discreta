import time

def squares(ctr, key):
    y = x = ctr * key
    z = y + key
    x = x * x + y; x = (x >> 32) | (x << 32)
    x = x * x + z; x = (x >> 32) | (x << 32)
    x = x * x + y; x = (x >> 32) | (x << 32)

    return (x*x + z) >> 32

if __name__ == "__main__":
    key = 0xfb9e125878fa6cb3
    two32 = 4294967296
    n = 100000
    sum = 0
    print("Key: ", key)
    print("2^32: ", two32)

    start = time.time()
    for i in range(n):
        #print("\nValor: ", squares(i, key))
        sum += (squares(i, key) // two32)

    end = time.time()
    print("\nMedia: ", sum//n)
    print("\nTempo: ", end - start)