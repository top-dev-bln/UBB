import sys
import os
from datetime import datetime

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.utils import fuzzy_search_destination
from domain.package_manager import create_manager, add_package_api, modify_package_api, delete_api
from domain.package_manager import search_by_interval_api, search_by_destination_price_api, search_by_end_date_api
from domain.package_manager import report_offer_count_api, report_packages_in_interval_api, report_avg_price_api
from domain.package_manager import filter_by_month_api, undo_api

def test_fuzzy_search():

    assert fuzzy_search_destination("Paris", ["Paris", "London"]) == "Paris"
    assert fuzzy_search_destination("London", ["Paris", "London"]) == "London"

    assert fuzzy_search_destination("paris", ["Paris", "London"]) == "Paris"
    assert fuzzy_search_destination("LONDON", ["Paris", "London"]) == "London"
    

    assert fuzzy_search_destination("Lon", ["Paris", "London"]) == "London"
    assert fuzzy_search_destination("Pari", ["Paris", "London"]) == "Paris"
    

    assert fuzzy_search_destination("Berlin", ["Paris", "London"]) is None
    assert fuzzy_search_destination("", ["Paris", "London"]) is None
    assert fuzzy_search_destination("Paris", []) is None

def create_test_data():
    manager = create_manager()
    def get_destinations(manager):
        return [offer["destination"] for offer in manager["offers"]]
    

    test_packages = [
        (datetime(2024, 1, 1), datetime(2024, 1, 10), "Paris", 1000),
        (datetime(2024, 2, 1), datetime(2024, 2, 10), "London", 1200),
        (datetime(2024, 3, 1), datetime(2024, 3, 10), "Rome", 800),
        (datetime(2024, 6, 1), datetime(2024, 8, 31), "Athens", 1500),  
        (datetime(2024, 12, 25), datetime(2025, 1, 5), "Alps", 2000)    
    ]
    
    for start, end, dest, price in test_packages:
        add_package_api(manager, start, end, dest, price)

    dest_list = get_destinations(manager)
    assert len(dest_list) == 5
    assert "Paris" in dest_list
    assert "London" in dest_list
    assert "Rome" in dest_list
    assert "Athens" in dest_list
    assert "Alps" in dest_list

    
    return manager

def test_basic_operations():
    manager = create_test_data()
    def get_destinations(manager):
        return [offer["destination"] for offer in manager["offers"]]
    def get_prices(manager):
        return [offer["price"] for offer in manager["offers"]]
    

    assert len(manager["offers"]) == 5
    

    add_package_api(manager, datetime(2024, 4, 1), datetime(2024, 4, 10), "Madrid", 900)
    dest_list = get_destinations(manager)
    assert "Madrid" in dest_list
    

    modify_package_api(manager, 0, datetime(2024, 1, 1), datetime(2024, 1, 10), "Paris", 1100)
    price_list = get_prices(manager)
    assert 1100 in price_list
    

    deleted_count = delete_api(manager, lambda x: x["price"] > 1500)
    assert deleted_count == 1
    dest_list = get_destinations(manager)
    assert len(dest_list) == 5

def test_search_functions():
    manager = create_test_data()
    

    interval_results = search_by_interval_api(manager, 
        (datetime(2024, 1, 1), datetime(2024, 3, 31)))
    assert len(interval_results) == 3
    
  
    price_results = search_by_destination_price_api(manager, "Paris", 1500)
    assert len(price_results) == 1
    assert price_results[0]["destination"] == "Paris"
    

    end_results = search_by_end_date_api(manager, datetime(2024, 1, 10))
    assert len(end_results) == 1
    assert end_results[0]["destination"] == "Paris"

def test_report_functions():
    manager = create_test_data()
    
 
    assert report_offer_count_api(manager, "Paris") == 1
    assert report_offer_count_api(manager, "NonExistent") == 0
    
   

    interval_packages = report_packages_in_interval_api(manager,
        (datetime(2024, 1, 1), datetime(2024, 12, 31)))
    assert len(interval_packages) == 5
    assert interval_packages[0]["price"] <= interval_packages[-1]["price"]  # Check sorting
    

    assert report_avg_price_api(manager, "Paris") == 1000
    assert report_avg_price_api(manager, "NonExistent") == 0

def test_filter_functions():
    manager = create_test_data()
    
 
    june_filtered = filter_by_month_api(manager, 6)
    assert len(june_filtered) == 4  
    
    january_filtered = filter_by_month_api(manager, 1)
    assert len(january_filtered) == 3  

def test_undo():
    manager = create_test_data()
    initial_count = len(manager["offers"])

    add_package_api(manager, datetime(2024, 4, 1), datetime(2024, 4, 10), "Madrid", 900)
    undo_api(manager)
    assert len(manager["offers"]) == initial_count

    original_price = manager["offers"][0]["price"]
    modify_package_api(manager, 0, datetime(2024, 1, 1), datetime(2024, 1, 10), "Paris", 1100)
    undo_api(manager)
    assert manager["offers"][0]["price"] == original_price
    
   
    delete_api(manager, lambda x: x["destination"] == "Paris")
    undo_api(manager)
    assert len(manager["offers"]) == initial_count
    assert any(offer["destination"] == "Paris" for offer in manager["offers"])

def run_all_tests():
    test_fuzzy_search()
    test_basic_operations()
    test_search_functions()
    test_report_functions()
    test_filter_functions()
    test_undo()
    print("All tests passed successfully!")

if __name__ == "__main__":
    run_all_tests()
    os.system("cls")
