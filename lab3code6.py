categorical_columns = thyroid_data.select_dtypes(include=['object']).columns

for col in numeric_columns:
    if(thyroid_data[col] - thyroid_data[col].mean()).abs().max() <=3 * thyroid_data[col].std():
        thyroid_data[col].fillna(thyroid_data[col].mean(), inplace = True)
    else:
        thyroid_data[col].fillna(thyroid_data[col].median(), inplace = True)

for col in categorical_columns:
    thyroid_data[col].fillna(thyroid_data[col].mode()[0], inplace = True)

missing_values = thyroid_data.isnull().sum()

thyroid_data.head(), missing_values
