import math
import random as rnd

THROTTLE_NUMBER = 10
MAX_ENT = 10
MIN_X = 0
MAX_X = 35
EXTREMUM = max
MUTATION_CHANCE = 0.1


def fitness(x):
    return math.cos(x) * (x - 3) * (x - 9) * (x - 1.5) * (x - 15) * (x - 4)


def get_max_pow_2(x):
    power = 0
    while True:
        if math.pow(2, power + 1) > x:
            return power
        else:
            power += 1


if __name__ == '__main__':
    population = [rnd.randint(MIN_X, MAX_X) for _ in range(MAX_ENT)]
    end_counter = 0

    population_fitness = list(map(fitness, population))
    best_result = EXTREMUM(population_fitness)

    while end_counter < THROTTLE_NUMBER:

        # Fitness
        population_fitness = list(map(fitness, population))

        if best_result == EXTREMUM(population_fitness):
            end_counter += 1
        else:
            end_counter = 0

        # Selection
        summa = sum(population_fitness)
        roll = list(map(lambda x: 2 * 3.14 * x / sum(population_fitness), population_fitness))

        parents = []
        for _ in range(MAX_ENT):
            numb = rnd.random() * 2 * 3.14
            summa = 0
            for i in range(MAX_ENT):
                if summa <= numb < (summa + roll[i]):
                    parents.append(population[i])
                    break
                else:
                    summa += roll[i]

        # Crossover
        new_population = []
        for i in range(MAX_ENT // 2):
            par_1 = parents[2 * i]
            par_2 = parents[2 * i + 1]

            mask = rnd.getrandbits()
            ch_1 = (par_1 & mask) | (par_2 & (not mask))
            ch_2 = (par_1 & (not mask)) | (par_2 & mask)

            new_population.append(ch_1)
            new_population.append(ch_2)

        # Mutation
        for i in range(MAX_ENT):
            if rnd.random() < MUTATION_CHANCE:
                elem = new_population[i]
                max_pow = get_max_pow_2(elem)
                pos_1 = rnd.

