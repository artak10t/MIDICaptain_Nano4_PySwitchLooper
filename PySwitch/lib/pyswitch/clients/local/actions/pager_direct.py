from ....controller.actions import Action

# Proxy action which directly selects a page
class DirectPagerProxy(Action):
    def __init__(self, pager, page_index, use_leds, id, enable_callback):
        Action.__init__(self, {
            "useSwitchLeds": use_leds,
            "id": id,
            "enableCallback": enable_callback
        })
        self.__pager = pager
        self.__page_index = page_index

    # Called when the switch is pushed down
    def push(self):
        if not hasattr(self.__pager, "switch") or not self.__pager.switch:
            raise Exception("Every Pager must be assigned to a switch. See Select Page action.")
        
        if not self.__pager.pages: 
            return
        
        if self.__page_index == None:
            return
        
        self.__pager.current_page_index = self.__page_index
        self.__pager.current_page_id = self.__pager.pages[self.__pager.current_page_index]["id"] if len(self.__pager.pages) > 0 else None
    
        self.__pager.appl.reset_actions()
        self.__pager.update_displays()

    def update_displays(self):
        if not hasattr(self, "switch"):
            return 
        
        if self.__page_index == None:
            return
        
        if not self.enabled:
            return
        
        page_select = self.__pager.pages[self.__page_index]
        
        if "color" in page_select:
            self.switch_color = page_select["color"]
        else:
            self.switch_color = (255, 255, 255)
            
        is_current = self.__page_index == self.__pager.current_page_index
        self.switch_brightness = self.__pager.led_brightness_on if is_current else self.__pager.led_brightness_off              
