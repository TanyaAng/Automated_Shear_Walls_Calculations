def calculate_AaV(required_reinforcement, head_width):
    wall_width = head_width
    min_percent_vertical_reinfocement = 0.002
    min_reinforcement = min_percent_vertical_reinfocement * 100 * wall_width / 2
    steps = [20, 15]
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
            if 0 < weight_of_current_mesh <= min_weight and rebar * rebars_per_meter[i] > min_reinforcement:
                min_weight = weight_of_current_mesh
                index_of_min_rebar = index
                index_of_min_step = i
    return rebars_per_meter[index_of_min_step], REBARS_DIAMETER[index_of_min_rebar], steps[index_of_min_step]