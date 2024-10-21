from datetime import datetime
from package_manager import PackageManager

def test_add_package():
    manager = PackageManager()
    
    start_date = datetime(2023, 12, 1)
    end_date = datetime(2023, 12, 10)
    destination = "Paris"
    price = 1000.0

    manager.add_package_api(start_date, end_date, destination, price)
    manager.add_package_api(datetime(2024, 1, 15), datetime(2024, 1, 25), "Rome", 1200.0)
    manager.add_package_api(datetime(2024, 2, 1), datetime(2024, 2, 7), "London", 800.0)
    manager.add_package_api(datetime(2024, 6, 16), datetime(2024, 6, 20), "Craiova", 100.0)
    manager.add_package_api(datetime(2024, 7, 2), datetime(2024, 7, 12), "Timisoara", 87.0)
    manager.add_package_api(datetime(2024, 5, 12), datetime(2024, 8, 12), "Cluj-Napoca", 420.0)
    manager.add_package_api(datetime(2024, 5, 12), datetime(2024, 9, 12), "Craiova", 69.0)
    manager.add_package_api(datetime(2024, 5, 12), datetime(2024, 8, 12), "Grecia, Athena", 420.0)
    manager.add_package_api(datetime(2024, 5, 4), datetime(2024, 8, 12), "Grecia, Athena", 69.0)

    offers = manager.get_offers()
    

    assert len(offers) == 9

    assert offers[0].start_date == start_date
    assert offers[0].end_date == end_date
    assert offers[0].price == price

    assert offers[1].destination == "Rome"
    manager.modify_package_api(2, datetime(2024, 2, 1), datetime(2024, 2, 7), "Madrid", 800.0)
    offers = manager.get_offers()
    assert offers[2].destination == "Madrid"
    manager.handle_undo()
    assert offers[2].destination == "London"


    return manager

def testing_package_removal(manager):
    manager.delete_api(lambda offer: offer.destination == "Craiova")
    offers = manager.get_offers()
    
    assert len(offers) == 7
    for offer in offers:
        assert offer.destination != "Craiova" 
   
    manager.handle_undo()
    offers_after_undo = manager.get_offers()
    assert len(offers_after_undo) == 9

def testing():
    manager = test_add_package()
    testing_package_removal(manager)

testing()
