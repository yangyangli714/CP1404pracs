from prac8.taxi import Taxi

prius = Taxi("Prius 1", 100)
prius.drive(40)
print(prius)
prius.start_fare()
prius.drive(100)
print(prius)
print(prius.get_fare())
