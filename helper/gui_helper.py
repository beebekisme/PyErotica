import dearpygui.dearpygui as dpg
import os
from bs4 import BeautifulSoup


class GuiHelperFunc:
    def __init__(self):
        pass


    def set_font():
        FONT_SCALE = 1
        with dpg.font_registry():
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            font_regular = dpg.add_font('../fonts/Inter-Regular.ttf', 16*FONT_SCALE)
            font_medium = dpg.add_font('../fonts/Inter-Medium.ttf', 16*FONT_SCALE)
            font_bold = dpg.add_font('../fonts/Inter-Bold.ttf', 22*FONT_SCALE)
        dpg.set_global_font_scale(1/FONT_SCALE)
        dpg.bind_font(font_regular)
    
    def set_button_theme():
        with dpg.theme(tag='algo_button_border_theme'):
            with dpg.theme_component():
                dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (255, 255, 255, 100))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 0, 0, 0))
                dpg.add_theme_color(dpg.mvThemeCol_Border, (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 3)
                dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 2)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 4)

    def add_custom_listbox(items: list, width: int = 250, height: int = 70, parent: int | str = None, callback: callable = None):
        parent = parent or dpg.last_container() 

        with dpg.theme() as custom_listbox_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 0,0)
                dpg.add_theme_style(dpg.mvStyleVar_ButtonTextAlign, 0, 0.5)

        with dpg.theme() as button_selected_theme:
            with dpg.theme_component(dpg.mvButton):
                dpg.add_theme_color(dpg.mvThemeCol_Button, (0,119,200,153))

        with dpg.theme() as button_normal_theme:
            with dpg.theme_component(dpg.mvButton):
                dpg.add_theme_color(dpg.mvThemeCol_Button, (51, 51, 55, 255))
        
        def custom_listbox_callback(sender):
            if callback:
                callback(dpg.get_item_parent(sender), dpg.get_item_label(sender))
            for button in dpg.get_item_children(dpg.get_item_parent(sender))[1]:
                dpg.bind_item_theme(button, button_normal_theme)
            dpg.bind_item_theme(sender, button_selected_theme)

        with dpg.child_window(height=height, width=width, border=False, parent=parent) as custom_listbox:
            for item in items:
                dpg.add_button(label=item, width=-1, callback=custom_listbox_callback)
        dpg.bind_item_theme(custom_listbox, custom_listbox_theme)

def main():
    GuiHelperFunc.set_font()
    GuiHelperFunc.set_button_theme()

if __name__ == "__main__":
    main()