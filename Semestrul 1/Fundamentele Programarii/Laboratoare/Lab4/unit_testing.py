from datetime import datetime
from utils import fuzzy_search_destination
from package_manager import PackageManager
import os

def test_fuzzy_search():
    destinations = ["Paris", "London", "New York", "Tokyo", "Sydney"]

    assert fuzzy_search_destination("Paris", destinations) == "Paris"
    assert fuzzy_search_destination("Pari", destinations) == "Paris"
    assert fuzzy_search_destination("london", destinations) == "London"
    assert fuzzy_search_destination("Berlin", destinations) == None
    assert fuzzy_search_destination("", destinations) == None
    assert fuzzy_search_destination("Paris", []) == None


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
    manager.undo_api()
    assert offers[2].destination == "London"


    return manager

def test_package_removal(manager):
    manager.delete_api(lambda offer: offer.destination == "Craiova")
    offers = manager.get_offers()
    
    assert len(offers) == 7
    for offer in offers:
        assert offer.destination != "Craiova" 
   
    manager.undo_api()
    offers_after_undo = manager.get_offers()
    assert len(offers_after_undo) == 9

def test_search(manager):
    interval_results = manager.search_by_interval_api((datetime(2024, 5, 1), datetime(2024, 9, 1)))
    assert len(interval_results) == 5
    for offer in interval_results:
        assert offer.start_date <= datetime(2024, 9, 1)
        assert offer.end_date >= datetime(2024, 5, 1)


    dest_price_results = manager.search_by_destination_price_api("Grecia, Athena", 100)
    assert len(dest_price_results) == 1
    assert dest_price_results[0].destination == "Grecia, Athena"
    assert dest_price_results[0].price == 69.0


    end_date_results = manager.search_by_end_date_api(datetime(2024, 8, 12))
    assert len(end_date_results) == 3
    for offer in end_date_results:
        assert offer.end_date == datetime(2024, 8, 12)




def test_report(manager):
    offer_count_grecia = manager.report_offer_count_api("Grecia, Athena")
    assert offer_count_grecia == 2

    offer_count_craiova = manager.report_offer_count_api("Craiova")
    assert offer_count_craiova == 2

    offer_count_nonexistent = manager.report_offer_count_api("Narnia")
    assert offer_count_nonexistent == 0


    interval_packages = manager.report_packages_in_interval_api((datetime(2024, 5, 1), datetime(2024, 9, 1)))
    assert len(interval_packages) == 5
    for package in interval_packages:
        assert package.start_date >= datetime(2024, 5, 1)
        assert package.end_date <= datetime(2024, 9, 1)

    empty_interval_packages = manager.report_packages_in_interval_api((datetime(2025, 1, 1), datetime(2025, 12, 31)))
    assert len(empty_interval_packages) == 0


    assert manager.report_avg_price_api("Grecia, Athena") == 244.5 
    assert manager.report_avg_price_api("Craiova") == 84.5
    assert manager.report_avg_price_api("Narnia") == 0


def test_filter(manager):

    not_june_offers = manager.filter_by_month_api(6)
    assert len(not_june_offers) == 7 
    for offer in not_june_offers:
        assert not (offer.start_date.month <= 6 <= offer.end_date.month)

  
    not_august_offers = manager.filter_by_month_api(8)
    assert len(not_august_offers) == 5 
    for offer in not_august_offers:
        assert not (offer.start_date.month <= 8 <= offer.end_date.month)

    
    not_december_offers = manager.filter_by_month_api(12)
    assert len(not_december_offers) == 8 
    for offer in not_december_offers:
        assert not (offer.start_date.month <= 12 <= offer.end_date.month)


    not_october_offers = manager.filter_by_month_api(10)
    assert len(not_october_offers) == 9  


    manager.add_package_api(datetime(2024, 12, 20), datetime(2025, 2, 10), "Test ce trece prin an", 2000.0)
    not_january_offers = manager.filter_by_month_api(1)
    assert len(not_january_offers) == 9



def testing():
    test_fuzzy_search()
    manager = test_add_package()
    test_package_removal(manager)
    test_search(manager)
    test_report(manager)


testing()
os.system("cls")
