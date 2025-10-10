class AC:
    def make_cool_wind(self):
        pass

    def make_hot_wind(self):
        pass

class Midea_Ac(AC):
    def make_cool_wind(self):
        print("use Midea ac to reduce room temperature")
    def make_hot_wind(self):
        print("use Midea ac to increase room temperature")

class Gree_Ac(AC):
    def make_cool_wind(self):
        print("use Gree ac to reduce room temperature")

    def make_hot_wind(self):
        print("use Gree ac to increase room temperature")

def use_ac(ac:AC):
    ac.make_cool_wind()
    ac.make_hot_wind()

if __name__ == '__main__':
    # gac = Gree_Ac()
    mac = Midea_Ac()

    # use_ac(gac)
    use_ac(mac)