from random import sample

sequence = [*range(100)]
collection = sample(sequence, 
                    int(len(sequence) * .25))


print(collection)