
str=input('enter string..>')
vowels="aeiouAEIOU"
consonat_count=0
for i in str:
    if ("a"<=i <="z") or ("A"<=i<="Z"):
        is_vowels=False
        for v in vowels:
            if i== v:
                is_vowels=True
                break
        if not is_vowels:
             consonat_count+=1 
print("total cosonanat are",consonat_count)