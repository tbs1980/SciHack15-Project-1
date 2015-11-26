from __future__ import print_function
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

# read through the folders and catagorise the data fiels
path_to_journal_data = '/Users/sbalan/Desktop/peerj/'

dirs_with_papers = os.listdir(path_to_journal_data)

dict_of_file_extensions = {}

for dir_name in dirs_with_papers:
    try:
        list_of_files = os.listdir(path_to_journal_data+dir_name)
        list_of_files.remove('suppdatalinks.txt')
        list_of_files.remove('fulltext.html')
        for file_name in list_of_files:
            extension = os.path.splitext(file_name)[1]
            if extension in dict_of_file_extensions:
                dict_of_file_extensions[extension] += 1
            else:
                dict_of_file_extensions[extension] = 1

    except Exception as inst:
        pass

# we have all the keys, we need to make another dict with zeros
# to start with so that we can add the number of files for each article

list_of_metrics = []
dirs_with_papers = os.listdir(path_to_journal_data)

list_of_metrics_df = pd.DataFrame()

for dir_name in dirs_with_papers:
    try:

        # now increase the counts for each extension
        list_of_files = os.listdir(path_to_journal_data+dir_name)
        list_of_files.remove('suppdatalinks.txt')
        list_of_files.remove('fulltext.html')

        # add the file name
        metric_of_file_extensions = {"article_id": dir_name}
        # copy the keys and set the keys to 0
        for key in dict_of_file_extensions:
            metric_of_file_extensions[key] = 0

        for file_name in list_of_files:
            extension = os.path.splitext(file_name)[1]
            metric_of_file_extensions[extension] += 1

        list_of_metrics.append(metric_of_file_extensions)

        metric_of_file_extensions.pop("article_id",None)
        list_of_metrics_df = list_of_metrics_df.append( pd.DataFrame(data=metric_of_file_extensions,index=[dir_name]) )

    except Exception as inst:
        pass

#keys = list_of_metrics[0].keys()
#with open("test.txt", "wb") as out_file:
#    dict_writer = csv.DictWriter(out_file, keys)
#    dict_writer.writeheader()
#    dict_writer.writerows(list_of_metrics)


list_of_metrics_df.to_csv("peerj_pandas.csv", header=True)

#list_of_metrics_df[0:5].transpose().plot()
