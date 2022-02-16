
import json
import typing
from datetime import date, datetime, timedelta

from debug_print import debug_print


def json_serial(obj: typing.Union[datetime, date, timedelta]) -> typing.Union[str, typing.Dict]:
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, (timedelta)):
        return {
            "microseconds": obj.microseconds,
            "seconds": obj.seconds,
            "days": obj.days,
        }

    # print(type(obj))
    # return str(obj)
    # raise TypeError("Type %s not serializable" % type(obj))


class Erinnerung:
    content: str = ""  # text welcher die erinnerung beschreibt
    date_created: datetime  # erstelldatum
    date_due: datetime  # fälligkeitsdatum
    date_last_remind: typing.Optional[datetime]  # zeitpunkt des letzten erinnern
    nerven_do: bool  # ob wiederholt erinnert werden soll
    nerven_intervall: timedelta  # wie oft genervt werden soll
    repeat_do: bool  # ob die erinnerung wiederholt werden soll
    repeat_interval: typing.Optional[timedelta]  # nach welcher zeit die erinnerung wiederholt werden soll
    is_active: bool  # ob die erinnerung abgeschlossen ist / erledigt
    metadata: typing.Dict

    def __init__(self: 'Erinnerung', arg_liste: list, metadata: typing.Dict = {}) -> None:
        assert isinstance(arg_liste, list)
        assert len(arg_liste) > 0

        self.metadata = metadata
        self.arg_liste = arg_liste
        self.content = ""
        self.date_created = datetime.now()
        self.date_due = datetime.now() + timedelta(minutes=5)
        self.date_last_remind = None
        self.nerven_do = True
        self.nerven_intervall = timedelta(minutes=1)
        self.repeat_do = False
        self.repeat_interval = None
        self.is_active = True

        self.parse_args()

    def parse_args(self: 'Erinnerung') -> None:
        self.content = self.arg_liste[0]
        for arg in self.arg_liste:
            debug_print(arg)

    def __eq__(self: 'Erinnerung', other: object) -> bool:
        if not isinstance(other, Erinnerung):
            return NotImplemented
        return self.content == other.content

    def save_json(self: 'Erinnerung') -> None:
        with open("filename.json", "w") as file:
            data = {}

            data["metadata"] = self.metadata

            data["data"] = {}
            data["data"]["arg_list"] = self.arg_liste
            data["data"]["content"] = self.content
            data["data"]["date_created"] = self.date_created
            data["data"]["date_due"] = self.date_due
            data["data"]["date_last_remind"] = self.date_last_remind
            data["data"]["nerven_do"] = self.nerven_do
            data["data"]["nerven_intervall"] = self.nerven_intervall
            data["data"]["repeat_do"] = self.repeat_do
            data["data"]["repeat_interval"] = self.repeat_interval
            data["data"]["is_active"] = self.is_active

            json.dump(data, file, indent=4, default=json_serial, sort_keys=True)
