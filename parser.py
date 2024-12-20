def add_rule(non_terminal, grammar):
    # Add two production rules for a given non-terminal
    for i in range(1, 3):
        production = input(f"Enter rule number {i} for non-terminal '{non_terminal}': ")
        grammar.setdefault(non_terminal, []).append(production)

def is_simple_grammar(grammar):
    # Check for epsilon productions
    for productions in grammar.values():
        if '' in productions:
            return False

    # Check for disjointness and correct form
    for productions in grammar.values():
        first_terminals = set()
        for production in productions:
            if not production or production[0].isupper():
                return False
            if production[0] in first_terminals:
                return False
            first_terminals.add(production[0])
    return True

def parser(grammar, text):
    stack = ['S']
    text = list(text)
    while stack:
        top = stack.pop(0) 
        if top.isupper():
            if top in grammar:
                for rule in grammar[top]:
                    if rule[0] == text[0]:
                        stack = list(rule) + stack
                        break  
                else:
                    return stack, text
            else:
                return stack, text
        elif text and top == text[0]:
            text.pop(0)
        else:
            return stack, text
        
        if (text == [] or stack == []):
            return stack, text


def main():
    while True:
        grammar = {}
        non_terminals = ['S', 'B']

        for non_terminal in non_terminals:
            add_rule(non_terminal, grammar)

        if not is_simple_grammar(grammar):
            print("The Grammar isn't simple. Try again.")
            continue

        while True:
            sequence = input("Enter the string you want to check: ")
            if not sequence:
                print("Invalid input. Sequence cannot be empty.")
                continue


            stack, unchecked = parser(grammar, sequence)

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
            elif choice == "3":
                return

if __name__ == "__main__":
    main()
