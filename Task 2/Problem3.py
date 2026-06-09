def reverse_complement(pattern):
  complement_map = {'A': 'T', 'T': 'A', 'C': 'G','G': 'C'}

  reversed_pattern = pattern[::-1]

  rev_comp =""
  for nucleotide in reversed_pattern:
      rev_comp += complement_map[nucleotide]

  return rev_comp

pattern_input = "AAAACCCGGT"
result = reverse_complement(pattern_input)

print(result)

