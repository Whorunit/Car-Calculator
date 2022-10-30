import PySimpleGUI as sg
from config import gears_max, gear_defaults

engine_volume_calc_layout = [
    [
        sg.Frame("",
                 layout=[
                     [sg.T("Bore: mm"), sg.Input(key="_bore_", justification="right", size=(10, 1))],
                     [sg.T("Stroke: mm"), sg.Input(key="_stroke_", justification="right", size=(10, 1))],
                     [sg.T("Cylinder: #"), sg.Input(key="_cylinder_count_", justification="right", size=(10, 1))],
                 ], element_justification="right"
                 )
    ],
    [
        sg.Col(
            layout=[
                [sg.B("Calculate", pad=(10, 10), key="_calculate_engines_")]
            ], element_justification="center", justification="center",
        )
    ]
]

gear_calc_layout = [
    [sg.Col([[sg.T("RPM: "),
              sg.Slider(range=(500, 10000), key="_rpm_", change_submits=True, default_value=500, orientation="h",
                        size=(30, 15), resolution=100)]], expand_x=True, expand_y=True)],
    [
        sg.Frame(
            "Gears ", layout=
            [
                *(
                    [
                        sg.T(f"{i}."),
                        sg.Input(key=f"_{i}gear_", default_text=gear_defaults[i - 1], justification="left",
                                 size=(10, 1)),
                        sg.T(key=f"_{i}kmh_results_", text_color="#FFFF20", font=("Tahoma, 11"),
                             background_color="#64778D", border_width=2, justification="right", size=(7, 1)),
                        sg.T(key=f"_{i}mph_results_", text_color="#FFFF20", font=("Tahoma, 11"),
                             background_color="#64778D", border_width=2, justification="right", size=(7, 1))
                    ] for i in range(1, gears_max + 1)),

            ], element_justification="right"
        ),
        sg.Frame("Tyres & Final Drive", [
            [sg.Col(
                layout=[
                    [
                        sg.T("FD", size=(10, 1)),
                        sg.Slider(
                            range=(1.00, 5),
                            key="_final_drive_",
                            change_submits=True,
                            default_value=1,
                            orientation="h",
                            size=(10, 15),
                            resolution=0.01
                        )
                    ]
                ]
                , expand_x=True, expand_y=True)
            ],

            [sg.Col([[sg.T("Tyre Width",  size=(10, 1)),
                      sg.Slider(range=(155, 345), key="_tyre_width_", change_submits=True, default_value=155,
                                orientation="h", size=(10, 15), resolution=5)]], expand_x=True, expand_y=True)],
            [sg.Col([[sg.T("Type Height",  size=(10, 1)),
                      sg.Slider(range=(20, 120), key="_tyre_height_", change_submits=True, default_value=20,
                                orientation="h", size=(10, 15), resolution=5)]], expand_x=True, expand_y=True)],
            [sg.Col([[sg.T("Tyre Diameter",  size=(10, 1)),
                      sg.Slider(range=(10, 22), key="_tyre_diam_", change_submits=True, default_value=15,
                                orientation="h", size=(10, 15), resolution=1)]], expand_x=True, expand_y=True)],

        ], element_justification="right")
    ],

]
tab3_layout = []

layout = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab('ENGINE CALC', engine_volume_calc_layout),
                    sg.Tab('GEAR CALC', gear_calc_layout),
                    sg.Tab('TEST2', tab3_layout)
                ]
            ],
            key='-group2-', tab_location='bottom'
        )
    ]
]
sg.Button(button_text="Calc", pad=(4, 4))
