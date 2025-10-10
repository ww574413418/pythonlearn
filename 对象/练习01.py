class Phone:
    __is_5G_enable = False

    def __check_5G(self):
        if self.__is_5G_enable:
            print("5g is opened")
        else:
            print("5g is closed")

    def call_by_5G(self):
        self.__check_5G()
        print("callling")

if __name__ == '__main__':
    phone = Phone()
    phone.call_by_5G()