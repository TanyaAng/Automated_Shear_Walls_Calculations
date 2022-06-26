import re

def read_from_txt_file(data):
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
    return Tower_results

a=5