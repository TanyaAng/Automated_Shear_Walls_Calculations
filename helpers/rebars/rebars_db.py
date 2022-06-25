def rebars():
    return REBARS_MAPPER.keys()


def rebar_area_cm2(rebar):
    return REBARS_MAPPER[rebar]['Area']


def rebar_weight_kg(rebar):
    return REBARS_MAPPER[rebar]['Weight']


REBARS_MAPPER = {
    8: {'Area': 0.503, 'Weight': 0.395},
    10: {'Area': 0.785, 'Weight': 0.617},
    12: {'Area': 1.131, 'Weight': 0.888},
    14: {'Area': 1.539, 'Weight': 1.208},
    16: {'Area': 2.011, 'Weight': 1.998},
    18: {'Area': 2.545, 'Weight': 2.466},
    20: {'Area': 3.142, 'Weight': 2.984},
    22: {'Area': 3.801, 'Weight': 3.853},
    25: {'Area': 4.909, 'Weight': 4.834},
    28: {'Area': 6.158, 'Weight': 6.313},
    32: {'Area': 8.042, 'Weight': 7.990}
}


