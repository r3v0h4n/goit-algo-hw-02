def are_brackets_symmetric(expression: str) -> str:
    stack = []
    opening_brackets = {'(', '{', '['}
    closing_brackets = {')', '}', ']'}
    
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets: 
            if stack == [] or brackets[char] != stack.pop():
                return False
    
    return not stack

def main():
    print(are_brackets_symmetric("( ){[ 1 ]( 1 + 3 )( ){ }}"))
    print(are_brackets_symmetric("( 23 ( 2 - 3);"))
    print(are_brackets_symmetric("( 11 }"))

if __name__ == "__main__":
    main()