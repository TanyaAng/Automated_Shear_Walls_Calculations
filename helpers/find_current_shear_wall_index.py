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