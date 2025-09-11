import pandas as pd

"""
Description

Two data frames are merged by common key (<id> in our case)

Result will have data in columns from both frames

Performed with inner join (by default, can be changed with parameter <how=>)

With this method, result will consist of rows,
that have their keys in both data frames
e.g.
    frame 1 keys = (1 2 3 4    )
    frame 2 keys = (1   3   5 7)

    result keys  = (1   3      )
So, while two first frames have 4 rows each,
result will consist of only 2 rows.
"""

# Utility, creates example data frame
def create_data_frame1():
    data_frame = pd.DataFrame(
        {
            "id": [0,    1,    2,    3   ],
            "A":  ["A0", "A1", "A2", "A3"],
            "B":  ["B0", "B1", "B2", "B3"],
            "C":  ["C0", "C1", "C2", "C3"],
            "D":  ["D0", "D1", "D2", "D3"],
        },
        index=[0, 1, 2, 3],
    )
    return data_frame

# Utility, creates example data frame
def create_data_frame2():
    data_frame = pd.DataFrame(
        {
            "id": [0,    1,    2,    3   ],
            "E":  ["E0", "E1", "E2", "E3"],
            "D":  ["D0", "D1", "D2", "D3"],
            "F":  ["F0", "F1", "F2", "F3"],
        },
        index=[0, 1, 2, 3],
        )
    return data_frame

# Two data frames, with common key "id"
data_frame1 = create_data_frame1()
data_frame2 = create_data_frame2()
key_column = "id"

# Check if <id> key is present
if key_column not in data_frame1.columns:
    raise ValueError(f"First data frame have no {key_column} column")
if key_column not in data_frame2.columns:
    raise ValueError(f"Second data frame have no {key_column} column")

# Method of merge can be changed here (add how="<method>")
# See pd.merge description to see available options 
data_frame_merge = pd.merge(data_frame1,
                            data_frame2,
                            on=key_column)

# Check result
#print("Data frame 1:")
#print(data_frame1.head())
#print("Data frame 2:")
#print(data_frame2.head())
print("Merge result:")
print(data_frame_merge.head(5))
print(f"Rows in data frame 1 = {len(data_frame1)}")
print(f"Rows in data frame 2 = {len(data_frame2)}")
print(f"Rows in merged data frame = {len(data_frame_merge)}")

# Output to .csv
data_frame_merge.to_csv('output.csv', index=False)