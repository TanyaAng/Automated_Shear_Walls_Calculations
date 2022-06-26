from helpers.rebars.rebars_db import rebars, rebar_area_cm2


def calculate_Aa1_Aa2(required_reinforcement, number_of_bars):
    required_rebar_cm2 = required_reinforcement / number_of_bars
    for diameter in rebars():
        if required_rebar_cm2 <= rebar_area_cm2(diameter):
            return diameter
    return "Change column size!!!"
