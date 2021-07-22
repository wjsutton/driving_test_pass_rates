# In Python
# Aggregate the datasets to explore how car test results vary by location and gender
# see read me for details of source locations

import pandas as pd

all_tests = pd.read_excel("data/all_pratical_tests.ods", engine="odf", sheet_name = '2020-21', header = 3)
#auto_tests = pd.read_excel("data/auto_pratical_tests.ods", engine="odf")

print(all_tests)