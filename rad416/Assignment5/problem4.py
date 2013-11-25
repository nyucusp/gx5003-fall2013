import pandas as pd
import matplotlib.pyplot as plt

genes = pd.read_csv('genes.dat')

pd.scatter_matrix(genes,alpha=0.7,figsize=(9,9), diagonal='kde')

