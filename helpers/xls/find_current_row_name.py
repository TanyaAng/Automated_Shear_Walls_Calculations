def current_row_name(row):
    current_row_as_string = str(row)
    dot_index = current_row_as_string.index('.')
    compare_symbol_index = current_row_as_string.index('>')
    return current_row_as_string[dot_index + 1:compare_symbol_index]