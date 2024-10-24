import os
from console import run
from package_manager import PackageManager
import unit_testing
def main():
    os.system("cls")
    package_manager = PackageManager()
    run(package_manager)



if __name__ == "__main__":
    main()
