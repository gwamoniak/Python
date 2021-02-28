
import sys

Height = 48
Width  = 128

def is_too_far(cell):
	dist_sqrt = cell.real*cell.real + cell.imag * cell.imag
	return dist_sqrt > 4
	
def iterations(x,y):
	c = complex(x,y)
	z = 0
	for i in range(0,250):
		if is_too_far(z):
			return i
		z = z*z + c
	return 256

def plot():
	start_posX = -3.0
	end_posX   = 1.0
	start_posY = -1.0
	end_posY   = 1.0
	for y in range(0,Height):
		posY = start_posY +(end_posY-start_posY) *(y/float(Height))
		for x in range(0,Width):
			posX = start_posX +(end_posX-start_posX) *(x/float(Width))
			stability = iterations(posX,posY)
			if stability > 256:
				sys.stdout.write("#")
			elif stability > 200:
				sys.stdout.write("*")
			elif stability > 100:
				sys.stdout.write(".")
			else:
				sys.stdout.write(" ")
		sys.stdout.write("\n")
		

if __name__ == "__main__":
	plot()
			
