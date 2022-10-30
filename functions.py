import ctypes
import PySimpleGUI as sg

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)


def calc_engine_volume(bore: int, stroke: int, cylinder: int) -> None:

    bore = int(bore)
    stroke = int(stroke)
    cylinder = int(cylinder)

    bore /= 10
    stroke /= 10
    total_volume = 3.14 * (bore * bore) / 4 * stroke * cylinder
    # width                #height
    sg.popup_no_border(
        "Result", "Volume CC: %.2f" % total_volume,
        location=(screensize[0] / 2, screensize[1] / 2 - 80)
    )


