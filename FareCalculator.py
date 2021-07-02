ride_type = "Black"
credits = 4

ride_price = 0
final_price = 0

if ride_type == "CarX":
  ride_price = 200 
elif ride_type == "Black":
  ride_price = 398
else:
  ride_price = 187

print("Ride price:")
print(ride_price)

if credits > 0:
  final_price = ride_price - credits

print("Final price:")
print(final_price)
