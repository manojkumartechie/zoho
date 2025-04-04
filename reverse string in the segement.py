def reverseStr(s: str, k: int) -> str:
    s = list(s)  # Convert the string to a list to allow modifications
    
    for i in range(0, len(s), 2 * k):
        # Reverse the first k characters in every 2k block
        s[i:i + k] = reversed(s[i:i + k])
    
    return ''.join(s)  # Convert the list back to a string

# Example usage:
s1, k1 = "abcdefg", 2
print(f"Input: s = {s1}, k = {k1}\nOutput: {reverseStr(s1, k1)}")

s2, k2 = "abcd", 2
print(f"Input: s = {s2}, k = {k2}\nOutput: {reverseStr(s2, k2)}")
