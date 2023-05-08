def party_brth(guest_name, venue="Hotel Ramada", day="21-July", timings="18:30",hostname="Cosmina"):
  print(f'''Dear {guest_name},
        Please come to my birthday party
        Venue- {venue}
        Date-{day}
        Time-{timings}
      {hostname}
      ************************************
        ''')


your_guests = input("Enter your guests separated by comma...")
guest_list = your_guests.split(",")


for guest in guest_list:
  party_brth(guest)

