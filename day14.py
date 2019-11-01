recipes = [3,7]
input = 320851
elf_a = 0
elf_b = 1
while len(recipes) < input+10:
    new_recipe = recipes[elf_a] + recipes[elf_b]
    #print(new_recipe)
    recipes.extend(map(int, str(new_recipe)))
    elf_a = (elf_a+recipes[elf_a] + 1)% len(recipes)
    elf_b = (elf_b+recipes[elf_b]+1)% len(recipes)

#print(''.join(map(str,recipes)).index('320851'))
#print('Part1', ''.join(str(recipe) for recipe in recipes[input:input+10]))

def part2(data):
    data = [int(x) for x in str(data)]
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    while True:
        recipe_sum = recipes[elf1] + recipes[elf2]

        new_recipes = map(int, str(recipe_sum))
        for nr in new_recipes:
            recipes.append(nr)
            if recipes[-len(data) :] == data:
                return len(recipes) - len(data)

        elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)


print(part2(320851))
