import pulp
prob = pulp.LpProblem("first_lp", pulp.LpMaximize)
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)
prob += 3*x + 2*y
prob += x + y <= 4
prob += x <= 3
prob.solve()

print("status:", pulp.LpStatus[prob.status])
print("x =", x.value())
print("y =", y.value())
print("objective =", pulp.value(prob.objective))