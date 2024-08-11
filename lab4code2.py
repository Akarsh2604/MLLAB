# A2: Feature Density and Histogram
feat = A[:, 0]
histogram , bins = np.histogram(feature, bins=15)
plt.histogram(feature, bins=15)
plt.title('DENSITY AND HISTOGRAM FEATURE')
plt.show()
f_mean = np.mean(feature)
f_var = np.var(feature)
print("Mean of the densisty histogram feature:", f_mean)
print("Variancen of the density histogram feature:", f_var)
