import numpy
import statistics
s=[32,111,138,28,59,77,97]
x=numpy.std(s)
print(x)

a= [99,86,87,88,111,86,103,87,94,78,77,85,86]
q=numpy.mean(a)
print("Mean speed=" , q)

r=[17,34,56,78,70,23]
print(numpy.std(r))

s=[12,13,14,16,15,20]
print(numpy.std(s))

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print("Median speed =" , x)

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = statistics.mode(speed)
print("Mode speed= ", x)





