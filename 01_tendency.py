from random import sample

sequence = [*range(100)]
collection = sample(sequence, 
                    int(len(sequence) * .25))


# task1 - simple
def mean(start: list) -> float:
    return sum(start) / len(start)

# print(mean(collection))


#task2
def find_average(*args) -> float:
    result = 0
    for i in args[0]:
        result += i
    return result / len(args[0])

# print(find_average(collection))