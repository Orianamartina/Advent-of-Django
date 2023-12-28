from lib.input_handlers import read_lines
from lib.answer_display import print_answer

file_contents = read_lines("day11/11input.txt")


def parse_monkeys():

    current = 0
    monkeys = [{} for _ in range(8)]

    for line in file_contents:
        monkeys[current]["times_inspected"] = 0

        if "Monkey" in line:
            monkeys[current]["id"] = line.split()[1][0]
        elif "Starting" in line:
            monkeys[current]["items"] = []
            for item in line.split()[2:]:
                monkeys[current]["items"].append(int(item[0:2]))
            monkeys[current]["thrown_items"] = monkeys[current]["items"]
        elif "Operation" in line:
            operation = line.split()[3:]
            monkeys[current]["operation"] = operation
        elif "Test" in line:
            divisible_by = line.split()[-1]
            monkeys[current]["divisible"] = divisible_by
        elif "true" in line:
            throw_to = line.split()[-1]
            monkeys[current]["throw_true"] = throw_to
        elif "false" in line:
            throw_to = line.split()[-1]
            monkeys[current]["throw_false"] = throw_to
            current += 1

    return monkeys


def get_most_active_monkeys(monkeys, positions):
    most_active_monkeys = [0 for _ in range(positions)]
    for monkey in monkeys:

        for i in range(positions):
            if monkey["times_inspected"] > most_active_monkeys[i]:
                most_active_monkeys.insert(i, monkey["times_inspected"])
                most_active_monkeys = most_active_monkeys[:2]
                break
    return (most_active_monkeys[0] * most_active_monkeys[1])


def monkey_business(monkeys, iteration, operation):
    for _ in range(iteration):
        for monkey in monkeys:

            monkey["items"] = monkey["thrown_items"]
            monkey["thrown_items"] = []
            for item in monkey["items"]:
                worry_level = item

                second_number = item if monkey["operation"][2] == "old" else int(
                    monkey["operation"][2])

                worry_level = item * \
                    second_number if monkey["operation"][1] == "*" else item + \
                    second_number

                worry_level = operation(worry_level)

                if worry_level % int(monkey["divisible"]) == 0:
                    monkey_to_throw_to = int(monkey["throw_true"])

                else:
                    monkey_to_throw_to = int(monkey["throw_false"])

                monkeys[monkey_to_throw_to]["thrown_items"].append(
                    worry_level)
                monkey["times_inspected"] += 1

    return get_most_active_monkeys(monkeys, 2)


def monkey_business_with_module(monkeys):
    modulo = 1
    for monkey in monkeys:
        modulo = modulo * int(monkey["divisible"])

    return monkey_business(monkeys, 10000, lambda x: x % modulo)


print_answer("11.1", monkey_business(parse_monkeys(), 20, operation=lambda x: x // 3))
print_answer("11.2", monkey_business_with_module(parse_monkeys()))
