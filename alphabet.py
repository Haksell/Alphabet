import math
import os
from statistics import mean
import sys
from time import time


def truncated_mean(results, *, size, skip):
    assert skip * 2 < size
    if size > len(results):
        return math.inf
    counting = sorted(results[-size:])[skip:-skip]
    return mean(counting)


phrase = "abcdefghijklmnopqrstuvwxyz" if len(sys.argv) == 1 else " ".join(sys.argv[1:])
lines = 1 + phrase.count("\\n")
results = []
best_single = best_avg5 = best_avg25 = math.inf

while True:
    # Multiline input
    t0 = time()  # Super imprecise and takes into account code execution time
    attempt = []
    for i in range(lines):
        attempt.append(input())
    attempt = "\\n".join(attempt)
    # Yay or nay?
    if attempt == phrase:
        print("SUCCESS")
        os.system("play -q -V0 success.wav&")  # -q means no output, -V0 suppresses warnings and & means async, I think
        single = time() - t0
    else:
        print("FAILURE")
        os.system("play -q -V0 failure.wav&")
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
