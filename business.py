import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    print(df['Year'].tolist())

    year            = df['Year'].tolist()

    pytorch_data    = df['Pytorch'].tolist()

    tensorflow_data = df['Tensorflow'].tolist()

    # print(df['quebec'].tolist())

    result_dict = {
        'year'            : year,
        'pytorch'    : pytorch_data,
        'tensorFlow' : tensorflow_data
    }

    # print(result_dict)

    return result_dict

def add_row(year, pytorch, tensorFlow):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'Year'       : year, 
        'Pytorch'    : pytorch, 
        'Tensorflow' : tensorFlow
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()