# Loop to get user input (name and age of each family member)
# Store each person in a dictionary
# Store all people in a list
# Save each name and age to a text file

def main():
    family = get_family()
    save_my_family(family)

def get_family():
    continue_bool = 'Y'
    family = []
    while continue_bool == 'Y':
        name = input('\nEnter name: ')
        age = input('Enter age: ')
        person = {'name': name, 'age': age}
        family.append(person)
        user_input = input('Continue? (Y/n) ') 
        continue_bool = 'n' if user_input == 'n' else 'Y'

        # if user_input == 'n':
        #     continue_bool = 'n'
        # else:
        #     continue_bool = 'Y'

    return family

def save_my_family(family):
    file = open('family.txt', 'w')
    file.write('Here is a list of your family members.\n\n')
    for person in family:
        file.write(person['name'] + ' is ' + person['age'] + ' years old.\n')

main()