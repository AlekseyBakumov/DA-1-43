import pandas as pd

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

data_frame1 = create_data_frame1()
data_frame2 = create_data_frame2()
#print(data_frame1.head())
print(f"Rows in data frame 1 = {len(data_frame1)}")
#print(data_frame2.head())
print(f"Rows in data frame 2 = {len(data_frame2)}")

data_frame_merge = pd.merge(data_frame1,
                            data_frame2,
                            on="id")

print(data_frame_merge.head(5))
print(f"Rows in merged data frame = {len(data_frame_merge)}")