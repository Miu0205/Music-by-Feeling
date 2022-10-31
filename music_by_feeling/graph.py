import pandas as pd
import matplotlib.pyplot as plt

#data input
df_2017 = pd.read_csv('../zep_related_track.csv', encoding = 'utf-8')
#df_2018 = pd.read_csv('2018_track_analysis.csvのpath', encoding = 'utf-8')
#df_2019 = pd.read_csv('2019_track_analysis.csvのpath', encoding = 'utf-8')
#df_2020 = pd.read_csv('2020_track_analysis.csvのpath', encoding = 'utf-8')


fig = plt.figure()
ax = fig.add_subplot(111)
plt.grid() #グリッド
plot_data = 'danceability' #analysis target
#plot_data = 'energy' #analysis target
ax.hist([df_2017[plot_data]],
        #df_2018[plot_data],
        #df_2019[plot_data],
        #df_2020[plot_data]],
        #label=['2017', '2018', '2019', '2020'],
        #label=['2017'],
        #bins=10, density=True, ec='black')
        bins=10, ec='black')
plt.xlabel(plot_data, fontsize=18) #x軸ラベル
plt.ylabel('Count', fontsize=18) #y軸ラベル
plt.title(plot_data + ' Scale', fontsize=18) #x軸ラベル
#plt.bar([df_2017[plot_data]], height, width=1.0)
ax.legend()
plt.show()
