from helpers.rebars.rebars_db import REBARS_MAPPER, rebar_area_cm2


def calculate_Aa1_Aa2(required_reinforcement, number_of_bars):
    required_rebar_cm2 = required_reinforcement / number_of_bars
    for key, value in REBARS_MAPPER.items():
        if required_rebar_cm2<=rebar_area_cm2(key):
            return key
    return "Change column size!!!"
