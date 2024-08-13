from hotel import Hotel, get_hotel_list
from reservation import ReservationTicket

get_hotel_list()
hotel_id = int(input('Enter the hotel id: '))
hotel = Hotel(hotel_id)
if hotel.is_available():
    user_name = input('Enter your name: ')
    hotel.book()
    rt = ReservationTicket(user_name, hotel)
    receipt = rt.generate()
    print(receipt)
else:
    print('cannot book. room not available')
