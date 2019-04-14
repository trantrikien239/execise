with open('./data/eu_countries.csv','r') as file:
    number_of_countries = 0
    for line in file:
        number_of_countries += 1
    print("Europe has " + str(number_of_countries) + ' countries.')