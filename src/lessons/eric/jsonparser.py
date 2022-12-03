import json
import pandas as pd
from pandas.io.json import json_normalize

# with open('sample.json') as f:
#     data = json.load(f)

with open('rake_sample.json') as f:
    rake_data = json.load(f)


# df = pd.json_normalize(data['data'])
rake_df = pd.json_normalize(rake_data)
print(rake_df)

top_rake = (rake_df['attributes.value']
    .div(100_000)
    .sort_values(ascending=False)
    )

print(top_rake.head(100))
