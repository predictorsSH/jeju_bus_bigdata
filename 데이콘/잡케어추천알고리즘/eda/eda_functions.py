import pandas as pd
import matplotlib.pyplot as plt

def bar_chart(x: pd.Series) :
    x.value_counts().plot(kind='bar')
    plt.title(x.name)
    plt.ylabel('counts')
    plt.show()

