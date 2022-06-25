from helpers.find_current_shear_wall_index import find_current_shear_wall_index
from helpers.find_required_index import find_required_index


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
                        sheet[current_row_as_string].value = None
                        sheet[find_required_index(current_row_as_string, 4)].value = None
                        sheet[find_required_index(current_row_as_string, 5)].value = None
                    elif cell_number == 2:
                        sheet[current_row_as_string].value = None
                        sheet[find_required_index(current_row_as_string, 4)].value = None
                        sheet[find_required_index(current_row_as_string, 5)].value = None
                        sheet[find_required_index(current_row_as_string, 6)].value = None
                    elif cell_number == 3:
                        sheet[current_row_as_string].value = None
                        sheet[find_required_index(current_row_as_string, 4)].value = None
                        sheet[find_required_index(current_row_as_string, 5)].value = None
                        sheet[find_required_index(current_row_as_string, 6)].value = None
                cell_number += 1
        row_index_for_head_size += 12

    workbook.save(file_path)