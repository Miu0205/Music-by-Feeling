import pandas as pd
import matplotlib.pyplot as plt
##data input
df_data = pd.read_csv('../zep_related_track.csv', encoding = 'utf-8')

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.grid() #グリッド
plot_data_1 = 'danceability' #analysis target
plot_data_2 = 'energy' #analysis target
plot_data_3 = 'valence'
ax.scatter([df_data[plot_data_1]],[df_data[plot_data_2]], [df_data[plot_data_2]],s=0.5)


plt.show()
