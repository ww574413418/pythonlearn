import json
from pyecharts.charts import Line
from pyecharts.options import *

# 读取美国,日本,印度的新冠数据
file_US = open("/Users/grubby/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/langChain/python_learn/python_learn/图表案例/可视化案例数据/折线图数据/美国.txt","r",encoding="UTF-8")
file_JP = open("/Users/grubby/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/langChain/python_learn/python_learn/图表案例/可视化案例数据/折线图数据/日本.txt","r",encoding="UTF-8")
file_IN = open("/Users/grubby/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/langChain/python_learn/python_learn/图表案例/可视化案例数据/折线图数据/印度.txt","r",encoding="UTF-8")

file_data_us = file_US.read()
file_data_jp = file_JP.read()
file_data_in = file_IN.read()

# 处理数据,让其符合json数据格式
file_data_us = file_data_us.replace("jsonp_1629344292311_69436(", "")
file_data_jp = file_data_jp.replace("jsonp_1629350871167_29498(", "")
file_data_in = file_data_in.replace("jsonp_1629350745930_63180(", "")
file_data_us = file_data_us[:-2]
file_data_jp = file_data_jp[:-2]
file_data_in = file_data_in[:-2]
# 将json数据专程python字典
us_dict = json.loads(file_data_us)
jp_dict = json.loads(file_data_jp)
in_dict = json.loads(file_data_in)

# 找到x,y轴数据
us_trend_data = us_dict["data"][0]["trend"]
us_x_data = us_trend_data["updateDate"][:314]
us_y_data = us_trend_data["list"][0]["data"][:314]

jp_trend_data = jp_dict["data"][0]["trend"]
jp_x_data = jp_trend_data["updateDate"][:314]
jp_y_data = jp_trend_data["list"][0]["data"][:314]

in_trend_data = in_dict["data"][0]["trend"]
in_x_data = in_trend_data["updateDate"][:314]
in_y_data = in_trend_data["list"][0]["data"][:314]

# 生成图表
line = Line()
# 添加x轴数据
line.add_xaxis(us_x_data)
# 添加y轴数据
line.add_yaxis("美国确诊人数",us_y_data)
line.add_yaxis("日本确诊人数",jp_y_data)
line.add_yaxis("印度确诊人数",in_y_data)

# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(is_show=True,title="新冠确证人数",pos_bottom="1%",pos_right="center"),

)
# 生成
line.render()

file_US.close()
file_JP.close()
file_IN.close()

