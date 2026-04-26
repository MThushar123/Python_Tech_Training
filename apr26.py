def solveEquation(equation):
    def parse_equation(equation):
        left, right = equation.split('=')
        left_coef, left_const = parse_side(left)
        right_coef, right_const = parse_side(right)

        coef = left_coef - right_coef
        const = left_const - right_const
        
        return coef, const
    
    def parse_side(side):
        coef = 0
        const = 0
        i = 0
        n = len(side)
        
        while i < n:
            if side[i] == '+':
                i += 1
            elif side[i] == '-':
                sign = -1
                i += 1
            else:
                sign = 1

            num = 0
            while i < n and side[i].isdigit():
                num = num * 10 + int(side[i])
                i += 1
            
            if i < n and side[i] == 'x':
                if num == 0:
                    coef += sign * 1
                else:
                    coef += sign * num
                i += 1
            else:
                const += sign * num
        
        return coef, const
    
    coef, const = parse_equation(equation)
    
    if coef == 0:
        if const == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        x = -const // coef
        return f"x={x}"

def main():
    equation = input("Enter the equation (e.g., x+5-3+x=6+x-2): ").strip()
    result = solveEquation(equation)
    print("Result:", result)

if __name__ == "__main__":

    test_cases = [
        "x+5-3+x=6+x-2",
        "2x=x"
    ]
    
    print("Test Results ")
    for eq in test_cases:
        print(f"Equation: {eq}")
        print(f"Result: {solveEquation(eq)}")
        print()
    
    print(" User Input ")
    main()