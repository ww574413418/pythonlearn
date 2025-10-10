class Phone:
    #私有变量
    __current_voltage = 1


    #私有方法
    def __get_current_voltage(self):
        print(f"current voltage is {self.__current_voltage}")
        return self.__current_voltage

    def use_5G_moudle(self):
        voltage = self.__get_current_voltage()
        if voltage >= 1:
            print("开启5G模块")
        else:
            print("开启省电模式")


if __name__ == '__main__':
    phone = Phone()
    phone.use_5G_moudle()