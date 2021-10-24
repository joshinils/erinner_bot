
class erinnerung:
    text: str = ""

    def __init__(self :'erinnerung', l: list = [""]) -> 'erinnerung':
        assert isinstance(l, list)
        self.l = l
        self.text = l[0]

    def parse_args(self :'erinnerung') -> None:
        for elem in self.l:
            print(elem)

    def __eq__(self: 'erinnerung', other: 'erinnerung') -> bool:
        if isinstance(other, erinnerung):
            return self.text == other.text
        return False
