class ProgrammingLanguage:
    def __init__(self,name,Typing,Reflection,Year):
        self.name=name
        self.Typing=Typing
        self.Refelction=Reflection
        self.Year=Year

    def __str__(self):
        return "{}, Typing:{},Refelction:{},Year:{}".format(self.name,self.Typing,self.Refelction,self.Year)

    def is_dynamic(self):
        return self.Typing == "Dynamic"

def run_tests():
        ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
        python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
        visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
        languages = [ruby, python, visual_basic]
        print(python)
        print("The dynamically typed languages are:")
        for language in languages:
            if language.is_dynamic():
                print(language.name)

if __name__ == '__main__':
    run_tests()