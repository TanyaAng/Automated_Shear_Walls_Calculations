from helpers.find_current_shear_wall_index import find_current_shear_wall_index
from helpers.find_required_index import find_required_index
from helpers.tower_helpers.get_Tower_results_from_txt_file import get_Tower_results_from_txt



def paste_Tower_results_in_xls(count_shear_walls, levels, sheet, data):
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
                for _ in row:
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
    # workbook.save(file_path)


