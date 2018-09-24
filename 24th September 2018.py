# 24th September 2018 Daily Coding Problem #10
#
# This problem was asked by Apple.
#
# Implement a job scheduler which takes in a function f and an integer n,
# and calls f after n milliseconds.

import time

def job_scheduler(f, n):
    time.sleep(float(n)/1000.0)
    return f()

def test_function():
    return "Test function."

n = int(input('Enter the delay amount in milliseconds : '))

print(time.ctime())
print(job_scheduler(test_function, n), '\n' + time.ctime())