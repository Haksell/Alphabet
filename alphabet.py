import math
import os
from statistics import mean
import sys
from time import time


def truncated_mean(results, *, size, skip):
    if size > len(results):
        return math.inf
    counting = sorted(results[-size:])[skip:-skip]
    return mean(counting)


phrase = "abcdefghijklmnopqrstuvwxyz" if len(sys.argv) == 1 else " ".join(sys.argv[1:])
results = []
best_single = best_avg5 = best_avg25 = math.inf

while True:
    t0 = time()
    attempt = input().strip()
    if attempt == phrase:
        print("SUCCESS")
        os.system("play -q success.mp3&")  # -q means no output and & means async, I think
        single = time() - t0
    else:
        print("FAILURE")
        os.system("play -q failure.mp3&")
        single = math.inf
    results.append(single)
    # Stats
    avg5 = truncated_mean(results, size=5, skip=1)
    avg25 = truncated_mean(results, size=25, skip=2)
    best_single = min(single, best_single)
    best_avg5 = min(avg5, best_avg5)
    best_avg25 = min(avg25, best_avg25)
    # Output
    print(f"Single: {single:5.2f} - Best single: {best_single:.2f}")
    print(f"Avg5:   {avg5:5.2f} - Best avg5:   {best_avg5:.2f}")
    print(f"Avg25:  {avg25:5.2f} - Best avg25:  {best_avg25:.2f}")
    print()
