# 面向别象, 数据分析案例, 主业务逻辑代码
# 实现步骤：
# 1.
# 设计一个些, 可以完成数据的封装
# 2. 設计一个抽象类, 定义文件读取的相关功能, 并使用子类实现具体功能
# 了. 渎取文件, 生产数据矿象
# 4. 进行数据需求的逻辑计算 (计算每一天的销售额)
# 5. 通过PyEcharts进行图形绘制

from 数据分析案例.file_operation_def import textFileReader,JsonFileReader
from 数据分析案例.Record import Record

from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

file_path1 = "/Users/grubby/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/langChain/python_learn/python_learn/数据分析案例/2011年1月销售数据.txt"
file_path2 = "/Users/grubby/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/langChain/python_learn/python_learn/数据分析案例/2011年2月销售数据JSON.txt"

textFileReader = textFileReader(file_path1)
JsonFileReader = JsonFileReader(file_path2)

data_text:list[Record] = textFileReader.fileReader()
data_json:list[Record] = JsonFileReader.fileReader()
all_data:list[Record] = data_text + data_json

data_dict = dict()

for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# 绘制图像
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("sales data",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(is_show=True,title="sales bar")
)
bar.render("sales bar graph.html")