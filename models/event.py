class Event():
    def __init__(self, date, event_name, no_guests, room_location, description, recurring):
        self.date = date
        self.event_name = event_name
        self.no_guests = no_guests
        self.room_location = room_location
        self.description = description
        self.recurring = recurring