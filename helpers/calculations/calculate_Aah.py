from helpers.rebars_db import REBARS_CM2, REBAR_WEIGHT, REBARS_DIAMETER


def calculate_AaH(required_reinforcement):
    steps = [20, 15, 12.5, 10]
    rebars_per_meter = [round(100 / x, 2) for x in steps]
    min_weight = 10000000
    index_of_min_rebar = 0
    index_of_min_step = 0
    for rebar in REBARS_CM2:
        needed_rebars_per_meter = required_reinforcement / rebar
        index = REBARS_CM2.index(rebar)
        current_rebar_weight = REBAR_WEIGHT[index]
        for i in range(len(rebars_per_meter)):
            if needed_rebars_per_meter > rebars_per_meter[i]:
                continue
            else:
                weight_of_current_mesh = rebars_per_meter[i] * current_rebar_weight
            if 0 < weight_of_current_mesh <= min_weight:
                min_weight = weight_of_current_mesh
                index_of_min_rebar = index
                index_of_min_step = i
    return rebars_per_meter[index_of_min_step], REBARS_DIAMETER[index_of_min_rebar], steps[index_of_min_step]
