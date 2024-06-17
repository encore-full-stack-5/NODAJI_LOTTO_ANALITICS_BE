import pandas as pd

async def sort_lotto(index, data):
    df = pd.DataFrame(data=data, index=index)
    df_sorted = df.apply(lambda row: sorted(row), axis=1, result_type='expand')
    return df_sorted
    

async def get_vertical_chart(index, data):
    df_sorted = await sort_lotto(index, data)
    all_values = df_sorted.values.flatten()
    counts = pd.Series(all_values).value_counts().reindex(range(1, 46), fill_value=0).astype(int)
    return counts.tolist()

async def get_lotto_result_by_group(index, data):
    df_sorted = await sort_lotto(index, data)
    all_values = df_sorted.values.flatten()
    counts = pd.Series(all_values).value_counts().reindex(range(1, 46), fill_value=0).astype(int)
    total_lotto_result_by_group = list()
    for i in range(1, 46, 10):
        total_lotto_result_by_group.append(int(counts.loc[i:i+9].sum()))
    return total_lotto_result_by_group

async def get_odd_even(index, data):
    df_sorted = await sort_lotto(index, data)
    desc_lotto_result = df_sorted.sort_index(ascending=False)
    return desc_lotto_result
    