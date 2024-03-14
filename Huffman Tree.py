
# freq of the format { char: freq}
# huffman tree is serialized in an array

def huffman(freq:dict[str:int]):
    sorted_freq = sorted(freq.items(), key=lambda x: x[1])
    print(sorted_freq)
    while len(sorted_freq) > 1:
        left = sorted_freq.pop(0)
        right = sorted_freq.pop(0)
        sorted_freq.append((left[0] + right[0], left[1] + right[1]))
        sorted_freq.sort(key=lambda x: x[1])
        print(sorted_freq)
    return sorted_freq[0][0]

print(huffman({'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}))


