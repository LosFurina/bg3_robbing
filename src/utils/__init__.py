import pyautogui
import time

from src.heads import Point
from src.heads import DELAY
from src.heads import LogLevel

from pathlib import Path
from datetime import datetime


PATH_PIC = "src/assets/pics"


class AltitudeImprove():
    """
    """
    def __init__(self):
        pass

    def start():
        pass


class Rob():
    """
    """
    def __init__(self):
        pyautogui.PAUSE = 1
        self.point_balance: Point =  Utils._get_pix_balance_offer()
        Utils.log(f"Balance Point x: {self.point_balance.x} | Balance Point y: {self.point_balance.y}", LogLevel.DEBUG)
        self.point_barter: Point =  Utils._get_pix_barter()
        Utils.log(f"Balance Point x: {self.point_barter.x} | Balance Point y: {self.point_barter.y}", LogLevel.DEBUG)

    def _rob_once(self):
        time.sleep(DELAY)
        pyautogui.click(self.point_balance.x, self.point_balance.y)
        time.sleep(DELAY)
        pyautogui.click(x=self.point_barter.x, y=self.point_barter.y)
    
    def start(self):
        times = 1
        while times < 10:
            Utils.log(f"Current robbing times is: {times}", LogLevel.INFO)
            self._rob_once()
            times = times + 1
        

class Utils():
    """
    """
    # ANSI color codes
    COLOR_DEBUG = "\033[94m"  # Blue
    COLOR_INFO = "\033[92m"   # Green
    COLOR_WARNING = "\033[93m" # Yellow
    COLOR_FATAL = "\033[91m"   # Red
    COLOR_RESET = "\033[0m"    # Reset to default

    @staticmethod
    def log(info: str, level: LogLevel):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # format time
        if level == LogLevel.DEBUG:
            output_message = f"{Utils.COLOR_DEBUG}[DE---BUG][{current_time}] {info}{Utils.COLOR_RESET}"
        elif level == LogLevel.INFO:
            output_message = f"{Utils.COLOR_INFO}[IN----FO][{current_time}] {info}{Utils.COLOR_RESET}"
        elif level == LogLevel.WARNING:
            output_message = f"{Utils.COLOR_WARNING}[WA-RNING][{current_time}] {info}{Utils.COLOR_RESET}"
        elif level == LogLevel.FATAL:
            output_message = f"{Utils.COLOR_FATAL}[FA---TAL][{current_time}] {info}{Utils.COLOR_RESET}"
        else:
            output_message = f"[UNK---NOW][{current_time}][UNKNOWN] {info}"
        print(output_message)

    @staticmethod
    def _get_pix_from_pic(pic_path: Path) -> Point:
        try:
            location = pyautogui.locateOnScreen(pic_path.as_posix(), confidence=0.8)
            ret = Point()
            ret.x = location.left + location.width / 2
            ret.y = location.top + location.height / 2
            return ret
        except pyautogui.ImageNotFoundException:
            # TODO
            Utils.log(f"This function is not finished!", LogLevel.FATAL)

    @staticmethod
    def _get_pix_barter() -> Point:
        path = Path(PATH_PIC + "/" + "bater.png")
        return Utils._get_pix_from_pic(path)

    @staticmethod
    def _get_pix_balance_offer() -> Point:
        path = Path(PATH_PIC + "/" + "balance_offer.png")
        return Utils._get_pix_from_pic(path)

    @staticmethod
    def _get_pix_consumables() -> Point:
        pass

    @staticmethod
    def _get_pix_magical() -> Point:
        pass

    @staticmethod
    def _get_pix_misc() -> Point:
        pass

