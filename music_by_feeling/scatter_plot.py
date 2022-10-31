import pandas as pd
import matplotlib.pyplot as plt

#data input
df_data = pd.read_csv('../zep_related_track.csv', encoding = 'utf-8')

fig = plt.figure()
ax = fig.add_subplot(111)
plt.grid() #グリッド
plot_data_1 = 'danceability' #analysis target
plot_data_2 = 'energy' #analysis target
ax.scatter([df_data[plot_data_1]],[df_data[plot_data_2]])

plt.xlabel(plot_data_1, fontsize=18) #x軸ラベル
plt.ylabel(plot_data_2, fontsize=18) #y軸ラベル
plt.title(plot_data_1 + ' and ' + plot_data_2 + ' Scale', fontsize=18) #x軸ラベル
ax.legend()
plt.show()
