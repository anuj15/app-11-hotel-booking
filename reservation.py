class ReservationTicket:
    def __init__(self, u_name, obj_hotel):
        self.u_name = u_name
        self.obj_hotel = obj_hotel

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking info:
        Name: {self.u_name}
        Hotel Name: {self.obj_hotel.h_name}
        """
        return content
