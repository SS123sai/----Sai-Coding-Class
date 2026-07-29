students = [
    {"name": "Ryan", "elective": "Art"},
    {"name": "Chloe", "elective": "Robotics"},
    {"name": "Marcus", "elective": "Art"},
    {"name": "Siddharth", "elective": "Drama"},
    {"name": "Hannah", "elective": "Robotics"},
    {"name": "Devin", "elective": "Art"}
]
by_elective= {}
for i in students:
    name= i["name"]
    elective= i["elective"]
    if elective in by_elective:
        by_elective[elective].append(name)
    else:
        by_elective[elective]=[name]
print(by_elective)