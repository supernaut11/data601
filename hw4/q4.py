import random

people = ['a', 'a', 'a', 'a', 'a', 'k', 'k', 'k']

def check(table):
    # We want to see if there are any instances of kids together
    if table[0] == 'k' and table[-1] == 'k':
        return True

    for i in range(1, len(table)):
        if table[i] == 'k' and table[i-1] == 'k':
            return True

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