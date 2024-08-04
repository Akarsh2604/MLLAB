#A3
buy_data['status'] = buy_data['Payment (Rs)'].apply(lambda x: "RICH" if x > 200 else "POOR")
print(buy_data[['Payment (Rs)', 'status']].head())
