def max_rebars_in_meter():
    return max(REBAR_STEPS_MAPPER.values())


def calculate_rebars_per_meter(rebars_per_meter):
    for step, count in REBAR_STEPS_MAPPER.items():
        if rebars_per_meter <= count:
            return step, count
    return None, None


def calculate_rebars_per_meter_and_min_reinforcement(rebar_area, rebars_per_meter, min_reinforcement,
                                                     custom_steps=None):
    for step, count in REBAR_STEPS_MAPPER.items():
        if custom_steps:
            if step in custom_steps and rebars_per_meter <= count and count * rebar_area >= min_reinforcement:
                return step, count
        else:
            if rebars_per_meter <= count and count * rebar_area >= min_reinforcement:
                return step, count
    return None, None


REBAR_STEPS_MAPPER = {20: 5,
                      15: 6.666666666666667,
                      12.5: 8,
                      10: 10}
