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