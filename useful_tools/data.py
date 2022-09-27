import pandas as pd


class Data():
    def __init__(self, file_name, output_name):
        self.file_name = file_name
        self.output_name = output_name

    def remove_ouliers_using_std(df, columns=list, n_std=float):
        for col in columns:
            mean = df[col].mean()
            sd = df[col].std()
            df = df[(df[col] <= mean+(n_std*sd))]
        return df

    def remove_outliers_using_quantiles(df, col_name, upper=0.95, lower=0.05):
        lower = df[f'{col_name}'].quantile(lower)
        upper = df[f'{col_name}'].quantile(upper)
        return df.clip(lower=lower, upper=upper)
