import pandas as pd
import matplotlib.pyplot as plt

#data input
df_data = pd.read_csv('../zep_related_track.csv', encoding = 'utf-8')

fig = plt.figure()
ax = fig.add_subplot(111)
plt.grid() #グリッド
plot_data_1 = 'danceability' #analysis target
plot_data_2 = 'energy' #analysis target
ax.scatter([df_data[plot_data_1]],[df_data[plot_data_2]], s=0.5, color = '#dcdcdc')

#全員丸　b, 2人丸　y, 1人丸　m, 丸0　r
#楽：10、アクティブ：10
plt.plot(0.759, 0.961, marker = "x", color = "m") #
plt.plot(0.729, 0.896, marker = "x", color = "r") #
plt.plot(0.729, 0.886, marker = "x", color = "m") #
plt.plot(0.742, 0.856, marker = "x", color = "y") #
plt.plot(0.718, 0.9, marker = "x", color = "b") #maru


#楽：0、アクティブ：10
plt.plot(0.611, 0.29, marker = "x", color = "r") #
plt.plot(0.642, 0.329, marker = "x", color = "r") #
plt.plot(0.682, 0.451, marker = "x", color = "r") #
plt.plot(0.718, 0.475, marker = "x", color = "b") #
plt.plot(0.49, 0.23, marker = "x", color = "m") #


#楽：0、アクティブ：0
plt.plot(0.446, 0.258, marker = "x", color = "b") #
plt.plot(0.49, 0.23, marker = "x", color = "b") #
plt.plot(0.53, 0.348, marker = "x", color = "b") #
plt.plot(0.611, 0.29, marker = "x", color = "b") #
plt.plot(0.642, 0.329, marker = "x", color = "b") #


#楽：10、アクティブ：0
plt.plot(0.291, 0.882, marker = "x", color = "b") #○
plt.plot(0.339, 0.909, marker = "x", color = "b") #○
plt.plot(0.347, 0.944, marker = "x", color = "y") #○
plt.plot(0.342, 0.817, marker = "x", color = "y") #2人○
plt.plot(0.449, 0.819, marker = "x", color = "m") #1人×



plt.xlabel(plot_data_1, fontsize=18) #x軸ラベル
plt.ylabel(plot_data_2, fontsize=18) #y軸ラベル
plt.title(plot_data_1 + ' and ' + plot_data_2 + ' Scale', fontsize=18) #x軸ラベル
ax.legend()
plt.show()
