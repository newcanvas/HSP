class SideCharacter:

    def __init__(self, nam):
        self._name = nam
        self.sl_level = 0

    def sl_level_up(self):
        self.sl_level += 1

class MainCharacter:

    def __init__(self, nam):
        self._name = nam
        self.sl = []

    def start_new_sl(self, nsl):
        self.sl.append(nsl)

sc = SideCharacter('Yukiko')
mc = MainCharacter('YN')
mc.start_new_sl(sc)
sc.sl_level_up()

