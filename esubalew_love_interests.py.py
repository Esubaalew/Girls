from enum import Enum
from typing import List
# esubalew_love_interests.py
"""
PLEASE READ THIS!!
This is a sample Python code that demonstrates the usage of classes and methods to perform certain tasks related to love preferences. 
This code is for educational and entertainment purposes only and does not reflect the actual dating criteria of anyone, including Esubalew.

Classes:
- Person: A class that represents a person with a name and an age.
- Girl: A class that represents a girl, derived from Person class, with additional attributes such as height, education level, and hobbies.
- Esubalew: A class that represents Esubalew, derived from Person class, with additional attributes such as a list of girls and methods to perform certain tasks such as counting trouser-wearing girls and getting potential love interests.
- EducationLevel: An enumeration that represents the education level of a person.

Methods:
- check_if_lovable(): A method of the Girl class that returns True if a girl can be loved by Esubalew based on certain criteria, such as age, height, education level, and hobbies.
- count_loved_girls(): A method of the Esubalew class that returns the percentage of girls who can be loved by Esubalew in the list of girls.
- get_potential_love_interests(): A method of the Esubalew class that returns a list of potential love interests based on the criteria defined in check_if_lovable() method.

Variables:
- girl1, girl2, girl3, girl4 etc: Instances of the Girl class that represent different girls with different attributes.
- girls: A list that contains instances of the Girl class.
- esubalew: An instance of the Esubalew class that represents Esubalew.

This code is for educational and entertainment purposes only and does not reflect the actual dating criteria of anyone, including Esubalew.


This is a sample Python code that demonstrates the usage of classes and methods to perform certain tasks related to dating preferences. This code is for educational and entertainment purposes only and does not reflect the actual dating criteria of anyone, including Esubalew.

Classes:
- Person: A class that represents a person with a name and an age.
- Girl: A class that represents a girl, derived from Person class, with additional attributes such as height, education level, and hobbies.
- Esubalew: A class that represents Esubalew, derived from Person class, with additional attributes such as a list of girls and methods to perform certain tasks such as counting trouser-wearing girls and getting potential love interests.
- EducationLevel: An enumeration that represents the education level of a person.

Methods:
- check_if_lovable(): A method of the Girl class that returns True if a girl can be loved by Esubalew based on certain criteria, such as age, height, education level, and hobbies.
- count_trouser_wearing_girls(): A method of the Esubalew class that returns the percentage of girls who do not wear trousers in the list of girls.
- get_potential_love_interests(): A method of the Esubalew class that returns a list of potential love interests based on the criteria defined in check_if_lovable() method.

Variables:
- girl1, girl2, girl3, girl4: Instances of the Girl class that represent different girls with different attributes.
- girls: A list that contains instances of the Girl class.
- esubalew: An instance of the Esubalew class that represents Esubalew.

This code is for educational and entertainment purposes only and does not reflect the actual dating criteria of anyone, including Esubalew.

"""


