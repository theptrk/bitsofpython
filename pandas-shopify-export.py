# read csv
with open('./data/orders.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [row for row in reader]

# pretty print header names
import json
print(json.dumps(header, indent=2))

# create data frame
df = pd.DataFrame(data, columns=header)

# filter by columns
df['Name', 'Email']

# get numpy.ndarray of unique values by column
df['Vendor'].unique()

# get data frame of unique values by column
col = 'Vendor'
vdf = pd.DataFrame(df[col].unique(), columns=[col])

# get revenue based on a column name
def get_revenue(category, value):
    _filter = df[category] == value
    _df = df[_filter]
    q = _df['Lineitem quantity'].astype(float)
    p = _df['Lineitem price'].astype(float)
    return (q * p).sum()

    # use case
    # vendors = df['Vendor'].unique()
    # vdf['Revenue'] = [get_revenue('Vendor', v) for v in vendors]
    # vdf['% of Rev'] = vdf['Revenue']/vdf['Revenue'].sum()

# get quantity based on Vendor
def get_quantity(vendor):
    vendor_filter = df['Vendor'] == vendor
    df_by_vendor = df[vendor_filter]
    return df_by_vendor['Lineitem quantity'].astype(int).sum()

    # use case
    # vdf['Items Sold'] = [get_quantity(v) for v in vendors]
