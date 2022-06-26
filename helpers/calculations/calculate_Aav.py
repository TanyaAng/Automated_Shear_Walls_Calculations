from helpers.rebars.rebars_per_meter import calculate_rebars_per_meter_and_min_reinforcement, \
    max_rebars_in_meter
from helpers.rebars.rebars_db import rebars, rebar_area_cm2, rebar_weight_kg

from sys import maxsize


def calculate_AaV(reinforcement, wall_width):
    STEPS_FOR_AaV = [20, 15]
    min_weight = maxsize
    min_diameter = 0
    min_rebar_per_meter = 0
    min_step = 0
    min_reinforcement = 0.002 * 100 * wall_width / 2

    for diameter in rebars():
        current_rebar_area = rebar_area_cm2(diameter)
        required_rebars_per_meter = reinforcement / current_rebar_area
        if required_rebars_per_meter > max_rebars_in_meter():
            continue
        current_rebar_weight = rebar_weight_kg(diameter)
        current_step, current_count = calculate_rebars_per_meter_and_min_reinforcement(current_rebar_area,
                                                                                       required_rebars_per_meter,
                                                                                       min_reinforcement,
                                                                                       custom_steps=STEPS_FOR_AaV)
        if current_step != None and current_count != None:
            current_weight = current_rebar_weight * current_count
            if current_weight <= min_weight:
                min_weight = current_weight
                min_diameter = diameter
                min_rebar_per_meter = current_count
                min_step = current_step
    return min_rebar_per_meter, min_diameter, min_step


