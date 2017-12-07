def health_calculator(age, apples_ate, num_cigeratte):
    answer = (100 - age) + (apples_ate * 3.5) - (num_cigeratte * 2)
    print(answer)


mamun = [23, 1, 0.25]
health_calculator(mamun[0], mamun[1], mamun[2])
health_calculator(*mamun)