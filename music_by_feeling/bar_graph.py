import pandas as pd
import matplotlib.pyplot as plt

#data input
df_data = pd.read_csv('../zep_related_track.csv', encoding = 'utf-8')

fig = plt.figure()
ax = fig.add_subplot(111)
plt.grid() #グリッド
plot_data = 'danceability' #analysis target
#plot_data = 'energy' #analysis target
ax.hist([df_data[plot_data]],
        #bins=10, density=True, ec='black')
        bins=10, ec='black')
plt.xlabel(plot_data, fontsize=18) #x軸ラベル
plt.ylabel('Count', fontsize=18) #y軸ラベル
plt.title(plot_data + ' Scale', fontsize=18) #x軸ラベル
ax.legend()
plt.show()
