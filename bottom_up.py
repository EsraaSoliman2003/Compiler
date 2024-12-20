def bottom_up_parser(grammar, text):
    stack = []
    text = list(text)
    while True:
        if stack == ['S'] and not text:
            return "Accepted"
        if text:
            stack.append(text.pop(0))

        reduced = False
        for non_terminal, rules in grammar.items():
            for rule in rules:
                if "".join(stack[-len(rule):]) == rule:
                    stack = stack[:-len(rule)] + [non_terminal]
                    reduced = True
                    break
            if reduced:
                break

        if not text and not reduced:
            break

    return "Rejected"

grammar = { 'S': ['aSB', 'b'], 'B': ['a', 'bBa'] }
text = "aba"

print(bottom_up_parser(grammar, text))

