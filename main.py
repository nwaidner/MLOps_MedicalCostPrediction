from person import Person, get_person_list_costs
import random

person_list = []

for _ in range(50000):
    age = random.randint(18, 65)
    sex = random.choice([0, 1])
    bmi = round(random.uniform(18.5, 24.9), 2)
    children = random.randint(0, 3)
    smoker = random.choice([0, 1])
    region = random.randint(0, 3)
    charges = round(random.uniform(1000, 10000), 2)

    person = Person(age, sex, bmi, children, smoker, region, charges)
    person_list.append(person)


for p in person_list:
    print(p.get_costs().content)



