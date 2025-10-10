class phone:
    IMEI = None
    producer = None

    def call_by_4g(self):
        print("use 4g to call")

class NFCreader:
    NFCtype = None
    producer = None

    def reader(self):
        print("read card")

    def writer(self):
        print("writer card")

class phone2022(phone,NFCreader):
    faceId = False

    def call_by_5g(self):
        print("use 5g to call")

    def add_friend_byScan(self):
        self.reader()
        print("add friend by scan card")

if __name__ == '__main__':
    phone2022 = phone2022()
    phone2022.call_by_4g()
    phone2022.call_by_5g()
    phone2022.add_friend_byScan()