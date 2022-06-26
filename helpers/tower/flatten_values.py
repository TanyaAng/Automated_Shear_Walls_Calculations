def flatten_values_and_reverse_levels_per_wall(dictionary_result):
    flatten_dict = {}
    for key, value in dictionary_result.items():
        key_splitted = key.split("-")
        new_key = key_splitted[0]
        if new_key not in flatten_dict:
            flatten_dict[new_key] = [value['Aah']]
        else:
            flatten_dict[new_key].append(value['Aah'])
        flatten_dict[new_key].append(value['Aav'])
        flatten_dict[new_key].append(value['Aa2'])
        flatten_dict[new_key].append(value['Aa1'])
    max_lenght = 0
    for value in flatten_dict.values():
        value.reverse()
        length = len(value)
        if length > max_lenght:
            max_lenght = length

    for value in flatten_dict.values():
        if len(value) < max_lenght:
            count_to_fill = max_lenght - len(value)
            for i in range(count_to_fill):
                value.append(None)

    return flatten_dict

a=5