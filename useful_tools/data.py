import pandas as pd


class Data():
    def __init__(self, file_name, output_name):
        self.file_name = file_name
        self.output_name = output_name

    def remove_ouliers_using_std(dt, columns=list, n_std=3):
        '''Recommended - assumes Gaussian distribution 
           Works for an array of columns, industry best practice is n_std = 3 
           https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/
        '''
        df = pd.DataFrame(dt)
        for col in columns:
            mean = df[col].mean()
            sd = df[col].std()
            df = df[(df[col] <= mean+(n_std*sd))]
        return df

    def remove_outliers_using_quantiles(dt, columns=list, upper=0.95, lower=0.05):
        '''Simplified - does not assume/require Gaussian distribution
            Works for an array of columns, lower and upper bounds change depending on the tolerance
            https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/
        '''
        df = pd.DataFrame(dt)
        for col in columns:
            lower = df[f'{col}'].quantile(lower)
            upper = df[f'{col}'].quantile(upper)
            df.clip(lower=lower, upper=upper)
        return df