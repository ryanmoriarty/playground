import datetime
import person

me = person.Person(
    "Ryan",
    "Moriarty",
    datetime.date(1980, 4, 1), # year, month, day
    "8 Ossian Road",
    "07968199004",
    "ryan.moriarty@btinternet.com"
)

somone = person.Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)


print(me)
print(somone.name)
print(me.name)
print(me.age() - somone.age())
