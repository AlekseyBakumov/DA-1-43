## Description

Two data frames are merged by common key ('id' in example)

Result will have data in columns from both frames

Performed with inner join (by default, can be changed with parameter 'how=')
#
With this method, result will consist of rows,
that have their keys in both data frames, e.g.
-    frame 1 keys = (1 2 3 4    )
-    frame 2 keys = (1   3   5 7)
-    result keys  = (1   3      )
#
So, while two first frames have 4 rows each,
result will consist of only 2 rows.
