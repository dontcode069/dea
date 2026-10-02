import pandas as pd
df = pd.DataFrame({
    "dmu":      ["A", "B", "C"],
    "teachers": [4, 7, 8],
    "rooms":    [3, 3, 1],
    "passes":   [60, 70, 80],
})

df = df.set_index("dmu")
