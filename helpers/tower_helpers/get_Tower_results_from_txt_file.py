import re
def get_Tower_results_from_txt(data):
    Tower_results = {}
    for line in data:
        pattern_shear_walls = r"Ш\d+-\d+"
        is_there_match = re.match(pattern_shear_walls, line)
        if is_there_match:
            shear_walls = re.findall(pattern_shear_walls, line)
            match_shear_walls = ''.join(shear_walls)
            if match_shear_walls not in Tower_results:
                Tower_results[match_shear_walls] = {'Aa1': [], 'Aa2': [], 'Aav': [], 'Aah': []}
                continue
        pattern_Aa1 = r"(?<=Aa1\s=\s)\d+\.\d+(?=\s+cm²)"
        pattern_Aa2 = r"(?<=Aa2\s=\s)\d+\.\d+(?=\s+cm²)"
        pattern_Aav = r"(?<=Aav\s=\s±)\d+\.\d+(?=\s+cm²)"
        pattern_Aah = r"(?<=Aah\s=\s±)\d+\.\d+(?=\s+cm²)"
        quantity_Aa1 = re.findall(pattern_Aa1, line)
        quantity_Aa2 = re.findall(pattern_Aa2, line)
        quantity_Aav = re.findall(pattern_Aav, line)
        quantity_Aah = re.findall(pattern_Aah, line)
        if not quantity_Aa1 == []:
            Tower_results[match_shear_walls]['Aa1'].append(float(''.join(quantity_Aa1)))
        if not quantity_Aa2 == []:
            Tower_results[match_shear_walls]['Aa2'].append(float(''.join(quantity_Aa2)))
        if not quantity_Aav == []:
            Tower_results[match_shear_walls]['Aav'].append(float(''.join(quantity_Aav)))
        if not quantity_Aah == []:
            Tower_results[match_shear_walls]['Aah'].append(float(''.join(quantity_Aah)))
    max_reinf_for_level = {}

    for key, value in Tower_results.items():
        max_sum = 0
        max_index = 0
        for i in range(0, len(value['Aa1'])):
            current_sum = value['Aa1'][i] + value['Aa2'][i] + value['Aav'][i]
            if current_sum >= max_sum:
                max_sum = current_sum
                max_index = i
        max_reinf_for_level[key] = {'Aa1': value['Aa1'][max_index], 'Aa2': value['Aa2'][max_index],
                                    'Aav': value['Aav'][max_index], 'Aah': max(value['Aah'])}

    result_dict = {}
    for key, value in max_reinf_for_level.items():
        key_splitted = key.split("-")
        new_key = key_splitted[0]
        if new_key not in result_dict:
            result_dict[new_key] = [value['Aah']]
        else:
            result_dict[new_key].append(value['Aah'])
        result_dict[new_key].append(value['Aav'])
        result_dict[new_key].append(value['Aa2'])
        result_dict[new_key].append(value['Aa1'])

    max_lenght = 0
    for value in result_dict.values():
        value.reverse()
        length = len(value)
        if length > max_lenght:
            max_lenght = length

    for value in result_dict.values():
        if len(value) < max_lenght:
            count_to_fill = max_lenght - len(value)
            for i in range(count_to_fill):
                value.append(None)
    print (f"Result dict: {result_dict}")
    result_list = []
    for key, value in result_dict.items():
        for num in value:
            result_list.append(num)

    return result_list