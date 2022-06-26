def get_max_values_per_level(tower_results):
    max_reinf_per_level = {}
    for key, value in tower_results.items():
        max_sum = 0
        max_index = 0
        for i in range(0, len(value['Aa1'])):
            current_sum = value['Aa1'][i] + value['Aa2'][i] + value['Aav'][i]
            if current_sum >= max_sum:
                max_sum = current_sum
                max_index = i
        max_reinf_per_level[key] = {'Aa1': value['Aa1'][max_index], 'Aa2': value['Aa2'][max_index],
                                    'Aav': value['Aav'][max_index], 'Aah': max(value['Aah'])}
    return max_reinf_per_level

a=5