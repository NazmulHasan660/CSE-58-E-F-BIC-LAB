def frequent_words(text,k):
    freq_map = {}
    n= len(text)

    for i in range(n-k+1):
       pattern = text[i:i+k]
       if pattern in freq_map:
          freq_map[pattern] += 1

       else:
           freq_map[pattern] = 1

   
    max_count = max(freq_map.values())


    most_frequent = []
    for pattern, count in freq_map.items():
       if count == max_count:
          most_frequent.append(pattern)
    return most_frequent


text_input = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k_input = 4

result = frequent_words(text_input,k_input)

print(" ".join(result))
