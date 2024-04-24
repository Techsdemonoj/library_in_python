# Optimizers is scipy : They are set of procedure defined in scipy that either find
# the minimum value odf a function or a root of an equation.

# Optimizing function: all the algorithms which helps in minimizing the data.

# Root on an equation: x+cos(x) , we will solve it via optimize.root function.
# This fuction takes 2 arguments: "fun" and x0



# Example:- Here we will find the root of the equation : x + cos(x)
from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)                 # output : [-0.73908513]

# Here we want the info about not just  x but the whole root

print("myroot = ", myroot) 

# output : 
# myroot =   message: The solution converged.
# success: True
#  status: 1
#     fun: [ 0.000e+00]
#       x: [-7.391e-01]
# method: hybr
#    nfev: 9
#    fjac: [[-1.000e+00]]
#       r: [-1.674e+00]
#    qtf: [-2.668e-13]


# Minimizing thre fuction or data:
# High point are called maxima and low point is called mimina
# Finding the minima: 
# we use scipy.optimize.minimize(). it uses 3 arguments: "fun",x and method: it also some leagal value:- "CG", "BFGS", "NEWTON-CG", "l-BFGS-B", "TNC", "COBYLA", "SLSQP".

# Callback :- function called after each iteration of optimixations.


# Example of the above: in which we will minimize the function: x^ + x + 2 with BFGS
from scipy.optimize import minimize
def eqn(x):
    return x**2 + x + 2
mymin = minimize(eqn,0,method="BFGS")
print(mymin)











 