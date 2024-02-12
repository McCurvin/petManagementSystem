#Mc Curvin Royeras
def createPet(name, age, species, breed, gender, price):
    return [name, age, species, breed, gender, price]

def addPet(pet_list, pet):
    pet_list.append(pet)

def searchPet(pet_list, name):
    for pet in pet_list:
        if pet[0] == name:
            return pet
    return None

def insertPet(pet_list, index, pet):
    pet_list.insert(index, pet)

def editPet(pet_list, name, new_value):
    for pet in pet_list:
        if pet[0] == name:
            index = pet_list.index(pet)
            pet_list[index] = new_value

def viewPets(pet_list):
    for pet in pet_list:
        print(f"Name: {pet[0]}, Age: {pet[1]}, Species: {pet[2]}, Breed: {pet[3]}, Gender: {pet[4]}, Price: {pet[5]}")

def deletePet(pet_list, name):
    pet_list[:] = [pet for pet in pet_list if pet[0] != name]

def countPets(pet_list):
    return len(pet_list)

def viewSpecies(pet_list, species):
    for pet in pet_list:
        if pet[2] == species:
            print(f"Name: {pet[0]}")

def viewBreed(pet_list, breed):
    for pet in pet_list:
        if pet[3] == breed:
            print(f"Name: {pet[0]}")

def viewGender(pet_list, gender):
    for pet in pet_list:
        if pet[4] == gender:
            print(f"Name: {pet[0]}")

def viewExpensive(pet_list):
    expensive_pet = max(pet_list, key=lambda x: x[5])
    print(f"Name: {expensive_pet[0]}")

def viewEldest(pet_list):
    eldest_pet = max(pet_list, key=lambda x: x[1])
    print(f"Name: {eldest_pet[0]}")

pet_list = []
pet_gender = []
pet_breed = []
pet_age = []
pet_price = []
pet_age = []

while True:
    print("\nMenu:")
    print("[1]Add  [2]Insert  [3]Search  [4]Edit  [5]View  [6]Delete  [7]Count  [8]Terminate")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter pet name: ")
        age = int(input("Enter pet age: "))
        species = input("Enter pet species: ")
        breed = input("Enter pet breed: ")
        gender = input("Enter pet gender: ")
        price = float(input("Enter pet price: "))
        pet = createPet(name, age, species, breed, gender, price)
        addPet(pet_list, pet)

    elif choice == "2":
        index = int(input("Enter index to insert: "))
        name = input("Enter pet name: ")
        age = int(input("Enter pet species: "))
        species = input("Enter pet species: ")
        breed = input("Enter pet breed: ")
        gender = input("Enter pet gender: ")
        price = float(input("Enter pet price: "))
        pet = createPet(name, age, species, breed, gender, price)
        insertPet(pet_list, index, pet)
    elif choice == "3":
        name = input("Enter pet name to search: ")
        result = searchPet(pet_list, name)
        if result:
            print(f"Pet found: {result}")
        else:
            print("Pet not found.")
    elif choice == "4":
        # Edit pet
        name = input("Enter pet name to edit: ")
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        new_species = input("Enter new species: ")
        new_breed = input("Enter new breed: ")
        new_gender = input("Enter new gender: ")
        new_price = float(input("Enter new price: "))
        new_pet = createPet(new_name, new_age, new_species, new_breed, new_gender, new_price)
        editPet(pet_list, name, new_pet)

    elif choice == "5":
        viewBy = input("Enter view type (all, species, breed, gender, expensive, eldest): ").lower()
        if viewBy == "all":
            viewPets(pet_list)
        elif viewBy == "species":
            specimen = input("Enter species to view: ")
            viewSpecies(pet_list, specimen)
        elif viewBy == "breed":
            breed = input("Enter breed to view: ")
            viewBreed(pet_list, breed)
        elif viewBy == "gender":
            gender = input("Enter gender to view: ")
            viewGender(pet_list, gender)
        elif viewBy == "expensive":
            viewExpensive(pet_list)
        elif viewBy == "eldest":
            viewEldest(pet_list)

    elif choice == "6":
        name = input("Enter pet name to delete: ")
        deletePet(pet_list, name)

    elif choice == "7":
        count = countPets(pet_list)
        print("Number of pets:", count)

    elif choice == "8":
        print("Program terminating...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")



