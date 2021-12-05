"""
사각형의 넓이는 알고 원의 넓이는 모를 때
사각형 안에 원을 그려놓고 많은 점을 투척한다.
이 때 원 안에 들어간 점의 비율에 사각형의 넓이를 곱하면 원의 넓이가 나온다.
"""

import random
import math

radius = 1
number = 1000000
answer = radius**2 * math.pi

in_circle = 0
for i in range(number):
    x = random.random() * radius * 2 - radius
    y = random.random() * radius * 2 - radius

    if x ** 2 + y ** 2 < radius ** 2:
        in_circle += 1
fraction = in_circle / number
estimated = fraction * 4 * radius **2
print(answer, estimated) 
