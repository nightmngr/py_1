# func za sobiranje na site digits
def digit_sum(n):
  sum = 0
  for x in str(n):
    sum += int(x)
  return sum

# func za faktoriel
def factorial(x):
  rez = 1
  for i in range(x):
    rez *= i+1 # deka range ke dade 0, 1, 2... i ke se za 1 pomali
  return rez

# is it prime?
def is_prime(x):
    if x < 2: # CodeCad vika pod 2 ne se primes;
              # uslovot da e prime e da e delliv samo so sebe i so 1 i radi toa go isklucuvaat 1 od primes
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

# reverse
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

# anti vowel
def anti_vowel(text):
  word = ""
  for x in text:
    if x != "A" and x != "a" \
    and x != "E" and x != "e" \
    and x != "I" and x != "i" \
    and x != "O" and x != "o" \
    and x != "U" and x != "u":
      word += x
  return word  

print anti_vowel("Hey look Words!")

# scrabble score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  total = 0
  for letter in word.lower():
    for leter in score:
      if letter == leter:
        total += score[leter]
  return total

print scrabble_score("Big G")

# censor
# (vo text da se cenzurira word)
def censor(text, word):
	return text.replace(word, "*" * len(word))

# count
# vrakja kolku pati se sretnuva item vo sequence
# sequence e list
# The item you input may be an integer, string, float, or even another list!
def count(sequence, item):
  cnt = 0
  for x in sequence:
    if x == item:
      cnt += 1
  return cnt

# purify
# brise neparni od lista
def purify(some_list):
  new_list = []
  for x in some_list:
    if x % 2 == 0:
      new_list.append(x)
  return new_list

# remove duplicates
def remove_duplicates(some_list):
  new_list = []
  for x in some_list:
    if x not in new_list:
      new_list.append(x)
  return new_list

# median (sredina na sortirana lista)
def median(some_list):
  sorted_list = sorted(some_list)
  dolz = len(sorted_list)
  if dolz % 2 == 1:
    return sorted_list[int(dolz/2)]
  else:
    return (sorted_list[int(dolz/2)] + sorted_list[int(dolz/2) - 1]) / 2.0