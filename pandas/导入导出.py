import numpy as np
import pandas as pd

# 导入
student = pd.read_csv("student.csv")
print(student)
# 导出
student.to_pickle("student.pickle")

# 读物pickle文件
student_pickle = pd.read_pickle("student.pickle")
print(student_pickle)