def hamming_distance(p, q):
    mismatches = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            mismatches += 1
    return mismatches
def approximate_pattern_matching(pattern, text, d):
    positions = []
    k=len(pattern)
    for i in range(len(text) -k +1):
        window = text[i:i+k]
        if hamming_distance(pattern, window) <= d:
            positions.append(i)
    return positions
    
    
    
    
pattern = "ATTCTGGA"

text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
d = 3

result = approximate_pattern_matching(pattern, text, d)
print(" ".join(map(str, result)))                   
