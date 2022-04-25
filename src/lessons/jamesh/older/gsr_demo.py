import random
import math
import numpy



def gsr(l):
    rng = numpy.random.default_rng()
    gsr_shuffled = []
    total_cards = len(l)
    # recognized that C(n, k) / 2^n fits a binomial distribution
    # with p = 0.5
    cards_to_grab = rng.binomial(total_cards, 0.5)
    # print(f"Cards to grab: {cards_to_grab}")
    left = list(l[: cards_to_grab])
    # print(left)
    right = list(l[cards_to_grab:])
    # print(right)
    while left != [] or right != []:
        chooser = rng.uniform(0.0, 1.0)
        if chooser < len(left) / (len(left) + len(right)):
            new_card = left.pop()

        else:
            new_card = right.pop()

        gsr_shuffled = [new_card] + gsr_shuffled

    return gsr_shuffled


def top_to_random(l):
    original_length = len(l)
    top_to_random_shuffled = list(l)
    top_card = top_to_random_shuffled.pop(0)
    top_to_random_shuffled.insert(random.randint(0, original_length - 1), top_card)
    return top_to_random_shuffled

def test_order(i, j, l):
    if l.index(i) < l.index(j):
        return True

    else:
        return False

def num_trials(err, prob):
    # Chebyshev's looks like this:
    # P(|X - E[X]| >= e) <= V[X] / e ** 2
    # lecture says that from Chebyshev's we get:
    # P(|X - E[X]| >= t * sqrt(V[X])) <= 1 / t ** 2
    # e = err in this case
    # prob = V[X] / e ** 2
    # solving for |X - E[X]|
    # E[X] should be 1 / 2, given problem instructions?
    # X should be Bernoulli with p = 1 / 2
    # E[X] would be 1 / 2, V[X] = 1 / 4
    # prototype: P(|X - 1/2} >= err) <= prob
    # Markov's looks like this:
    # P(X >= a) <= E[X] / a
    # lectures says that from Markov, we get:
    # P(X >= t * E[X]) <= 1 / t
    trials = math.floor(1 / (4 * err ** 2 * prob)) + 1
    return trials

def gsr_order_prob(n, k, i, j, err, prob):
    # n = number of cards in deck
    # k = number of shuffles
    # shuffle k times, then check if i comes before j in l with test_order
    # do this num_trial(err, prob) times
    # count successes from test_order
    gsr_list = list(range(n))
    number_of_trials = num_trials(err, prob)
    list_of_results = []
    while number_of_trials > 0:
        shuffled_deck = gsr_list
        while k > 0:
            shuffled_deck = gsr(shuffled_deck)
            # print(shuffled_deck)
            k = k - 1

        list_of_results += [test_order(i, j, shuffled_deck)]
        number_of_trials = number_of_trials - 1


    print(list_of_results.count(True))
    return sum(list_of_results) / len(list_of_results)

def top_to_random_order_prob(n, k, i, j, err, prob):
    top_to_random_list = list(range(n))
    number_of_trials = num_trials(err, prob)
    list_of_results = []
    while number_of_trials > 0:
        shuffled_deck = top_to_random_list
        while k > 0:
            shuffled_deck = top_to_random(shuffled_deck)
            # print(shuffled_deck)
            k = k - 1

        list_of_results += [test_order(i, j, shuffled_deck)]
        number_of_trials = number_of_trials - 1

    print(list_of_results.count(True))
    return sum(list_of_results) / len(list_of_results)

def main():
    input_list = range(52)
    test_trials = num_trials(0.1, 0.016)
    gsr_test = gsr_order_prob(52, 10, 51, 0, 0.1, 0.016)
    top_to_random_test = top_to_random_order_prob(52, 10000, 51, 0, 0.1, 0.016)
    print(gsr_test)
    print(top_to_random_test)


if __name__ == "__main__":
    main()
