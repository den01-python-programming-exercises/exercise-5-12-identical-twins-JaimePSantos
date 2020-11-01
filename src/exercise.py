# from person import Person
# from simple_date import SimpleDate
def main():
  date = SimpleDate(24, 3, 2017)
  date2 = SimpleDate(23, 7, 2017)

  leo = Person("Leo", date, 62, 9)
  leo1 = Person("Leo", date, 62, 9)
  lily = Person("Lily", date2, 65, 8)

  if (leo == lily):
      print("Is this quite correct?")

  leo_with_different_weight = Person("Leo", date, 62, 10)

  if (leo == leo_with_different_weight):
      print("Is this quite correct?")
  print(leo==leo1)

if __name__ == '__main__':
  main()
  from person import Person
  from simple_date import SimpleDate
else:
  from src.person import Person
  from src.simple_date import SimpleDate