class Person:
    """
    A class representing a person with a name and an age.

    Attributes:
    - name (str): The name of the person.
    - age (int): The age of the person.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Girl(Person):
    """
    A subclass of Person representing a girl with additional attributes.

    Attributes:
    - name (str): The name of the girl.
    - age (int): The age of the girl.
    - wears_trouser (bool): True if the girl wears trousers, False otherwise.
    - hair_color (str): The color of the girl's hair.
    - skin_color (str): The color of the girl's skin.
    - height (int): The height of the girl in centimeters.
    - education_level (EducationLevel): The girl's level of education.
    - hobbies (List[str]): A list of the girl's hobbies.
    - can_be_loved_by_esubalew (bool): True if the girl is a potential love interest for Esubalew, False otherwise.

    Methods:
    - check_if_lovable() -> bool:
        Determines if the girl is a potential love interest for Esubalew based on certain criteria.
    """

    def __init__(self, name: str, age: int, wears_trouser: bool, hair_color: str, skin_color: str, height: int,
                 education_level: 'EducationLevel', hobbies: List[str]):
        super().__init__(name, age)
        self.wears_trouser = wears_trouser
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.height = height
        self.education_level = education_level
        self.hobbies = hobbies
        self.can_be_loved_by_esubalew = self.check_if_lovable()

    def check_if_lovable(self) -> bool:
        if self.age < 16:
            return False
        if self.age > Esubalew.age - 4:
            return False
        if self.wears_trouser:
            return False
        if self.skin_color == 'Ethiopian':
            if self.height >= 160 and self.education_level.is_completed(EducationLevel.HIGH_SCHOOL):
                if 'reading' in self.hobbies and 'music' not in self.hobbies:
                    return True
        return False


class Esubalew:
    """
    A class representing a person named Esubalew with a list of girls.

    Attributes:
    - girls (List[Girl]): A list of Girl objects.

    Methods:
    - count_loved_girls() -> str:
        Returns the percentage of girls who are not wearing trousers as str.
    - get_potential_love_interests() -> List[Girl]:
        Returns a list of girls who are potential love interests for Esubalew based on certain criteria.
    """
    age = 21

    def __init__(self, girls: List[Girl]):
        self.girls = girls

    def count_loved_girls(self) -> str:
        loved_girls = [
            girl for girl in self.girls if girl.can_be_loved_by_esubalew]

        return f'{((len(loved_girls) / len(self.girls)) * 100):.2f} %'

    def get_potential_love_interests(self) -> List[Girl]:
        return [girl.name for girl in self.girls if girl.can_be_loved_by_esubalew]


class EducationLevel(Enum):
    """
    An enumeration representing different levels of education.

    Attributes:
    - HIGH_SCHOOL: The high school education level.
    - ASSOCIATE_DEGREE: The associate degree education level.
    - BACHELOR_DEGREE: The bachelor degree education level.
    - MASTER_DEGREE: The master degree education level.
    - DOCTORATE_DEGREE: The doctorate degree education level.

    Methods:
    - is_completed(current_level: 'EducationLevel') -> bool:
        Determines if the current education level is at least the level represented by this enumeration.
    """
    HIGH_SCHOOL = 1
    ASSOCIATE_DEGREE = 2
    BACHELOR_DEGREE = 3
    MASTER_DEGREE = 4
    DOCTORATE_DEGREE = 5

    def is_completed(self, current_level: 'EducationLevel') -> bool:
        return current_level.value >= self.value


def main():
    """The main function that creates instances of the Girl class and calls the methods of the Esubalew class.
    This function creates four instances of the Girl class with different attributes and stores them in a list. It then
    creates an instance of the Esubalew class by passing the list of girls as an argument. Finally, it calls two methods
    of the Esubalew class: count_trouser_wearing_girls() and get_potential_love_interests(), and prints their output.
    """
    girl1: Girl = Girl("Misrak", 17, False, "black",
                       "Ethiopian", 170, EducationLevel.HIGH_SCHOOL, ["reading"])
    girl2: Girl = Girl("Martha", 19, True, "brown", "Kenyan",
                       160, EducationLevel.BACHELOR_DEGREE, ["music", "reading"])
    girl3: Girl = Girl("Yeshimebet", 20, True, "black",
                       "Ethiopian", 165, EducationLevel.HIGH_SCHOOL, ["sports", "reading"])
    girl4: Girl = Girl("Tiruwork", 19, False, "black",
                       "Tanzanian", 180, EducationLevel.MASTER_DEGREE, ["reading"])
    girl5: Girl = Girl("Birtukan", 17, False, "black",
                       "Ethiopian", 70, EducationLevel.DOCTORATE_DEGREE, ["reading", "swwimming"])
    girl6: Girl = Girl("Makeda", 31, True, "brown", "Kenyan",
                       160, EducationLevel.BACHELOR_DEGREE, ["music", "reading"])
    girl7: Girl = Girl("Tsion", 20, True, "black",
                       "Ethiopian", 165, EducationLevel.HIGH_SCHOOL, ["sports", "reading"])
    girl8: Girl = Girl("Tsion", 19, False, "black",
                       "Tanzanian", 180, EducationLevel.MASTER_DEGREE, ["reading"])
    girl9: Girl = Girl("Almaz", 17, False, "black",
                       "Ethiopian", 170, EducationLevel.HIGH_SCHOOL, ["reading"])
    girl10: Girl = Girl("Rahel", 19, True, "brown", "Kenyan",
                        160, EducationLevel.BACHELOR_DEGREE, ["music", "reading"])
    girl11: Girl = Girl("Liya", 20, True, "black",
                        "Ethiopian", 165, EducationLevel.HIGH_SCHOOL, ["sports", "reading"])
    girl12: Girl = Girl("Aida", 19, False, "black",
                        "Tanzanian", 180, EducationLevel.MASTER_DEGREE, ["reading"])
    girls = [girl1, girl2, girl3, girl4, girl5, girl6,
             girl7, girl8, girl9, girl10, girl11, girl12]
    esubalew = Esubalew(girls)

    print(esubalew.count_loved_girls())
    print(esubalew.get_potential_love_interests())


if __name__ == "__main__":
    main()
