# ----------------------------------------------------------
# Author : Joshua Parker
# Date   : July 6, 2025
# Purpose: Demonstrate a simple **Flower** class with one
#          ATTRIBUTE (*name*) and two METHODS (*grow*, *bloom*).
#          The script instantiates three Flower objects and
#          calls their methods to illustrate basic OOP concepts.
# ----------------------------------------------------------

class Flower:                          # CLASS definition (blueprint for flowers)
    def __init__(self, name):         # CONSTRUCTOR METHOD – runs automatically on instantiation
        self.name = name              # ATTRIBUTE → holds the specific flower's name

    def grow(self):                   # METHOD → describes the flower growing
        print(f"The {self.name} is growing.")   # Action performed when grow() is called

    def bloom(self):                  # METHOD → describes the flower blooming
        print(f"The {self.name} is blooming.")  # Action performed when bloom() is called


def main():                           # Main function – program execution starts here
    flower1 = Flower("Rose")          # Instantiate first Flower object with name "Rose"
    flower1.grow()                    # Call grow() on flower1
    flower1.bloom()                   # Call bloom() on flower1

    flower2 = Flower("Daisy")         # Instantiate second Flower object with name "Daisy"
    flower2.grow()                    # Call grow() on flower2
    flower2.bloom()                   # Call bloom() on flower2

    flower3 = Flower("Tulip")         # Instantiate third Flower object with name "Tulip"  ← NEW FLOWER
    flower3.grow()                    # Call grow() on flower3
    flower3.bloom()                   # Call bloom() on flower3


if __name__ == "__main__":            # Ensures main() runs only when script is executed directly
    main()                            # Invoke the main function
