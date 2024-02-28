# IV Delta encoding

def delta_encoding(array):
    if not array:
        return []

    result = [array[0]]
    for i in range(1, len(array)):
        difference = array[i] - array[i - 1]
        result.append(difference)
    return result

# Exemples
original_array = [1000, 800, 802, 1000, 1003]
encoded_array = delta_encoding(original_array)
print(encoded_array)
