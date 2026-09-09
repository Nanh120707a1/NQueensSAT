from pysat.solvers import Solver
N = int(input());
def var(i, j):
    return (i-1)*N + j;
clauses = []
# mỗi hàng có ít nhất một queen
for i in range (1, N+1):
    clause = []
    for j in range (1, N+1):
        clause.append(var(i,j))
    clauses.append(clause);

# mỗi hàng có nhiều nhất một queens
for i in range (1, N+1):
    for j in range (1, N):
        for k in range (j+1, N+1):
            clauses.append([-var(i,j), -var(i,k)])

# mỗi cột có nhiều nhất một queens
for j in range (1, N+1):
    for i in range (1, N):
        for k in range (i+1, N+1):
            clauses.append([-var(i,j), -var(k,j)])

# đường chéo
for i in range (1, N+1):
    for j in range (1, N+1):
        for l in range (i+1, N+1):
            for r in range (1, N+1):
                if abs(i-l) == abs(j-r):
                    clauses.append([-var(i,j), -var(l,r)])

with Solver() as solver:
    for clause in clauses:
        solver.add_clause(clause)
    if solver.solve():
        print("SAT")
        model = solver.get_model()
        print(model)
    else:
        print("UNSAT")