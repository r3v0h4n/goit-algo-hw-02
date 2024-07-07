from collections import deque

def is_palindrome(s: str) -> bool:
    s = s.lower()
    
    dq = deque(s)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    
    return True

def main():
    print(is_palindrome("aa"))
    print(is_palindrome("a b a"))
    print(is_palindrome("hello"))
    print(is_palindrome("tenet"))
    print(is_palindrome("test"))

if __name__ == "__main__":
    main()