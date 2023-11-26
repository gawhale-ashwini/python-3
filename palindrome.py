def is_palindrome(s):
    # Remove spaces and make all letters lowercase
    s = s.replace(" ", "").lower()
    
    # Compare the word or phrase with its reverse
    return s == s[::-1]

# Test cases
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("Hello"))  