import math
import time
import os
import sys

A = 0
B = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    output = [' '] * 1760
    zbuffer = [0] * 1760
    clear()
    for j in range(0, 628, 7):     # Ring angle
        for i in range(0, 628, 2): # Circle angle
            c = math.sin(i / 100)
            d = math.cos(j / 100)
            e = math.sin(A)
            f = math.sin(j / 100)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i / 100)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 0 <= o < 1760 and D > zbuffer[o]:
                zbuffer[o] = D
                output[o] = ".,-~:;=!*#$@"[max(0, N)]

    sys.stdout.write("\x1b[92m")  # Set green
    for i in range(0, 1760, 80):
        print(''.join(output[i:i+80]))
    sys.stdout.write("\x1b[0m")   # Reset color

    A += 0.04
    B += 0.02
    time.sleep(0.03)
