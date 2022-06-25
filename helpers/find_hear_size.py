def find_head_size(row_indices, column_indices, sheet):
    column_size = []
    # for x_indices in range(row_indices, row_indices + 8):
    for y_indices in range(column_indices, column_indices + 10):
        if sheet.cell(row=row_indices, column=y_indices).value == 'глава - h/b':
            column_size.append(sheet.cell(row=row_indices, column=y_indices + 4).value)
            column_size.append(sheet.cell(row=row_indices, column=y_indices + 5).value)
            break
    return column_size