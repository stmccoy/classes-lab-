class Student: 

    def __init__(self, name: str, cohort: str):
        self.name = name
        self.cohort = cohort
    
    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, language):
        return f"I love {language}"