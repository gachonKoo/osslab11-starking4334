import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import geo.utils as utils

a, b = 3, 4
c = utils.hypotenuse(a, b)
print('c =', c)

r = 10
area = utils.circle_area(r)
print('area =', area)
