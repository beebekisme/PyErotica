import dearpygui.dearpygui as dpg
import pprint
import ctypes
import dearpygui.demo as demo

import helper.gui_helper as gui_helper
import helper.reddit_helper as reddit_helper
import helper.extra_helpers as extra_helpers

dpg.create_context()
gui_helper.GuiHelperFunc.set_font()
gui_helper.GuiHelperFunc.set_button_theme()


GUI_CONSTANTS = {
    "SIDEBAR_WIDTH": 400 
    
}

def resize_primary_window():
    
    x,y = dpg.get_item_rect_size(primary_window)
    
    dpg.set_item_width(demo_button, x//6)
    dpg.set_item_height(child_window, y)
    dpg.set_item_width(child_window, x//6)
    

with dpg.window(tag ="Algorithms List", label="Algorithms List",
                 width=250,
                height=250) as primary_window:
    
    with dpg.group(horizontal=True):
        with dpg.child_window() as child_window:
            demo_button = dpg.add_button(label="Show Demo", 
                                         width=GUI_CONSTANTS['SIDEBAR_WIDTH'],
                                        height=30, tag="Show Demo",
                                          callback=demo.show_demo) 
            
            def _selection(sender, app_data, user_data):
                for item in user_data:
                    if item != sender:
                        dpg.set_value(item, False)

            with dpg.tree_node(label="Available Subreddits"):
                sub_reddits = [dpg.add_selectable(label=f"{item}") for item in reddit_helper.Reddit_Scraper().return_subreddits() ]
                for sub_reddit in sub_reddits:
                    dpg.configure_item(sub_reddit, user_data=sub_reddits, callback=lambda: pprint.pprint(dpg.get_value(sub_reddit)))
                    

        with dpg.child_window() as viewport:
            pass



with dpg.item_handler_registry() as registry:
    dpg.add_item_resize_handler(callback=resize_primary_window)
dpg.bind_item_handler_registry(primary_window, registry)

def main():
    dpg.create_viewport(title='PySrt', width=1280, height=720)
    ctypes.windll.user32.SetProcessDPIAware(2)
    dpg.setup_dearpygui()

    dpg.show_viewport()
    dpg.set_primary_window("Algorithms List", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()