# Name - Akshala Bhatnagar
# Roll number - 2018012
# Section - A
# Group - 4

import matplotlib.pyplot as plt 
from matplotlib.patches import Ellipse
from matplotlib.patches import Polygon 
import math
from copy import deepcopy
import warnings
warnings.filterwarnings("ignore")


def multiply(A, B):
	"""
	Function for multiplying a matrix with a column matrix.
	Input: A is any matrix and B is a column matrix
	Returns: Resultant matrix
	"""
	if len(A) != len(B):
		return False
	else:
		result = [0 for x in range(len(B))]
		for i in range(len(A)):
			for j in range(len(A[0])):
				result[i] += A[i][j] * B[j]
	return result


class polygon(object):
	def __init__(self, X, Y):
		"""
		Initialises the objects of the class
		X: x coordinates of the vertices of the polygon
		Y: y coordinates of the vertices of the polygon
		"""
		self.X = X
		self.Y = Y
		self.prevPolygon = None
		self.points = []
		for i in range(len(X)):
			self.points.append([X[i], Y[i]])
		self.n = 1


	def drawPolygon(self):
		"""
		Draws the polygon 
		"""
		plt.ion()
		# plt.figure(self.n)
		plt.axes()
		if self.prevPolygon:
			self.prevPolygon.remove()
			plt.clf()
		polygon = Polygon(xy = self.points, closed = 'True')
		self.prevPolygon = polygon
		polygon.set_fill(False)
		plt.gca().add_patch(polygon)
		plt.axis('scaled')
		# plt.show(block = False)
		self.n += 1

	def scale(self, sx, sy):
		"""
		Scales the polygon about the origin
		Inputs: x and y axis scaling factors
		Changing values of the polygon vertices
		"""
		scaleMatrix = [[0 for x in range(2)] for y in range(2)] 
		scaleMatrix[0][0] = sx
		scaleMatrix[1][1] = sy
		result = []
		for element in self.points:
			result.append(multiply(scaleMatrix, element))
		self.points = result	
		self.X, self.Y = zip(*self.points)
		print(self.X, self.Y)

	def rotate(self, theta):
		"""
		Rotates the polygon about the origin
		Input: Angle of rotation in the clockwise direction
		Changing values of the polygon vertices
		"""
		theta = theta * math.pi / 180
		rotationMatrix = [[0 for x in range(2)] for y in range(2)] 
		rotationMatrix[0][0] = math.cos(-theta)
		rotationMatrix[0][1] = -math.sin(-theta)
		rotationMatrix[1][0] = math.sin(-theta)
		rotationMatrix[1][1] = math.cos(-theta)
		result = []
		for element in self.points:
			result.append(multiply(rotationMatrix, element))
		self.points = result
		self.X, self.Y = zip(*self.points)
		print(self.X, self.Y)

	def translate(self, dx, dy):
		"""
		Shifts the polygon
		Input: shift along x and y axis
		Changing values of the polygon vertices
		"""
		translationMatrix = [[0 for x in range(3)] for y in range(3)]
		translationMatrix[0][0] = 1
		translationMatrix[0][1] = 0
		translationMatrix[0][2] = dx
		translationMatrix[1][0] = 0
		translationMatrix[1][1] = 1
		translationMatrix[1][2] = dy
		translationMatrix[2][0] = 0
		translationMatrix[2][1] = 0
		translationMatrix[2][2] = 1
		result = []
		for element in self.points:
			element.append(1)
			product = multiply(translationMatrix, element)
			product = product[:2]
			result.append(product)
		self.points = result
		self.X, self.Y = zip(*self.points)
		print(self.X, self.Y)


