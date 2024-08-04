#A3
buying_data['status'] = buying_data['Payment (Rs)'].apply(lambda x: "RICH" if x > 200 else "POOR")
print(buying_data[['Payment (Rs)', 'status']].head())
