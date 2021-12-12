import openpyxl
from math import ceil
import json
from tkinter import messagebox



# This function works only for row index with two leters (example:HJ...)
def find_required_index(starting_row, step):
    row_alpha = []
    row_digit = []
    for index in starting_row:
        if index.isalpha():
            row_alpha.append(index)
        elif index.isdigit():
            row_digit.append(index)
    row_alpha = list(reversed(row_alpha))
    next_row_alpha = []
    is_previous_bigger_than_Z = False
    is_appended_next_symbol = False
    for index in range(len(row_alpha)):
        if len(row_alpha) == 1:
            if ord(row_alpha[index]) < 90 - step:
                next_row_alpha.append(chr(ord(row_alpha[index]) + step))
            else:
                next_char_ASCII_index = 65 + (step - 1) - (90 - ord(row_alpha[index]))
                next_row_alpha.append(chr(next_char_ASCII_index))
                next_row_alpha.append('A')

        elif len(row_alpha) > 1:
            if is_appended_next_symbol:
                next_row_alpha.append(row_alpha[index])
                continue
            if is_previous_bigger_than_Z:
                if ord(row_alpha[index]) + 1 > 90 and index == len(row_alpha) - 1:
                    if row_alpha[index] == 'Z':
                        next_row_alpha.append('A')
                        next_row_alpha.append('A')
                        break
                    else:
                        next_char_ASCII_index = 65 + (step - 1) - (90 - ord(row_alpha[index]))
                        next_row_alpha.append(chr(next_char_ASCII_index))
                        next_row_alpha.append('A')
                        break
                else:
                    next_row_alpha.append(chr(ord(row_alpha[index]) + 1))
                    is_appended_next_symbol = True
                    continue
            if ord(row_alpha[index]) > 90 - step:
                next_char_ASCII_index = 65 + (step - 1) - (90 - ord(row_alpha[index]))
                next_row_alpha.append(chr(next_char_ASCII_index))
                is_previous_bigger_than_Z = True
                continue
            else:
                next_row_alpha.append(chr(ord(row_alpha[index]) + step))
                is_appended_next_symbol = True
    return ''.join(list(reversed(next_row_alpha)) + row_digit)


def find_current_shear_wall_index(number_of_shear_wall):
    next_starting_column = 'H8'
    next_ending_column = 'H11'
    if number_of_shear_wall >= 1:
        list_alpha = []
        list_digit = []
        for symbol in next_starting_column:
            if symbol.isdigit():
                list_digit.append(symbol)
            elif symbol.isalpha():
                list_alpha.append(symbol)
        string_of_digits = [str(el) for el in list_digit]
        int_of_digits = int(''.join(string_of_digits))
        next_starting_column = str(int_of_digits + 12 * (number_of_shear_wall))
        string_of_alpha = ''.join(list_alpha)
        next_starting_column = string_of_alpha + next_starting_column
        list_alpha = []
        list_digit = []
        for symbol in next_ending_column:
            if symbol.isdigit():
                list_digit.append(symbol)
            elif symbol.isalpha():
                list_alpha.append(symbol)
        string_of_digits = [str(el) for el in list_digit]
        int_of_digits = int(''.join(string_of_digits))
        next_ending_column = str(int_of_digits + 12 * (number_of_shear_wall))
        string_of_alpha = ''.join(list_alpha)
        next_ending_column = string_of_alpha + next_ending_column

    return next_starting_column, next_ending_column


def clear_cell(count_shear_walls, levels, file_path, sheet, workbook):
    number_of_shear_walls = count_shear_walls
    building_levels = levels
    row_index_for_head_size = 7
    for current_shear_wall in range(number_of_shear_walls):
        column_index_for_head_size = 6
        starting_index_for_current_wall = find_current_shear_wall_index(current_shear_wall)
        index_for_Aa1 = starting_index_for_current_wall[0]
        index_for_Aah = starting_index_for_current_wall[1]
        for level in range(building_levels):
            column_index_for_head_size += 10
            if level == 0:
                step = 0
            else:
                step = 10
            start_row_index = find_required_index(index_for_Aa1, step)
            end_row_index = find_required_index(index_for_Aah, step)
            index_for_Aa1 = start_row_index
            index_for_Aah = end_row_index
            cell_number = 0
            for row in sheet[start_row_index: end_row_index]:
                current_row_as_string = str(row)
                dot_index = current_row_as_string.index('.')
                compare_symbol_index = current_row_as_string.index('>')
                current_row_as_string = current_row_as_string[dot_index + 1:compare_symbol_index]
                for cell in row:
                    if cell_number == 0 or cell_number == 1:
                        sheet[find_required_index(current_row_as_string, 4)].value = None
                        sheet[find_required_index(current_row_as_string, 5)].value = None
                    elif cell_number == 2:
                        sheet[find_required_index(current_row_as_string, 4)].value = None
                        sheet[find_required_index(current_row_as_string, 5)].value = None
                        sheet[find_required_index(current_row_as_string, 6)].value = None
                    elif cell_number == 3:
                        sheet[find_required_index(current_row_as_string, 4)].value = None
                        sheet[find_required_index(current_row_as_string, 5)].value = None
                        sheet[find_required_index(current_row_as_string, 6)].value = None
                cell_number += 1
        row_index_for_head_size += 12

    workbook.save(file_path)

# if __name__ == '__main__':
def main_function_clear():
    with open('database.txt', 'r') as file:
        try:
            user_input = json.load(file)
            file_path = user_input[0]
            sheet_name = user_input[1]
            number_shear_walls = int(user_input[2])
            storey_levels = int(user_input[3])
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook[sheet_name]
            clear_cell(number_shear_walls, storey_levels, file_path, sheet, workbook)
            print (user_input)
            messagebox.showinfo("Info", "Successful")
        except:
            messagebox.showwarning("Warning", "Invalid Input")