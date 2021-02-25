'''
https://www.codewars.com/kata/586d6cefbcc21eed7a001155
6 kyu
'''
def longest_repetition(chars):
    # Create answer variables
    largest_sum = 0
    letter = ''
    # Enumerate through string
    for n, i in enumerate(chars):
        count = 0
        temp_sum = 0
        # Count consecutive characters
        while i == chars[n+count]:
            count += 1
            temp_sum += 1
            if n+count == len(chars):
                break
        # Update answer if necessary
        if temp_sum > largest_sum:
            largest_sum = temp_sum
            letter = i
    # Return answer
    return (letter,largest_sum)