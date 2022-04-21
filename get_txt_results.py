from shear_walls_automation import find_current_shear_wall_index
from shear_walls_automation import find_required_index
import re
import openpyxl
import json
from tkinter import messagebox


def get_Tower_results_from_txt(data):
    Tower_results = {}
    for line in data:
        pattern_shear_walls = r"Ш\d+-\d+"
        is_there_match = re.match(pattern_shear_walls, line)
        if is_there_match:
            shear_walls = re.findall(pattern_shear_walls, line)
            match_shear_walls = ''.join(shear_walls)
            if match_shear_walls not in Tower_results:
                Tower_results[match_shear_walls] = {'Aa1': [], 'Aa2': [], 'Aav': [], 'Aah': []}
                continue
        pattern_Aa1 = r"(?<=Aa1\s=\s)\d+\.\d+(?=\s+cm²)"
        pattern_Aa2 = r"(?<=Aa2\s=\s)\d+\.\d+(?=\s+cm²)"
        pattern_Aav = r"(?<=Aav\s=\s±)\d+\.\d+(?=\s+cm²)"
        pattern_Aah = r"(?<=Aah\s=\s±)\d+\.\d+(?=\s+cm²)"
        quantity_Aa1 = re.findall(pattern_Aa1, line)
        quantity_Aa2 = re.findall(pattern_Aa2, line)
        quantity_Aav = re.findall(pattern_Aav, line)
        quantity_Aah = re.findall(pattern_Aah, line)
        if not quantity_Aa1 == []:
            Tower_results[match_shear_walls]['Aa1'].append(float(''.join(quantity_Aa1)))
        if not quantity_Aa2 == []:
            Tower_results[match_shear_walls]['Aa2'].append(float(''.join(quantity_Aa2)))
        if not quantity_Aav == []:
            Tower_results[match_shear_walls]['Aav'].append(float(''.join(quantity_Aav)))
        if not quantity_Aah == []:
            Tower_results[match_shear_walls]['Aah'].append(float(''.join(quantity_Aah)))
    max_reinf_for_level = {}

    for key, value in Tower_results.items():
        max_sum = 0
        max_index = 0
        for i in range(0, len(value['Aa1'])):
            current_sum = value['Aa1'][i] + value['Aa2'][i] + value['Aav'][i]
            if current_sum >= max_sum:
                max_sum = current_sum
                max_index = i
        max_reinf_for_level[key] = {'Aa1': value['Aa1'][max_index], 'Aa2': value['Aa2'][max_index],
                                    'Aav': value['Aav'][max_index], 'Aah': max(value['Aah'])}

    result_dict = {}

    for key, value in max_reinf_for_level.items():
        key_splitted = key.split("-")
        new_key = key_splitted[0]
        if new_key not in result_dict:
            result_dict[new_key] = [value['Aah']]
        else:
            result_dict[new_key].append(value['Aah'])
        result_dict[new_key].append(value['Aav'])
        result_dict[new_key].append(value['Aa2'])
        result_dict[new_key].append(value['Aa1'])

    max_lenght = 0
    for value in result_dict.values():
        value.reverse()
        length = len(value)
        if length > max_lenght:
            max_lenght = length

    for value in result_dict.values():
        if len(value) < max_lenght:
            count_to_fill = max_lenght - len(value)
            for i in range(count_to_fill):
                value.append(None)
    print (f"Result dict: {result_dict}")
    result_list = []
    for key, value in result_dict.items():
        for num in value:
            result_list.append(num)
    return result_list


def paste_Tower_results_in_xls(count_shear_walls, levels, file_path, sheet, workbook, data):
    number_of_shear_walls = count_shear_walls
    building_levels = levels
    row_index_for_head_size = 7
    current_index_of_result_list = 0
    result_Tower = get_Tower_results_from_txt(data)
    print(f"result tower: {result_Tower}")
    for current_shear_wall in range(number_of_shear_walls):
        column_index_for_head_size = 6
        starting_index_for_current_wall = find_current_shear_wall_index(current_shear_wall)
        index_for_Aa1 = starting_index_for_current_wall[0]
        index_for_Aah = starting_index_for_current_wall[1]
        print(f"<<< SHEAR WALL {current_shear_wall + 1} >>>")
        for level in range(building_levels):
            print(f'Level:{level + 1}')
            column_index_for_head_size += 10
            if level == 0:
                step = 0
            else:
                step = 10
            start_row_index = find_required_index(index_for_Aa1, step)
            end_row_index = find_required_index(index_for_Aah, step)
            index_for_Aa1 = start_row_index
            index_for_Aah = end_row_index
            print(f"Start index: {start_row_index}, End index: {end_row_index}")
            cell_number = 0
            for row in sheet[start_row_index: end_row_index]:
                current_row_as_string = str(row)
                dot_index = current_row_as_string.index('.')
                compare_symbol_index = current_row_as_string.index('>')
                current_row_as_string = current_row_as_string[dot_index + 1:compare_symbol_index]
                for cell in row:
                    if cell_number == 0:
                        sheet[current_row_as_string].value = result_Tower[current_index_of_result_list]
                    elif cell_number == 1:
                        sheet[current_row_as_string].value = result_Tower[current_index_of_result_list + 1]
                    elif cell_number == 2:
                        sheet[current_row_as_string].value = result_Tower[current_index_of_result_list + 2]
                    elif cell_number == 3:
                        sheet[current_row_as_string].value = result_Tower[current_index_of_result_list + 3]
                cell_number += 1
            if current_index_of_result_list + 3 < len(result_Tower) - 1:
                current_index_of_result_list += 4
                print(current_index_of_result_list)
        row_index_for_head_size += 12
    workbook.save(file_path)


def main_function_get_results():
    with open('database.txt', 'r') as file:
        try:
            user_input = json.load(file)
            txt_path = user_input[0]
            file_path = user_input[1]
            sheet_name = user_input[2]
            number_shear_walls = int(user_input[3])
            storey_levels = int(user_input[4])
            print(user_input)
            data = open(txt_path, encoding='utf-8', mode='r')
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook[sheet_name]
            print(sheet)
            paste_Tower_results_in_xls(number_shear_walls, storey_levels, file_path, sheet, workbook, data)
            print(user_input)
            messagebox.showinfo("Info", "Successful")
        except:
            messagebox.showwarning("Warning", "Invalid input")
