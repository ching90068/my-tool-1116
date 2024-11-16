# import random
# food=["麥當勞","肯德基","三商巧福"]
# result=random.choices(food)
# print(result)

import random
food=[lunch()]
def lunch():
    with open("lunch.txt","r",encoding="utf-8") as file:
        for line in file:
            print(line.strip())

result=random.choice(food)
print(result)

