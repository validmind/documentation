# StabilityAnalysisRandomNoise

Randomly swap two adjacent words.
if len(word_list) < 2:
return word_list

index = random.randint(0, len(word_list) - 2)
word_list[index], word_list[index + 1] = word_list[index + 1], word_list[index]

return word_list


def introduce_typo(word):
Introduce a random typo in a word.