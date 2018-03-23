#https://github.com/thiagohomem/RoboFEI-HT_Debug/blob/master/AI/Vision/src/DNN.py

import random
import time


class campo:
	x = 9
	y = 6


class robo:
	peso = 4.5
	altura = 0.45
	v = 0.6042
	x = 1
	y = 1


print("%.3f" % robo.x)

print("Eu estou em X = %.3f" % robo.x)
print("Eu estou em Y = %.3f" % robo.y)
xi = 1.000
for i in range(15):
	xi += 0.010
	print("X da bola: %.3f" % xi)
a = 0.02
count = 0
for i in range(1000):
	#time.sleep(0.02)
	count += a
	#print("%.2f" % count)
