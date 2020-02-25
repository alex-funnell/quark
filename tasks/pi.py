import multiprocessing
import time
import sys
from tqdm import tqdm

def calcPi():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            nr = 10 * (r - n * t)
            n  = ((10 * (3 * q + r)) // t) - 10 * n
            q  *= 10
            r  = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q  *= k
            t  *= l
            l  += 2
            k += 1
            n  = nn
            r  = nr

i = 0
pi_digits = calcPi()
startTime = time.time()
duration = 120
endTime = startTime + duration
validTime = True



for digit in pi_digits:
    sys.stdout.write(str(digit))
    i += 1
    currentTime = time.time()
    if currentTime == endTime or currentTime > endTime and validTime:
        print('Digits found:',str(i))
        timeTaken = currentTime-startTime
        print('Took',timeTaken,'seconds.')
        validTime = False
        exit()
