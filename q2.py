import random

def build_balls(num_black, max_balls):
    # 0 -> black, 1 -> white
    return [0] * num_black + [1] * (max_balls - num_black)

def check(three_balls):
    # If exactly one black ball, sum will be 2 since we mapped 1 to white
    if sum(three_balls) == 2:
        return True
    else:
        return False

if __name__ == "__main__":
    successes = 0
    trials = 0

    balls = build_balls(3, 8)

    for i in range(1000000):
        trials += 1

        random.shuffle(balls)
        result = check(balls[:3])

        if result:
            successes += 1
        
        if trials % 1000 == 0:
            print(f"{trials} trials complete")
    
    print(f"successes, trials: {successes}, {trials}")
    print(f"success rate: {successes / trials}")
    balls.sort()
    print(f"{balls}")