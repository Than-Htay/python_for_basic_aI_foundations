import re
text="hello thanhtay0450@gmai.com pyThon??? Is      easy and  is fUn "
lower_text=text.lower()
print(lower_text)
break_line=lower_text.split()
print(break_line)
join_split=" ".join(break_line)
print(join_split)
no_email = re.sub(r'\S+@\S+', '',join_split)
print(f"{no_email}............")
clean_text=" ".join(no_email.split())
print(clean_text)
remove_special=re.sub(r'[^a-zA-Z0-9\s]','',clean_text)
print(remove_special)
token_text=remove_special.split()
print(token_text)
frequency={}

for word in token_text:
    if word in frequency:
        frequency[word]+=1
    else:
        frequency[word]=1
print(frequency)
sort_word=sorted(frequency.items(), key=lambda item: item[1], reverse=True)

print(sort_word)


try:
    n = int(input("Enter the number of words you want: "))

except ValueError:
    print("Please enter a valid whole number.")

else:
    top_words = sort_word[:n]
    print(" ".join(word for word, count in top_words))

