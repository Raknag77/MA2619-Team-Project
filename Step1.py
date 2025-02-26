import pandas as pd
import csv
from itertools import count

station_names = ["ML0028", "ML0032", "ML0040"]


num_rows = 0

with open("project_data.csv", "w") as f:
    pass

for i in range(2014,2019+1):
    for j in range (1,4+1):
        file_name = f"{i}-Q{j}-Central.csv"
        with open("TfL-data/" + file_name, "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                out_row = []
                if row[1] in station_names:
                    row[0] = f"{i}Q{j}"
                    out_row.append(num_rows)
                    out_row.extend(row)
                    num_rows += 1
                    with open("project_data.csv", "a") as f:
                        writer = csv.writer(f)
                        writer.writerow(out_row)


col_names = ["Quarter", "Station", "Date", "Weather", "Time", "Day", "Drop1", "Direction", "Drop2", "Mode", "Count"]
df = pd.read_csv("project_data.csv", names=col_names)
df = df.drop(["Drop1", "Drop2"], axis=1)
df["Full_time"] = df["Date"] + " " + df["Time"]

with pd.ExcelWriter("CycleData.xlsx") as writer:
    df.to_excel(writer, sheet_name="Sheet1")
