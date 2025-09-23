import pandas as pd

# Utility, creates example data frame
def __create_data_frame1__():
    data_frame = pd.DataFrame(
        {
            "id": [0,    1,    2,    3,  ],
            "A":  ["A0", "A1", "A2", "A3"],
            "B":  ["B0", "B1", "B2", "B3"],
            "C":  ["C0", "C1", "C2", "C3"],
            "D":  ["D0", "D1", "D2", "D3"],
        },
        index=[0, 1, 2, 3],
    )
    return data_frame

# Utility, creates example data frame
def __create_data_frame2__():
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

def pandas_merge(data_frame1, data_frame2, key_column, how_to='inner', csv_output=False):
    """
    Performs merge of two dataframes.

    Parameters
    ----------
    data_frame1 : pd.DataFrame
        First dataframe.
    data_frame2 : pd.DataFrame
        Second dataframe.
    key_column  : str
        Name of a column on which dataframes will be merged.
    how_to      : str   (optional, default='inner')
        Merge method (inner, outer, left, right).
    csv_output  : bool  (optional, default=False')
        Set True, to output the result into .csv file.

    Returns
    -------
    pd.DataFrame
        Result of merge.
    """

    if isinstance(data_frame1, pd.DataFrame) is False:
        raise ValueError(f"First argument supposed to be pd.DataFrame")
    if isinstance(data_frame2, pd.DataFrame) is False:
        raise ValueError(f"Second argument supposed to be pd.DataFrame")
    if isinstance(key_column, str) is False:
        raise ValueError(f"Third argument supposed to be string")
    if True in list(data_frame1.duplicated()):
        raise ValueError(f"First DataFrame contains dublicates")
    if True in list(data_frame2.duplicated()):
        raise ValueError(f"Second DataFrame contains dublicates")



    if key_column not in data_frame1.columns:
        raise ValueError(f"First data frame have no {key_column} column")
    if key_column not in data_frame2.columns:
        raise ValueError(f"Second data frame have no {key_column} column")
    
    data_frame_merge = pd.merge(data_frame1,
                                data_frame2,
                                on=key_column,
                                how=how_to)
    
    if csv_output:
        data_frame_merge.to_csv('pandas_merge_output.csv', index=False)


    return data_frame_merge


# Two data frames, with common key "id"
data_frame1 = __create_data_frame1__()
data_frame2 = __create_data_frame2__()
key_column = "id"

# Usage example
data_frame_merge = pandas_merge(data_frame1, 
                                data_frame2, 
                                key_column,
                                csv_output=True)

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