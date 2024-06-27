import json
import numpy as np


def get_characteristics_of_parallelipiped(dict_abc: dict) -> tuple[float]:
    a, b, c = map(float, [dict_abc['a'], dict_abc['b'], dict_abc['c']])
    diag = np.sqrt(a**2 + b**2 + c**2)
    volume = a * b * c
    surface_area = 2 * (a*b + b*c + c*a)
    alpha = np.rad2deg(np.arccos(a / diag))
    beta = np.rad2deg(np.arccos(b / diag))
    gamma = np.rad2deg(np.arccos(c / diag))
    radius_described_sphere = 0.5 * diag
    volume_described_sphere = 4/3 * np.pi * radius_described_sphere**3
    result = {
        'diag': diag,
        'volume': volume,
        'surface_area': surface_area,
        'alpha': alpha,
        'beta': beta,
        'gamma': gamma,
        'radius_described_sphere': radius_described_sphere,
        'volume_described_sphere': volume_described_sphere
             }
    return result


def main():
    f = open('parallelepipeds.json')
    data = json.load(f)

    average_values = dict()

    result_dict = dict()
    for k, v in data.items():
        params = get_characteristics_of_parallelipiped(v)

        for param_name, param_val in params.items():
            avg_name = 'avg_' + param_name
            if avg_name not in average_values:
                average_values[avg_name] = param_val
            else:
                average_values[avg_name] += param_val
            params[param_name] = str(param_val)

        result_dict[k] = params

    n = len(average_values)
    for k, v in average_values.items():
        average_values[k] = v / n

    with open("characteristics.json", "w") as outfile:
        json.dump(result_dict, outfile, indent=2)

    with open("statistics.json", "w") as outfile:
        json.dump(average_values, outfile, indent=2)


if __name__ == "__main__":
    main()
