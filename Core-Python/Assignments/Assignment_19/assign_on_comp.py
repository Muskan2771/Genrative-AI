# Q1
nums_div_8 = [i for i in range(1, 1001) if i % 8 == 0]
print(nums_div_8)

#Q2
nums_with_6 = [i for i in range(1, 1001) if '6' in str(i)]
print(nums_with_6)

#Q3
s = input("Enter a string: ")

spaces = sum(1 for ch in s if ch == ' ')
print("Total spaces:", spaces)

#Q4
s = input("Enter a string: ")

no_vowels = ''.join(ch for ch in s if ch.lower() not in 'aeiou')
print("String without vowels:", no_vowels)

#Q5
s = input("Enter a string: ")

small_words = [word for word in s.split() if len(word) < 5]
print("Words with less than 5 letters:", small_words)

#Q6
s = input("Enter a sentence: ")

word_len = {word: len(word) for word in s.split()}
print(word_len)

#Q7
nums = [n for n in range(1, 1001) if any(n % d == 0 for d in range(1, 10))]
print(nums)
