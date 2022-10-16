#Solve constraint satisfaction problem

import constraint
problem = constraint.Problem()
problem.addVariable('x', [1,2,3])
problem.addVariable('y', range(10))
def our_constraint(x,y):
    if x+y>=5:
        return True
problem.addConstriant(our_constraint, ['x','y'])
solutions = problem.getSolutions()
length = len(solutions)
print("(x,y) ∈ {", end = "")
for index, solution in enumerate(solutions):
    if index == length - 1:
        print("({},{})".format(solution['x'], solution['y']), end = "")
    else:
        print("({},{})".format(solution['x'], solution['y']), end = "")
print("}")