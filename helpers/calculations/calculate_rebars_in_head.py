from math import ceil

def calculate_rebars_in_head(height, width):
    number_rebars = 0
    if height == 10:
        number_rebars += 2
    elif height > 10:
        number_rebars += ceil((height - 5) / 15 + 1) * 2
    if width > 25:
        if width in [30, 35, 40, 45] and height == 10:
            number_rebars += 1
        elif width in [50, 60] and height == 10:
            number_rebars += 2
        elif width in [30, 35, 40, 45] and height > 10:
            number_rebars += 2
        else:
            number_rebars += ceil((width - 5) / 15 - 1) * 2
    return number_rebars

a=5