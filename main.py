import pulp as p

problem = p.LpProblem("Bag Problem", p.LpMaximize)

x1 = p.LpVariable("Object 1", cat="Binary")
x2 = p.LpVariable("Object 2", cat="Binary")
x3 = p.LpVariable("Object 3", cat="Binary")
x4 = p.LpVariable("Object 4", cat="Binary")
x5 = p.LpVariable("Object 5", cat="Binary")
x6 = p.LpVariable("Object 6", cat="Binary")
x7 = p.LpVariable("Object 7", cat="Binary")

# Objective function
problem += 7000 * x1 + 6500 * x2 + 8250 * x3 + 7125 * x4 + 3500 * x5 + 2400 * x6 + 3100 * x7

# Constraints
problem += 8 * x1 + 10 * x2 + 4 * x3 + 9 * x4 + 3 * x5 + 2 * x6 + 4 * x7 <= 15

status = problem.solve()
print(p.LpStatus[status])

print(x1, ": ", p.value(x1))
print(x2, ": ", p.value(x2))
print(x3, ": ", p.value(x3))
print(x4, ": ", p.value(x4))
print(x5, ": ", p.value(x5))
print(x6, ": ", p.value(x6))
print(x7, ": ", p.value(x7))
