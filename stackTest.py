eq0 = " 1 + 2"
eq1 = "10 + 20 * 2"
eq2 = "foo / 30 + 7"
eq3 = "10 + 20 - 47 * 2"
eq4 = "28 / 4"

def equationSolver(eq):
        # Goal is to split the numbers from the operators
        numbers = []
        operators = []
        equation = eq.split()

        for term in equation:
            if term.isdigit():
                numbers.append(term)
            elif term == "+" or term == "-" or term == "*" or term == "/":
                operators.append(term)
            else:
                # anything needs to return Nan or None
                print("Nan => STRING IN EQUATION")
                return None

        while operators:
            numerand1 = int(numbers.pop())
            numerand2 = int(numbers.pop())

            if operators:
                op = operators.pop()
            else:
                break

            if op == "+":
                numbers.append(numerand2 + numerand1)
                continue
            elif op == "-":
                numbers.append(numerand2 - numerand1)
                continue
            if op == "*":
                numbers.append(numerand2 * numerand1)
                continue
            elif op == "/":
                numbers.append(numerand2 / numerand1)
                continue
            else:
                break

        return numbers[0]

print(equationSolver(eq3))