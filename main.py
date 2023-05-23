from person import Person, get_person_list_costs
import random
import csv

with open('insurance.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    person_list = []

    # Read each row in the CSV file

    for row in reader:
        # Access the data in each column of the row
        if row[1] == 'female':
            row[1] = 0
        else:
            row[1] = 1

        if row[4] == 'yes':
            row[4] = 1
        else:
            row[4] = 10

        if row[5] == 'southwest':
            row[5] = 3
        elif row[5] == 'southeast':
            row[5] = 2
        elif row[5] == 'northwest':
            row[5] = 1
        elif row[5] == 'northeast':
            row[5] = 0

        person = Person(
            int(row[0]),
            int(row[1]),
            round(float(row[2]), 2),
            int(row[3]),
            int(row[4]),
            int(row[5]),
            round(float(row[6]), 2)
            )

        person_list.append(person)

        person.print_details()


for p in person_list:
    print(p.get_costs().content)


'''
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

'''



