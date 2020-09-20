import random

people = ['a', 'a', 'a', 'a', 'a', 'a', 'k', 'k']

def check(table):
    # Assume indices 1-3 are one long side, 4-6 the other
    if table[1] == 'k' and table[2] == 'k' or \
        table[2] == 'k' and table[3] == 'k' or \
        table[4] == 'k' and table[5] == 'k' or \
        table[5] == 'k' and table[6] == 'k':
        return True
    else:
        return False

if __name__ == "__main__":
    successes = 0
    trials = 0

    for i in range(1000000):
        trials += 1

        table = people[:]
        random.shuffle(table)
        result = check(table)

        if result:
            successes += 1
        
        if trials % 1000 == 0:
            print(f"{trials} trials complete")
    
    print(f"successes, trials: {successes}, {trials}")
    print(f"success rate: {successes / trials}")