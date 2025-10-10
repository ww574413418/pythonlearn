from my_utils import file_util
from my_utils import str_util

file_name = "/Users/grubby/Downloads/myutils.txt"
str = "hello world"

re_str = str_util.str_reverse(str)
print(re_str)
sub_str = str_util.substr(str,0,4)
print(sub_str)

file_util.print_file_info(file_name)
file_util.append_to_file(file_name,"hell world")

