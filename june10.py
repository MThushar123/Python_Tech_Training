def addOperators(num, target):
    result = []

    def backtrack(index, expr, value, prev):
        if index == len(num):
            if value == target:
                result.append(expr)
            return

        for i in range(index, len(num)):
            if i > index and num[index] == '0':
                break

            curr_str = num[index:i + 1]
            curr_num = int(curr_str)

            if index == 0:
                backtrack(i + 1, curr_str, curr_num, curr_num)
            else:
                backtrack(
                    i + 1,
                    expr + "+" + curr_str,
                    value + curr_num,
                    curr_num
                )

                backtrack(
                    i + 1,
                    expr + "-" + curr_str,
                    value - curr_num,
                    -curr_num
                )

                backtrack(
                    i + 1,
                    expr + "*" + curr_str,
                    value - prev + (prev * curr_num),
                    prev * curr_num
                )

    backtrack(0, "", 0, 0)
    return result

num = input("Enter numeric string: ")
target = int(input("Enter target value: "))

result = addOperators(num, target)

print("Valid Expressions:")
for expr in result:
    print(expr)

if not result:
    print("No valid expression found.")