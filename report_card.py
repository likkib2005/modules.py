import marks
name=input("Enter student name:")
marks_list=[]
for i in range(1,6):
   mark=int(input(f"Enter marks for subject{i}:"))
   marks_list.append(mark)
   total=marks.total_marks(marks_list)
   avg=marks.average_marks(marks_list)
   grade=marks.grade(avg)
   print("**************************")
   print(f"Name:{name}")
   print(f"marks:{marks_list}")
   print(f"Total:{total}")
   print(f"average:{avg:2f}")
   print(f"Grade:{grade}")
         

