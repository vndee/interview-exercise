import random


def estimate(n):
    inner_circle = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 < 1:
            inner_circle += 1
    
    return 4 * inner_circle / n
    

if __name__ == '__main__':
    print(estimate(1000000))
