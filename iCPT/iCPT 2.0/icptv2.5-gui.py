from dearpygui.core import *
from dearpygui.simple import *

# themes
set_main_window_size(540, 720)
set_global_font_scale(1.3)
set_theme("Gold")

with window("iCPT", width=520, height=677):
    print("GUI UP....")
    set_window_pos("iCPT", 0, 0)
    add_separator()
    add_spacing(count=12)
    add_text("")
    add_spacing(count=12)
    add_input_text("PASSWORD", width=415, default_value="")
start_dearpygui()
