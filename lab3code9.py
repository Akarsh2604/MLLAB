num_data = thyroid_data.select_dtypes(include=[np.number])
vec1_full = thyroid_data.loc[0].values
vec2_full = thyroid_data.loc[1].values

if len(numeric_data) >= 2:
    vec1_full = num_data.iloc[0].values
    vec2_full = num_data.iloc[1].values

    print("Vector 1:", vec1_full)
    print("Vector 2:", vec2_full)

    cosine_similarity = 1 - cosine(vec1_full, vec2_full)
    print("Cosine Similarity: {:.4f}".format(cosine_similarity))
else:
    print("Cannot find cosine sim")
