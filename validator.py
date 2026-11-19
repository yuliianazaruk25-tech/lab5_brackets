
BRACKETS = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<"
}

OPENING = set(BRACKETS.values())
CLOSING = set(BRACKETS)


def validate_brackets(text):
    stack = []
    errors = []

    for index, char in enumerate(text):
        if char in OPENING:
            stack.append((char, index))

        elif char in CLOSING:
            if stack and stack[-1][0] == BRACKETS[char]:
                stack.pop()
            else:
                errors.append(index)

    errors.extend(index for char, index in stack)
    errors.sort()

    if errors:
        positions = ", ".join(str(i + 1) for i in errors)
        raise ValueError(
            f"Дужки незбалансовані на позиціях {positions}"
        )

    return True
