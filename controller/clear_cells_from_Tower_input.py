from helpers.xls.find_current_row_name import current_row_name
from helpers.xls.find_current_shear_wall_index import find_current_shear_wall_index
from helpers.xls.find_required_index import find_required_index


def clear_cell(count_shear_walls, levels, sheet):
    row_index_for_head_size = 7
    for current_shear_wall in range(count_shear_walls):
        column_index_for_head_size = 6
        index_for_Aa1, index_for_Aah = find_current_shear_wall_index(current_shear_wall)
        for level in range(levels):
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
                current_row_as_string = current_row_name(row)
                for _ in row:
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
