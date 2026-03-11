
import sys
import pandas as pd
print("arguments", sys.argv)

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")



df = pd.DataFrame({"days": [1, 2], "number_of_passengers": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")