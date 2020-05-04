import cv2


class MouseParam:
    def __init__(self, img_name):
        # mouse parameter
        self.mouseEvent = {"x": None, "y": None, "event": None, "flags": None}
        # mouse setting
        cv2.setMouseCallback(img_name, self.__CallBackFunc, None)

    def __CallBackFunc(self, eventType, x, y, flags, userdata):
        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = eventType
        self.mouseEvent["flags"] = flags

    # return parameter
    def get_data(self):
        return self.mouseEvent

    # return mouse flag
    def get_flags(self):
        return self.mouseEvent["flags"]

    # return mouse event
    def get_event(self):
        return self.mouseEvent["event"]

    # return x coordinate
    def get_x(self):
        return self.mouseEvent["x"]

    # return y coordinate
    def get_y(self):
        return self.mouseEvent["y"]

    # return xy coordinate
    def get_xy(self):
        return (self.mouseEvent["x"], self.mouseEvent["y"])
