print(thyroid_data[numeric_columns].describe())

scaler = MinMaxScaler()
thyroid_data_normalized = thyroid_data.copy()
thyroid_data_normalized[numeric_columns] = scaler.fit_transform(thyroid_data[numeric_columns])

print(thyroid_data_normalized.head())

scaler_standard = StandardScaler()
thyroid_data_standardized = thyroid_data.copy()
thyroid_data_standardized[numeric_columns] = scaler_standard.fit_transform(thyroid_data[numeric_columns])

print(thyroid_data_standardized.head())
