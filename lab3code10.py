data_set = thyroid_data.iloc[:20]

for c in data_set.columns:
    if data_set[c].dtype == 'object':
        le = LabelEncoder()
        data_set[c] = le.fit_transform(data_set[c].astype(str))
        
data_set2 = data_set.values

jc_sim = 1-pairwise_distances(data_set2, metric = 'jaccard')
smc_sim = 1-pairwise_distances(data_set2, metric=lambda u, v: np.sum(u==v) / len(u))
cosine_sim = 1-pairwise_distances(data_set2, metric = 'cosine')

plt.figure(figsize=(10,8))
sns.heatmap(jc_sim, annot = True, cmap='coolwarm')
plt.title('Jaccard Similarity Heatmap')
plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(smc_sim, annot = True, cmap='coolwarm')
plt.title('Simple Matching Similarity Heatmap')
plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(cosine_sim, annot = True, cmap='coolwarm')
plt.title('Cosine Similarity Heatmap')
plt.show()
