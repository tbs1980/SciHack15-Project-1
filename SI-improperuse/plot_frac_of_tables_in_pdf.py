import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read the csv file
journal_data_file_name = "./peerj-pdf-table-ratio.csv"

# rows 51,52 and 600 had an extra coma in it. changed
journal_df = pd.DataFrame().from_csv(journal_data_file_name,header=0, sep=',',index_col=0)

# plot the data
journal_df['fraction'].plot(kind='hist',histtype='step',bins=10)

png_file_name = journal_data_file_name.replace('csv','png')
plt.savefig(png_file_name)
