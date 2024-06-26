#You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is *z*."

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
combined_names = name1 + name2
combined_names_lower = combined_names.lower()
t = combined_names_lower.count("t")
r = combined_names_lower.count("r")
u = combined_names_lower.count("u")
e= combined_names_lower.count("e")
first_digit = t + r + u + e
l = combined_names_lower.count("l")
o = combined_names_lower.count("o")
v = combined_names_lower.count("v")
e = combined_names_lower.count("e")
second_digit = l + o + v + e
final_digit = int(str(first_digit) + str(second_digit))

if (final_digit < 10) or (final_digit > 90):
  print(f"Your score is {final_digit}, you go together like coke and mentos.")
elif (final_digit >= 40) and (final_digit <= 50):
  print(f"Your score is {final_digit}, you are alright together.")
else:
  print(f"Your score is {final_digit}.")