class disc(object):
	def __init__(self, a, b, r1, r2):
		"""
		Initialises the objects of the class
		a: x coordinate of the centre
		b: y coordinate of the centre
		r1: first radius of ellipse
		r2: second radius of ellipse
		"""
		self.a = a
		self.b = b
		self.centre = [a, b]
		self.r1 = r1
		self.r2 = r2
		self.radii = [r1, r2]
		self.n = 1
		self.points = []
		self.prevPolygon = None
		X = []
		Y = []
		for i in range(-100, 101):
			x = r1*i/100
			X.append(x)
			y = (abs(r**2 - x**2) ** 0.5)
			Y.append(y)
		for i in range (100, -101, -1):
			x = r1*i/100
			X.append(x)
			y = -(abs(r**2 - x**2) ** 0.5)
			Y.append(y)
		for i in range(len(X)):
			self.points.append([X[i]+a, Y[i]+b])


	def drawDisc(self):
		"""
		Draws the disc
		"""
		plt.ion()
		# plt.figure(self.n)
		plt.axes()
		if self.prevPolygon:
			self.prevPolygon.remove()
			plt.clf()
		polygon = Polygon(xy = self.points, closed = 'True')
		self.prevPolygon = polygon
		polygon.set_fill(False)
		plt.gca().add_patch(polygon)
		plt.axis('scaled')
		plt.show(block = False)
		self.n += 1

	def scale(self, sx, sy):
		"""
		Scales the disc about the origin
		Inputs: x and y axis scaling factors
		Changing values of the centre coordinates and radii
		"""
		scaleMatrix = [[0 for x in range(2)] for y in range(2)] 
		scaleMatrix[0][0] = sx
		scaleMatrix[1][1] = sy
		self.centre = multiply(scaleMatrix, self.centre)
		self.a = self.centre[0]
		self.b = self.centre[1]
		self.radii = multiply(scaleMatrix, self.radii)
		self.r1 = self.radii[0]
		self.r2 = self.radii[1]
		result = []
		for element in self.points:
			result.append(multiply(scaleMatrix, element))
		self.points = result
		print(self.a, self.b, self.r1, self.r2)

	def rotate(self, theta):
		"""
		Rotates the disc about the origin
		Input: Angle of rotation in the clockwise direction
		Changing values of the centre coordinates and radii
		"""
		rotationMatrix = [[0 for x in range(2)] for y in range(2)] 
		rotationAngle = theta * math.pi / 180
		rotationMatrix[0][0] = math.cos(-rotationAngle)
		rotationMatrix[0][1] = -math.sin(-rotationAngle)
		rotationMatrix[1][0] = math.sin(-rotationAngle)
		rotationMatrix[1][1] = math.cos(-rotationAngle)
		self.centre = multiply(rotationMatrix, self.centre)
		self.a = self.centre[0]
		self.b = self.centre[1]
		result = []
		for element in self.points:
			result.append(multiply(rotationMatrix, element))
		self.points = result
		print(self.a, self.b, self.r1, self.r2)


	def translate(self, dx, dy):
		"""
		Shifts the polygon
		Input: shift along x and y axis
		Changing values of the centre coordinates and radii
		"""
		translationMatrix = [[0 for x in range(3)] for y in range(3)]
		translationMatrix[0][0] = 1
		translationMatrix[0][1] = 0
		translationMatrix[0][2] = dx
		translationMatrix[1][0] = 0
		translationMatrix[1][1] = 1
		translationMatrix[1][2] = dy
		translationMatrix[2][0] = 0
		translationMatrix[2][1] = 0
		translationMatrix[2][2] = 1
		element = self.centre
		element.append(1)
		product = multiply(translationMatrix, element)
		product = product[:2]
		self.centre = product
		self.a = self.centre[0]
		self.b = self.centre[1]
		result = []
		for element in self.points:
			element.append(1)
			product = multiply(translationMatrix, element)
			product = product[:2]
			result.append(product)
		self.points = result
		print(self.a, self.b, self.r1, self.r2)

figure = input()
plt.ion()

if figure == 'disc': # for disc
	disc_attributes = input() # a, b, r
	disc_attributes =  list(map(float, disc_attributes.split()))
	a = disc_attributes[0] # x coordinate of centre
	b = disc_attributes[1] # y coordinate of the centre
	r = disc_attributes[2] # radius of disc
	disc = disc(a, b, r, r)
	disc.drawDisc()
	transformation = input()

	while transformation != 'quit': # quit
		transformation = transformation.split()
		if transformation[0] == 'S': # scaling
			sx = float(transformation[1])
			sy = float(transformation[2])
			disc.scale(sx, sy)
			disc.drawDisc()

		if transformation[0] == 'R': # rotation
			theta = float(transformation[1])
			disc.rotate(theta)
			disc.drawDisc()

		if transformation[0] == 'T': # translation
			dx = float(transformation[1])
			dy = float(transformation[2])
			disc.translate(dx, dy)
			disc.drawDisc()

		transformation = input()
	

if figure == 'polygon': # for polygon
	list1 = input() # x coordinates
	list2 = input() # y coordinates
	X = list(map(float, list1.split())) # x coordinates
	Y = list(map(float, list2.split())) # y coordinates
	polygon = polygon(X, Y)
	polygon.drawPolygon()
	transformation = input()

	while transformation != 'quit': # quit
		transformation = transformation.split()
		if transformation[0] == 'S': # scaling
			sx = float(transformation[1])
			sy = float(transformation[2])
			polygon.scale(sx, sy)
			polygon.drawPolygon()

		if transformation[0] == 'R': # rotation
			theta = float(transformation[1])
			polygon.rotate(theta)
			polygon.drawPolygon()

		if transformation[0] == 'T': # translation
			dx = float(transformation[1])
			dy = float(transformation[2])
			polygon.translate(dx, dy)
			polygon.drawPolygon()
		transformation = input()
	


