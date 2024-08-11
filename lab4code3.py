# A3: Minkowski Distance with varying r
dist_1 = []
f_1 = X[:, 0] 
f_2 = X[:, 1]  


for i in range(1, 11):
    dist_2 = minkowski(feature_1, feature_2, i)
    dist_1.append(dist_2)

plt.plot(range(1, 11), dist_1)
plt.xlabel('Minkowski i')
plt.ylabel('normal distance')
plt.title('Minkowski Distance for varying r')
plt.show()
