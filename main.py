import asyncio
from math import pi
from config import gears_max

import PySimpleGUI as sg
from functions import calc_engine_volume, screensize
from layouts import layout

sg.theme("Material1")

window = sg.Window('Cal Calculator', layout, icon="icon.ico", finalize=True,
                   location=(screensize[0] / 2, screensize[1] / 2))


def calc(rpm, tyre_size, f_drive, gear):
    return (3.6 * rpm * pi * float(tyre_size)) / float(30 * float(gear) * float(f_drive))


async def main_run():
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        # print(event, values) -> Uncomment for debuting

        if event == "_calculate_engines_":  # check whether the button is pressed

            bore = values["_bore_"]
            stroke = values["_stroke_"]
            cylinder = values["_cylinder_count_"]

            if bore and stroke and cylinder:  # check whether all fields are filled with data/ not checked what data yet
                if bore.isdigit() and stroke.isdigit() and cylinder.isdigit():
                    calc_engine_volume(bore, stroke, cylinder)
                else:
                    ...
            else:
                ...

        if event:
            checked = True
            for gear in range(1, gears_max + 1):
                if not values[f'_{gear}gear_']:
                    checked = False
                    break

            if checked and \
                    values['_final_drive_'] and \
                    values['_tyre_width_'] and \
                    values['_tyre_height_'] and \
                    values['_tyre_diam_'] and \
                    values['_rpm_'] and \
                    values['_final_drive_']:

                for gear in range(1, gears_max + 1):
                    tyre_real = (float(values['_tyre_width_']) * float(values['_tyre_height_'])) / 100

                    tyre_sshit = (float(float(values['_tyre_diam_']) * 12.7)) + tyre_real
                    tyre_size = tyre_sshit / 1000
                    window[f'_{gear}kmh_results_'].Update(
                        "%.2f" %
                        calc(
                            int(values['_rpm_']),
                            tyre_size,
                            float(values['_final_drive_']),
                            float(values[f'_{gear}gear_'])
                        )
                    )
                    window[f'_{gear}mph_results_'].Update(
                        "%.2f" %
                        (calc(
                            int(values['_rpm_']),
                            tyre_size,
                            float(values['_final_drive_']),
                            float(values[f'_{gear}gear_'])
                        ) // 1.6)
                    )
            else:
                continue

    window.close()


if __name__ == '__main__':
    asyncio.run(main_run())
