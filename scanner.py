import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

def lex(input_str):
    tokens = []
    pos = 0

    token_exprs = [
        (r'//.*', 'COMMENT'),  # Single-line comment
        (r'/\*.*?\*/', 'COMMENT_BLOCK'),  # Multi-line comment
        (r'\b(int|float|char|if|else|while|for)\b', 'KEYWORD'),  # Keywords
        (r'\d+', 'INTEGER'),
        (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
        (r'[\+\-\*/=<>]', 'OPERATOR'),
        (r'[{}();]', 'SPECIAL_CHARACTER'),  # Special characters
        (r'\s+', 'WHITESPACE'),  # Ignore whitespace
        (r'"[^"]*"', 'STRING_LITERAL'),  # String literals (double quotes)
    ]

    while pos < len(input_str):
        match = None
        for token_expr, token_type in token_exprs:
            match = re.match(token_expr, input_str[pos:])
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE':
                    tokens.append(Token(token_type, value))
                pos += len(value)
                break
        if not match:
            print(f"Invalid character: {input_str[pos]}")
            pos += 1  # Move to the next character

    return tokens

print("Please enter the code to lex (type 'END' on a new line to finish):")

input_lines = []
while True:
    line = input()
    if line.strip() == 'END':  
        break
    input_lines.append(line)

input_code = ' '.join(input_lines)

print(f"Entered code: {input_code}")

tokens = lex(input_code)

for token in tokens:
    print(f"Token: {token.type}, Value: {token.value}")
