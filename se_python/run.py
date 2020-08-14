import os
import sys
f = open('a.log', 'a')
sys.stdout = f
sys.stderr = f

def fun():
    for i in range(20):
        os.system("python StatisticCount.py")
fun()
