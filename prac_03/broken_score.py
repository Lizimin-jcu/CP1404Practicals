import random
def main():
    score = float(input("Enter score: "))
    grade=get_score(score)
    print(grade)
    num=random.randint(0, 101)
    print(f"{num} is {get_grade(num)}")



def get_score(score):
    if score < 0 or score>100:
        print("Invalid score")
    elif score >=90 :
        print(f"{score} is excellent")
    elif score >= 50:
        print(f"{score} is Pass")
    elif score <50:
        print(f"{score} is Bad")

def get_grade(num):
    if num >=90 :
        print("excellent")
    elif num >= 50:
        print("Pass")
    elif num <50:
        print("Bad")


main()


