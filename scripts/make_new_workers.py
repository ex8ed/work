import pandas as pd
import os

PTH = os.getcwd()
print(PTH)
os.chdir(PTH[:len(PTH) - 8])
workers = pd.read_excel("./data/DB.xlsx", sheet_name="workers")
children = pd.read_excel("./data/DB.xlsx", sheet_name="children")
otdeli = pd.read_excel("./data/DB.xlsx", sheet_name="otdeli")
print(workers)
print(children)
print(otdeli)
workers.to_pickle("./data/workers.pic")
children.to_pickle("./data/children.pic")
otdeli.to_pickle("./data/otdeli.pic")
