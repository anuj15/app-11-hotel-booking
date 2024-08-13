import pandas as pd

df = pd.read_csv(filepath_or_buffer='hotels.csv')
hotel_list = df.to_dict(orient='records')


def get_hotel_list():
    for hotels in hotel_list:
        print(hotels)


class Hotel:
    def __init__(self, h_id):
        self.h_id = h_id
        self.h_name = df.loc[df['id'] == self.h_id, 'name'].squeeze()

    def is_available(self):
        return df.loc[df['id'] == self.h_id, 'available'].squeeze() == 'yes'

    def book(self):
        df.loc[df['id'] == self.h_id, ['available']] = 'no'
        df.to_csv('hotels.csv', index=False)
