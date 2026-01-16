# Reverse Thinking Problem Solver
# Finds possible number combinations for a given result


def reverse_solver(target):
    results = []

    for i in range(1, target + 1):
        for j in range(1, target + 1):

            # Addition
            if i + j == target:
                results.append(f"{i} + {j} = {target}")

            # Multiplication
            if i * j == target:
                results.append(f"{i} × {j} = {target}")

    return results


# Main Program
def main():
    try:
        target = int(input("Enter the final result: "))

        solutions = reverse_solver(target)

        if solutions:
            print("\nPossible explanations:")
            for sol in solutions:
                print(sol)
        else:
            print("No possible combinations found.")

    except ValueError:
        print("Please enter a valid number")


# Run Program
main()
