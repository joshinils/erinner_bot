
import datetime
from datetime import date, timedelta
from debug_print import *
class erinnerung:
    # text welcher die erinnerung beschreibt
    content: str = ""

    # fälligkeitsdatum
    date_due: date

    # zeitpunkt des letzten erinnern
    date_last_remind: date

    # ob wiederholt erinnert werden soll
    nerven_do: bool

    # wie oft genervt werden soll
    nerven_intervall: timedelta

    # ob die erinnerung wiederholt werden solely
    repeat_do: bool

    # nach welcher zeit die erinnerung wiederholt werden soll
    repeat_interval: timedelta

    # ob die erinnerung abgeschlossen ist / erledigt
    is_active: bool

    def __init__(self: 'erinnerung', l: list) -> 'erinnerung':
        assert isinstance(l, list)
        assert len(l) > 0

        self.l = l
        self.content = ""
        self.date_due = datetime.datetime.now() + timedelta(minutes=5)
        self.date_last_remind = None
        self.nerven_do = True
        self.nerven_intervall = timedelta(minutes=1)
        self.repeat_do = False
        self.repeat_interval = None
        self.is_active = True

        self.parse_args()

    def parse_args(self: 'erinnerung') -> None:
        self.content = self.l[0]
        for elem in self.l:
            debug_print(elem)

    def __eq__(self: 'erinnerung', other: 'erinnerung') -> bool:
        if isinstance(other, erinnerung):
            return self.content == other.content
        return False
