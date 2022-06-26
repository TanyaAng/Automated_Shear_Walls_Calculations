from helpers.tower.flatten_values import flatten_values_and_reverse_levels_per_wall
from helpers.tower.get_result_list import result_list_of_flattened_dict
from helpers.tower.max_values_per_level import get_max_values_per_level
from helpers.tower.read_from_txt_file import read_from_txt_file


def get_Tower_results_from_txt(data):
    Tower_results = read_from_txt_file(data)
    max_reinf_per_level = get_max_values_per_level(Tower_results)
    flattened_dict = flatten_values_and_reverse_levels_per_wall(max_reinf_per_level)
    result_list = result_list_of_flattened_dict(flattened_dict)
    return result_list
