from adventapi.days.lib.input_handlers import read_file

file_contents = read_file("adventapi/days/day_6_input.txt")

def solve(input = file_contents):

    def find_packet_in_signal(length_of_packet, data_stream):
        if len(data_stream) >= length_of_packet:
            for i in range(length_of_packet, len(data_stream) + 1):
                comparable_characters = data_stream[(i - length_of_packet) : i]

                if len(set(comparable_characters)) == length_of_packet:
                    return data_stream


    def process_signal(signal, length_of_packet):
        data_stream = ""

        for character in signal:
            data_stream += character
            found_marker = find_packet_in_signal(length_of_packet, data_stream)
            if found_marker:
                return len(found_marker)


    part1 = process_signal(input, 4)
    part2 = process_signal(input, 14)

    return {1:part1, 2:part2}