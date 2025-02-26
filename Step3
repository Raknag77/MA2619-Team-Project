import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Step2 import validate_input

def make_plot(data: pd.DataFrame) -> plt:
    plt.figure(figsize=(20,5))
    sns.scatterplot(data=data, x="Time", y="Count")
    plt.title("Time against Count")
    plt.xlabel("Time")
    plt.ylabel("Count")
    plt.show()
    
    
my_data = pd.read_excel("CycleData.xlsx", index_col=0)
#print(my_data)

station = validate_input("Enter desired station (ML0028/ML0032/ML0040): ", ["ML0028", "ML0032", "ML0040"])
direction = validate_input("Enter desired direction (Northbound/Southbound): ", ["Northbound", "Southbound"])

filtered_df = my_data[(my_data["Station"] == station) & (my_data["Direction"] == direction)]
#print(filtered_df)

grouped_df = filtered_df.groupby(["Date","Time"])["Count"].sum()
#print(grouped_df)
grouped_df = grouped_df.reset_index()

mean_df = time_mean = grouped_df.groupby(["Time"])["Count"].mean()
#print(mean_df)
mean_df = mean_df.reset_index()


make_plot(mean_df)
