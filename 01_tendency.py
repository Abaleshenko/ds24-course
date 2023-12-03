from random import sample

sequence = [*range(100)]
collection = sample(sequence, 
                    int(len(sequence) * .25))


# task1 - simple
def mean(start: list) -> float:
    return sum(start) / len(start)

# print(mean(collection))