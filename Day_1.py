
# This code is part of the Advent of Code 2023 challenge.
# Day 1: Trebuchet Numbers

with open("Trebuchet_num.txt", "r") as file:
    lines = file.readlines()

written_num_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
symb_num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
written_num_list_dict = {key:value for key,value in zip(written_num_list, symb_num_list)}

# PART 2 //////////////////////////////////////////////////////////////////////////////////////////////////

# This loop will read written numbers too and count them in the calibration codes:


# List will be formatted as [(symb_num1, index1),(symb_num2, index2),...]
# First number is for the symbolic number present, second number is for the index of the symbolic number in the code
symb_index_list = []
calibration_code_list = []

# # This loop inspects each code in the file
# for code in lines:
#     symb_index_list = []
#     # This loop goes through each written number
#     for written_num in written_num_list:
#         # Write code that identifies written/symb numbers in the order they appear in the code
#         if written_num in code:

#             # Intializes a list to hold the spliced code
#             spliced_code_list = [code]
#             while spliced_code_list[-1].count(written_num) > 0:
#                 # Stores the written number found in the code/spliced code
#                 symb_num = written_num_list_dict[written_num]

#                 # Finds the index of the written number in the original code by correcting for the length of what has been spliced off
#                 # spliced_code_list[-1].index(written_num) ~ gets index of written number in the most recent spliced code
#                 # (len(spliced_code_list[0]) - len(spliced_code_list[-1])) ~ length of whatever has been spliced off from most recent in splice list
#                 symb_num_index = spliced_code_list[-1].index(written_num) + (len(spliced_code_list[0]) - len(spliced_code_list[-1]))

#                 # Creates a tuple of the symbolic number and its index in the code
#                 symb_index_pair = (symb_num, symb_num_index)
#                 symb_index_list.append(symb_index_pair)

#                 # Splices the code at the index of the END of the written number found in the most recently spliced code
#                 splice_position = spliced_code_list[-1].index(written_num) + len(written_num)
#                 spliced_code = (spliced_code_list[-1])[splice_position:]
#                 spliced_code_list.append(spliced_code)


#     for symb_num in symb_num_list:
#         # Write code that identifies written/symb numbers in the order they appear in the code
#         if symb_num in code:

#             # Intializes a list to hold the spliced code
#             spliced_code_list = [code]
#             while spliced_code_list[-1].count(symb_num) > 0:
#                 # Stores the written number found in the code/spliced code

#                 # Finds the index of the written number in the original code by correcting for the length of what has been spliced off
#                 # spliced_code_list[-1].index(written_num) ~ gets index of written number in the most recent spliced code
#                 # (len(spliced_code_list[0]) - len(spliced_code_list[-1])) ~ length of whatever has been spliced off from most recent in splice list
#                 symb_num_index = spliced_code_list[-1].index(symb_num) + (len(spliced_code_list[0]) - len(spliced_code_list[-1]))

#                 # Creates a tuple of the symbolic number and its index in the code
#                 symb_index_pair = (symb_num, symb_num_index)
#                 symb_index_list.append(symb_index_pair)

#                 # Splices the code at the index of the END of the written number found in the most recently spliced code
#                 splice_position = spliced_code_list[-1].index(symb_num) + len(symb_num)
#                 spliced_code = (spliced_code_list[-1])[splice_position:]
#                 spliced_code_list.append(spliced_code)

#     # Sorts the list of symbolic numbers in ascending index order
#     symb_index_list.sort(key=lambda x: x[1])
#     calibration_code = int(symb_index_list[0][0] + symb_index_list[-1][0])
#     calibration_code_list.append(calibration_code)

# # print(calibration_code_list)
# print("Answer:" + str(sum(calibration_code_list)))

# PART 1 ////////////////////////////////////////////////////////////////////////////////////////////////

# If we are discounting the written numbers, we can simplify the code by only looking for symbolic numbers:

# This loop inspects each code in the file
for code in lines:
    symb_index_list = []
    # This loop goes through each written number

    for symb_num in symb_num_list:
        # Write code that identifies written/symb numbers in the order they appear in the code
        if symb_num in code:

            # Intializes a list to hold the spliced code
            spliced_code_list = [code]
            while spliced_code_list[-1].count(symb_num) > 0:
                # Stores the written number found in the code/spliced code

                # Finds the index of the written number in the original code by correcting for the length of what has been spliced off
                # spliced_code_list[-1].index(written_num) ~ gets index of written number in the most recent spliced code
                # (len(spliced_code_list[0]) - len(spliced_code_list[-1])) ~ length of whatever has been spliced off from most recent in splice list
                symb_num_index = spliced_code_list[-1].index(symb_num) + (len(spliced_code_list[0]) - len(spliced_code_list[-1]))

                # Creates a tuple of the symbolic number and its index in the code
                symb_index_pair = (symb_num, symb_num_index)
                symb_index_list.append(symb_index_pair)

                # Splices the code at the index of the END of the written number found in the most recently spliced code
                splice_position = spliced_code_list[-1].index(symb_num) + len(symb_num)
                spliced_code = (spliced_code_list[-1])[splice_position:]
                spliced_code_list.append(spliced_code)

    # Sorts the list of symbolic numbers in ascending index order
    symb_index_list.sort(key=lambda x: x[1])
    calibration_code = int(symb_index_list[0][0] + symb_index_list[-1][0])
    calibration_code_list.append(calibration_code)

# print(calibration_code_list)
print("Answer:" + str(sum(calibration_code_list)))


