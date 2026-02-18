import sys
import pandas as pd
print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"days": [1, 2], "num_passengers": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

print(f"Hello Pipeline, Month is:, {month}")