import time 

def squares(ctr, key):
    y = x = ctr * key
    z = y + key
    x = x * x + y; x = (x >> 32) | (x << 32)
    x = x * x + z; x = (x >> 32) | (x << 32)
    x = x * x + y; x = (x >> 32) | (x << 32)

    return (x*x + z) >> 32

if __name__ == "__main__":
    key = 0x548c9decbce65297
    two32 = 4294967296
    n = 1000000000
    sum = 0
    print("Key: ", key)
    print("two32: ", two32)

    start = time.time()
    for i in range(n):
        sum += (squares(i, key) // two32)

    end = time.time()
    print("\nMedia: ", sum/n)
    print("\nTempo: ", end - start)