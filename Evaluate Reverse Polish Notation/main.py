def evalRPN(tokens: list[str]) -> int:

    stack = []

    for i in tokens:
        if i == "+":
            a = stack.pop()
            b = stack.pop()
            result = int(a + b)
            stack.append(result)
            print("Operation +")
            print(f"{a} and {b} result is {result}")

        elif i == "*":
            a = stack.pop()
            b = stack.pop()
            result = int(a * b)
            stack.append(int(result))
            print("Operation *")
            print(f"{a} and {b} result is {result}")

        elif i == "-":
            a = stack.pop()
            b = stack.pop()
            result = int(b - a)
            stack.append(result)
            print("Operation -")
            print(f"{a} and {b} result is {result}")

        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            result = int(b / a)
            stack.append(int(result))
            print("Operation /")
            print(f"{a} and {b} result is {result}")

        else:
            stack.append(int(i))
            print(f"Appending {int(i)}")

    ans = stack.pop()
    return ans


print(evalRPN(["4", "13", "5", "/", "+"]))
print("Expected 6")
