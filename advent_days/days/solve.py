from . import day_1, day_2, day_3, day_4, day_5, day_6, day_7, day_8,day_9, day_10, day_11, day_12, day_13, day_14, day_15

functions = {
    1: day_1,
    2: day_2,
    3: day_3,
    4: day_4,
    5: day_5,
    6: day_6,
    7: day_7,
    8: day_8,
    9: day_9,
    10: day_10,
    11: day_11,
    12: day_12,
    13: day_13,
    14: day_14,
    15: day_15,
}

# Dynamic import of day modules
day_modules = {
    f"day_{i}": __import__(f"advent_days.days.day_{i}", fromlist=["solve"])
    for i in range(1, 16)
}

def solve(day, input_data=None):
    day_module = day_modules.get(f"day_{day}") 
    if day_module:
        print(day_module.solve(input_data))
        return(day_module.solve(input_data))
    else:
        return TypeError