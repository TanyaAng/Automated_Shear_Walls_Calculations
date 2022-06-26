from helpers.calculations.calculate_Aa1_Aa2 import calculate_Aa1_Aa2
from helpers.calculations.calculate_Aah import calculate_AaH
from helpers.calculations.calculate_Aav import calculate_AaV
from helpers.calculations.calculate_rebars_in_head import calculate_rebars_in_head
from helpers.xls.find_current_shear_wall_index import find_current_shear_wall_index
from helpers.xls.find_hear_size import find_head_size
from helpers.xls.find_required_index import find_required_index


def calculate_shear_walls(count_shear_walls, levels, sheet):
    row_index_for_head_size = 7
    for current_shear_wall in range(count_shear_walls):
        column_index_for_head_size = 6
        starting_index_for_current_wall = find_current_shear_wall_index(current_shear_wall)
        index_for_Aa1 = starting_index_for_current_wall[0]
        index_for_Aah = starting_index_for_current_wall[1]
        print(f"<<< SHEAR WALL {current_shear_wall + 1} >>>")
        for level in range(levels):
            print(f'Level:{level + 1}')
            # find choosen from engineer head size for each level and calculate number of rebars in it
            head_height, head_width = find_head_size(row_index_for_head_size, column_index_for_head_size, sheet)
            head_rebars = calculate_rebars_in_head(head_height, head_width)
            print(f"{head_rebars} number of rebars in head {head_height}, {head_width}")
            column_index_for_head_size += 10
            if level == 0:
                step = 0
            else:
                step = 10
            start_row_index = find_required_index(index_for_Aa1, step)
            end_row_index = find_required_index(index_for_Aah, step)
            # searching for new values of required reinforcement starts from the last found indices
            index_for_Aa1 = start_row_index
            index_for_Aah = end_row_index
            # read excel cell with required reinforcement for each level
            cell_number = 0
            for row in sheet[start_row_index: end_row_index]:
                current_row_as_string = str(row)
                dot_index = current_row_as_string.index('.')
                compare_symbol_index = current_row_as_string.index('>')
                current_row_as_string = current_row_as_string[dot_index + 1:compare_symbol_index]
                for cell in row:
                    # if cell.value == None:
                    #     cell.value = 0
                    if cell.value != None:
                        if cell_number == 0 or cell_number == 1:
                            result = calculate_Aa1_Aa2(cell.value, head_rebars)
                            print(f"{head_rebars}N{result}")
                            sheet[find_required_index(current_row_as_string, 4)].value = head_rebars
                            sheet[find_required_index(current_row_as_string, 5)].value = result
                        elif cell_number == 2:
                            result = calculate_AaV(cell.value, head_width)
                            print(f"{result[0]} -> N{result[1]}/{result[2]}")
                            sheet[find_required_index(current_row_as_string, 4)].value = result[0]
                            sheet[find_required_index(current_row_as_string, 5)].value = result[1]
                            sheet[find_required_index(current_row_as_string, 6)].value = '/' + str(result[2])
                        elif cell_number == 3:
                            result = calculate_AaH(cell.value)
                            print(f"{result[0]} -> N{result[1]}/{result[2]}")
                            sheet[find_required_index(current_row_as_string, 4)].value = result[0]
                            sheet[find_required_index(current_row_as_string, 5)].value = result[1]
                            sheet[find_required_index(current_row_as_string, 6)].value = '/' + str(result[2])
                cell_number += 1
        row_index_for_head_size += 12


a=5
