#!/usr/bin/python
# Justin Limbach
# Imaginary Calculator 10/02/2017


# Test variables for working conditions. Uncomment if not needed
x = 8,8
y = 10,10

# Expects complex numbers in (real, phase) polar format. Returns the sum.

def complex_add (complex_a, complex_b) :
    real_answer = complex_a[0] + complex_b[0]
    imag_answer = complex_a[1] + complex_b[1]
    return real_answer, imag_answer

# Expects complex numbers in (real,phase) polar format. Returns the difference of B from A

def complex_subtract (complex_a, complex_b) :
    real_answer = complex_a[0] - complex_b[0]
    imag_answer = complex_a[1] - complex_b[1]
    return real_answer, imag_answer

# Expects complex numbers in (real,phase) polar format. Returns the quotient of B from A

def complex_division (complex_a, complex_b) :
    real_answer = complex_a[0] / complex_b[0]
    imag_answer = complex_a[1] - complex_b[1]
    return real_answer, imag_answer

#Expects complex numbers in (real,phase) polar format. Returns the product of A and B

def complex_multiplication (complex_a, complex_b) :
    real_answer = complex_a[0] * complex_b[0]
    imag_answer = complex_a[1] + complex_b[1]
    return real_answer, imag_answer

print 'Your Variables are : x = %d,%d y = %d,%d' % (x[0], x[1], y[1], y[1])
print ('Testing of Addition Commencing')
print complex_add(x,y)
print ('Testing of Subtraction Commencing')
print complex_subtract(x,y)
print ('Testing of Multiplication Commencing')
print complex_multiplication(x,y)
print ('Testing of Division Commencing')
print complex_division(x,y)





# JustinImaginaryCalculator
