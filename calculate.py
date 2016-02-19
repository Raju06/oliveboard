from sympy import solve_poly_system
from sympy.abc import x,y

print solve_poly_system([x+y-81,1.2*x-1.5*y],x,y)
