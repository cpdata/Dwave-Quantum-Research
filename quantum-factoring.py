import dwavebinarycsp as dbc
# Add an AND gate as a constraint to CSP and_csp defined for binary variables 
and_gate = dbc.factories.and_gate(["x1", "x2", "x3"])
and_csp = dbc.ConstraintSatisfactionProblem('BINARY')
and_csp.add_constraint(and_gate)

# Test that for input x1,x2=1,1 the output is x3=1 (both switches on and light shining)
and_csp.check({"x1": 1, "x2": 1, "x3": 1})

# Convert the CSP into BQM and_bqm
and_bqm = dbc.stitch(and_csp)
and_bqm.remove_offset()
# Print the linear and quadratic coefficients. These are the programable inputs to a D-Wave system
print(and_bqm.linear)
print(and_bqm.quadratic)

# Use a dimod test sampler that gives the BQM value for all values of its variables
from dimod import ExactSolver
sampler = ExactSolver()

# Solve the BQM
solution = sampler.sample(and_bqm)
list(solution.data())

# Set an integer to factor
P = 21

# A binary representation of P ("{:06b}" formats for 6-bit binary)
bP = "{:06b}".format(P)
print(bP)

csp = dbc.factories.multiplication_circuit(3)
# Print one of the CSP's constraints, the gates that constitute 3-bit binary multiplication
print(next(iter(csp.constraints)))
