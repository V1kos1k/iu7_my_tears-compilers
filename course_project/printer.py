def print_tree(ast_string):
    tabs = 0
    for c in ast_string:
        if c == '(':
            print("\n", end='')
            for i in range(tabs):
                print("  ", end='')
            tabs += 1
        elif c == ')':
            tabs -= 1
        print(c, end='')