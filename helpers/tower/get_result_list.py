def result_list_of_flattened_dict(flattened_dict):
    result = []
    for key, value in flattened_dict.items():
        for num in value:
            result.append(num)
    return result

