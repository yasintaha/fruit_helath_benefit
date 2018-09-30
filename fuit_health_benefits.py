# Fruit class starts here
class Fruits():
    # apple function declaration
    def apple(self):
        print("10 Impressive Health Benefits of Apples")
        print("""
                Calories: 95.
                Carbs: 25 grams.
                Fiber: 4 grams.
                Vitamin C: 14% of the RDI.
                Potassium: 6% of the RDI.
                Vitamin K: 5% of the RDI.
                Manganese, copper and vitamins A, E, B1, B2 and B6: Under 4% of the RDI.""")
    # banana function declaration
    def banana(self):
        print("Impressive Health Benefits of Banana's")
        print("""Vitamin B6 - 0.5 mg.
                 Manganese - 0.3 mg.
                 Vitamin C - 9 mg.
                 Potassium - 450 mg.
                 Dietary Fiber - 3g.
                 Protein - 1 g.
                 Magnesium - 34 mg.
                 Folate - 25.0 mcg""")

    # muskmelon function declaration
    def musk(self):
        print("Impressive Health Benefits of Muskmelon")
        print("""Beta Carotene. When it comes to beta carotene, cantaloupe knocks other yellow-orange fruits out of the park. ...
                Vitamin C. ...
                Folate. ...
                Water. ...
                Fiber. ...
                Potassium. ...
                Other Vitamins and Miner""")
     #beetroot function declaration
    def beet(self):
        print("Impressive Health Benefits of Beetroot")
        print("""
                calcium.
                iron.
                magnesium.
                manganese.
                phosphorous.
                sodium.
                zinc.
                copper.
                """)

    #pomogranet function declaration
    def pomo(self):
        print("Impressive Health Benefits of Pomograned")
        print("""
                Vitamin C. ...
                Cancer prevention. ...
                Alzheimer's disease protection. ...
                Digestion. ...
                Anti-inflammatory. ...
                Arthritis. ...
                Heart disease
                        """)
# fruit class ends here


# main function declaration
def main():
    while True:
            print("*The list of fruits and their benefits*")
            print("1.apple\n"
                "2.banana\n"
                "3.muskmelon\n"
                "4.beetroot\n"
                "5.pomograned")
            ask=int(input("Enter the fruit name choice-->\n"))
            if ask == 1:
                a=Fruits()
                a.apple()
            elif ask == 2:
                b=Fruits()
                b.banana()
            elif ask == 3:
                c=Fruits()
                c.musk()
            elif ask == 4:
                d=Fruits()
                d.beet()
            elif ask == 5:
                e=Fruits()
                e.pomo()
                break

            else:
                print("wrong choice")
                continue
# end of main() function declaration


#calling of main() function
if __name__== "__main__":
     main()
