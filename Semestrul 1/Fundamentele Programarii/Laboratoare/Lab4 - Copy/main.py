
from console import run
from package_manager import PackageManager
import unit_testing
def main():
    package_manager = PackageManager()
    from datetime import datetime
    package_manager.add_package_api(datetime(2024, 1, 15), datetime(2024, 1, 25), "Rome", 1200.0)
    package_manager.add_package_api(datetime(2024, 2, 1), datetime(2024, 2, 7), "London", 800.0)
    package_manager.add_package_api(datetime(2024, 6, 16), datetime(2024, 6, 20), "Craiova", 100.0)
    package_manager.add_package_api(datetime(2024, 7, 2), datetime(2024, 7, 12), "Timisoara", 87.0)
    package_manager.add_package_api(datetime(2024, 5, 12), datetime(2024, 8, 12), "Cluj-Napoca", 420.0)
    package_manager.add_package_api(datetime(2024, 5, 12), datetime(2024, 9, 12), "Craiova", 69.0)
    package_manager.add_package_api(datetime(2024, 5, 12), datetime(2024, 8, 12), "Grecia, Athena", 420.0)
    package_manager.add_package_api(datetime(2024, 5, 4), datetime(2024, 8, 12), "Grecia, Athena", 69.0)
    run(package_manager)



if __name__ == "__main__":
    main()
