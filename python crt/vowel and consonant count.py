input_str=input("enter a string:")
vowel_lcount=0
vowel_ucount=0
consonant_count=0
for ch in input_str:
    if ch.isalpha():
        if ch in['a','e','i','o','u']:
            vowel_lcount+=1
        elif ch in['A','E','I','O','U']:
            vowel_ucount+=1
        else:
            consonant_count+=1
print(f"vowel lower count:{vowel_lcount}")
print(f"vowel upper count:{vowel_ucount}")
print(f"consonant count:{consonant_count}")
