def is_year_leap(год):
   if год % 4 == 0:
       print("год " + str(год) + ": True")
   else:
       print("год " + str(год) + ": False")

is_year_leap (int(input("год")))