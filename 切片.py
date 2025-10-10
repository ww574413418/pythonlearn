# 练习案例：序列的切片实践
# 有字符串："万过薪月, 员序程马黑来, nohtyP学"
# • 请使用学过的任何方式, 得到"黑马程序员"
# 可用方式参考：
# • 倒序字符串, 切片取出或切片取出, 然后倒序
# • split分隔”, "replace替换"来"为空, 倒序字符串

str = "万过薪月, 员序程马黑来, nohtyP学"

str_list = str.split(",")
str2 = str_list[1]
str3 = str2.replace("来","")
str4 = str3[::-1]
print(str4)