from helpers.rebars_db import REBARS_CM2, REBARS_DIAMETER


def calculate_Aa1_Aa2(required_reinforcement, number_of_bars):
    required_diameter = required_reinforcement / number_of_bars
    provided_diameter=0
    for index in range(len(REBARS_CM2)):
        if required_diameter <= 1.539:
            provided_diameter = 14
        else:
            if required_diameter <= REBARS_CM2[index]:
                provided_diameter = REBARS_DIAMETER[index]
                break
            else:
                provided_diameter = 'Change column size!!!'
    return provided_diameter
