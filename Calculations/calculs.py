from CalculDistance import *
from CalculDirection import *

a = 46.821333
b = 6.500167
c = 46.81983333333333
d = 6.5

angle = cap_vrai(a,b,c,d)
longueur = distance_haversine(a,b,c,d)

print(longueur*1000)
print(angle)