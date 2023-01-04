#!/usr/bin/env python3

from pysat.formula import CNF, WCNF
from pysat.examples.rc2 import RC2
from pysat.solvers import Solver
import sys


def solve_cnf(input_file, output_file):
    cnf = CNF(input_file)
    solver = Solver(name='g4')
    solver.append_formula(cnf)
    status = solver.solve()

    with open(output_file, 'w') as f:
        if status:
            f.write("True\n")
            f.write(str(len(solver.get_model())))
            f.write('\n')
            f.write(''.join(list(map(lambda x: str(x) + ' ', solver.get_model()))))
        else:
            f.write("False\n")


def solve_wcnf(input_file, output_file):
    wcnf = WCNF(input_file)
    with RC2(wcnf) as rc2:
        nodes = rc2.compute()
        cost = rc2.cost

    with open(output_file, 'w') as f:
        f.write(str(len(nodes)) + ' ' + str(cost))
        f.write('\n')
        f.write(''.join(list(map(lambda x: str(x) + ' ', nodes))))
        f.write('\n')


def solve_sat(input_file, output_file):
    with open(input_file) as f:
        clause_type = f.readline().split()[1]

    if clause_type == "cnf":
        solve_cnf(input_file, output_file)
    elif clause_type == "wcnf":
        solve_wcnf(input_file, output_file)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Wrong number of arguments (received {sys.argv})", file=sys.stderr)
        print("    Usage: python sat_oracle.py <input_filename> <output_filename>")
        sys.exit(-1)
    solve_sat(sys.argv[1], sys.argv[2])
