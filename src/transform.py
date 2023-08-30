
# function to identify and drop duplicates
def identify_and_remove_duplicates(df):

    if df.duplicated().sum() > 0:
        print(f"number of duplicates = {df.duplicated().sum()}")
        df_cleaned = df.drop_duplicates(keep='first')

    else:
        df_cleaned = df
        print('No duplicates found')

    return df_cleaned




