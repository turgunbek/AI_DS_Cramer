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


def generate_html(data_dict):
    html_content = f"""
    <!doctype html>
    <html lang="en">
    <style>
        table {{
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
            }}

        td, th {{
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
            }}

        tr:nth-child(even) {{
            background-color: #dddddd;
            }}
    </style>

    <body>
    <h1>Data Summary</h1>

        <h2>Обработали полученные фигуры и подвели статистику</h2>

            <table style="width:25%">
                <tr>
                    <th>Parameter</th>
                    <th>Value</th>
                </tr>

                <tr>
                    <td>Average Diagonal</td>
                    <td>{data_dict['avg_diag']}</td>
                <tr>
                <tr>
                    <td>Average Volume</td>
                    <td>{data_dict['avg_volume']}</td>
                <tr>
                <tr>
                    <td>Average Surface Area</td>
                    <td>{data_dict['avg_surface_area']}</td>
                <tr>
                <tr>
                    <td>Average Alpha</td>
                    <td>{data_dict['avg_alpha']}</td>
                <tr>
                <tr>
                    <td>Average Beta</td>
                    <td>{data_dict['avg_beta']}</td>
                <tr>
                <tr>
                    <td>Average Gamma</td>
                    <td>{data_dict['avg_gamma']}</td>
                <tr>
                <tr>
                    <td>Average Radius of Described Sphere</td>
                    <td>{data_dict['avg_radius_described_sphere']}</td>
                <tr>
                <tr>
                    <td>Average Volume of Described Sphere</td>
                    <td>{data_dict['avg_volume_described_sphere']}</td>
                <tr>
            </table>
    </body>
    </html>
    """

    with open("data_summary.html", "w") as file:
        file.write(html_content)


def main():
    pict = """
    MY FIRST SKRIPT

        /------/
       /      /|
      /      / |
     /------/  |
    |      |  /
    |      | /
    |______|/

    I LOVE PYTHON
    """
    print(pict)

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

    n = len(result_dict)
    for k, v in average_values.items():
        average_values[k] = v / n

    print(f'Total number of figures = {len(result_dict)}')

    with open("characteristics.json", "w") as outfile:
        json.dump(result_dict, outfile, indent=2)

    with open("statistics.json", "w") as outfile:
        json.dump(average_values, outfile, indent=2)

    generate_html(average_values)


if __name__ == "__main__":
    main()
