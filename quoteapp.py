import pandas as pd
import numpy as np
import time as ti
import subprocess, sys

array = pd.read_csv('quotes.csv')

i = 10
while i == 10:
    x = np.random.randint(0, 1660)
    y = array.iloc[x]
    print(f"{y['Quote']} -{y['Author']}")
    ti.sleep(7)
    subprocess.run("cls", shell=True)