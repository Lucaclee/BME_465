import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

def custom_latex_printer(exp,**options):
    from google.colab.output._publish import javascript
    url = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.1.1/latest.js?config=TeX-AMS_HTML"
    javascript(url=url)
    return sym.printing.latex(exp,**options)
sym.init_printing(use_latex="mathjax",latex_printer=custom_latex_printer)

# Problem 2:
ga = sym.symbols(r'gamma')
be = sym.symbols(r'beta')
Rz = sym.Function(r'R_z')(ga)
Ry = sym.Function(r'R_y')(be)
a = sym.cos(ga)
b = sym.sin(ga)
c = sym.cos(be)
d = sym.sin(be)
A1 = [[a, -b, 0],
      [b, a, 0],
      [0, 0, 1]]
B1 = [[c, 0, d],
      [0, 1, 0],
      [-d, 0, c]]
A = sym.Matrix(A1)
B = sym.Matrix(B1)
print('The solution for the Problem 2 matrix multiplication is:')
display(A*B)

# Problem 3:
al = sym.symbols(r'alpha')
Ra = sym.Function(r'R_x')(al)
e = sym.cos(al)
f = sym.sin(al)
C1 = [[1, 0, 0],
      [0, e, -f],
      [0, f, e]]
C = sym.Matrix(C1)
P3_Mat = A*B*C
P3_inv = P3_Mat.inv()
display(P3_inv)
