from pyecharts.charts import Line
from pyecharts.options import TitleOpts,ToolboxOpts,LegendOpts

line = Line()

line.add_xaxis(["china","England","America"])
line.add_yaxis("GPD",[10,20,30])
# 设置全局配置
line.set_global_opts(
    title_opts = TitleOpts(True,"GDP",pos_top="center"),
    legend_opts = LegendOpts(is_show=True),
    toolbox_opts = ToolboxOpts(is_show=True),
)
line.render()

