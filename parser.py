def addGrammer():
    grammar = { 'S': [], 'B': [] }

    for non_terminal, rules in grammar.items():
        for i in range(1, 3):
            rule = input(f"Enter rule number {i} for non-terminal '{non_terminal}': ")
            rules.append(rule)

    return grammar


def is_simple_grammar(grammar):
    for rules in grammar.values():
        # Check for epsilon
        if '' in rules:
            return False
        
        # Check for correct form
        for rule in rules:
            if rule[0].isupper():
                return False
            
        # Check for disjointness
        if rules[0][0] == rules[1][0]:
            return False
    return True


def parser(grammar, string):
    stack = ['S']
    string = list(string)
    while stack:
        top = stack.pop(0)
        if top.isupper():
            if top in grammar:
                for rule in grammar[top]:
                    if rule[0] == string[0]:
                        stack = list(rule) + stack
                        break
                else:
                    return stack, string
            else:
                return stack, string
        elif top == string[0]:
            string.pop(0)
        else:
            return stack, string
        
        if (string == [] or stack == []):
            return stack, string


def main():
    while True:
        grammar = addGrammer()
        
        if not is_simple_grammar(grammar):
            print("The Grammar isn't simple. Try again.")
            continue

        while True:
            string = input("Enter the string you want to check: ")
            if not string:
                print("Invalid input. String cannot be empty.")
                continue

            stack, unchecked = parser(grammar, string)

            print(f"Stack after finished: {stack}")
            print(f"The rest of unchecked string: {unchecked}")

            if not unchecked and not stack:
                print("Your input string is Accepted.")
            else:
                print("Your input string is Rejected.")

            print("===============================")
            print("1-Another Grammar.")
            print("2-Another String.")
            print("3-Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                break
            elif choice == "2":
                continue
            elif choice == "3":
                return

if __name__ == "__main__":
    main()
