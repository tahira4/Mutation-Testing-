import os


def apply_mutation(original_code, mutation_function, mutant_name):
    mutated_code = mutation_function(original_code)
    with open(f"mutants/{mutant_name}.py", "w") as mutant_file:
        mutant_file.write(mutated_code)


def mutate_arithmetic(original_code):
    # Example: Replace "+" with "-"
    return original_code.replace("+", "-")


def mutate_coefficients(original_code):
    # Example: Replace coefficients with "0"
    return original_code.replace("3", "0").replace("2", "0")


# Add more mutation functions as needed

def main():
    with open("Polynomial.py", "r") as file:
        original_code = file.read()

    # Apply mutations
    os.makedirs("mutants", exist_ok=True)
    apply_mutation(original_code, mutate_arithmetic, "mutant_arithmetic")
    apply_mutation(original_code, mutate_coefficients, "mutant_coefficients")


if __name__ == "__main__":
    main()
