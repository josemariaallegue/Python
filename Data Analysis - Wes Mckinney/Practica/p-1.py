import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(6, 4),
    index=['one', 'two', 'three', 'four', 'five', 'six'],
    columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))

df = pd.DataFrame()

df.plot.bar()