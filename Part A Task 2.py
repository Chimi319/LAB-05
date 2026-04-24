def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        # Push opening brackets
        if char in "({[":
            stack.append(char)

        # Check closing brackets
        elif char in ")}]":
            if not stack:
                return "Not Balanced"
            if stack[-1] == pairs[char]:
                stack.pop()
            else:
                return "Not Balanced"

    # If stack is empty, it is balanced
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Not Balanced"


# Example inputs
expr1 = "(a+b)*(c+d)"
expr2 = "(a+b)*(c+d"

print(expr1, ":", is_balanced(expr1))
print(expr2, ":", is_balanced(expr2))