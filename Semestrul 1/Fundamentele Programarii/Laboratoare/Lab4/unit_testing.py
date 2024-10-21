from datetime import datetime
from package_manager import PackageManager

def test_add_package():
    manager = PackageManager()
    
    start_date = datetime(2023, 12, 1)
    end_date = datetime(2023, 12, 10)
    destination = "Paris"
    price = 1000.0

    manager.add_package(start_date, end_date, destination, price)
    manager.add_package(datetime(2024, 1, 15), datetime(2024, 1, 25), "Rome", 1200.0)
    manager.add_package(datetime(2024, 2, 1), datetime(2024, 2, 7), "London", 800.0)

    offers = manager.get_offers()
    

    assert len(offers) == 3

    assert offers[0].start_date == start_date
    assert offers[0].end_date == end_date
    assert offers[0].destination == destination
    assert offers[0].price == price

    assert offers[1].destination == "Rome"
    manager.modify_package_api(2, datetime(2024, 2, 1), datetime(2024, 2, 7), "Madrid", 800.0)
    offers = manager.get_offers()
    assert offers[2].destination == "Madrid"
    manager.handle_undo()
    assert offers[2].destination == "London"


    return manager

def testing_package_removal(manager):
    pass
   

def testing():
    manager = test_add_package()
    testing_package_removal(manager)

testing()
