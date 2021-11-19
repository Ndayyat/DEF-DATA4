
def resu(int_homework, int_assessment, int_finalexam):
    answer = (int(int_homework) + int(int_assessment) + int(int_finalexam)) /175 *100 
    return answer


name = str(input("enter your name"))
homework = 26
while homework > 25 :
   homework = float(input("enter your homewrk score"))
   if homework > 25 or homework < 0:
       print("not avlid score, try again")

assessment = 51
while assessment > 50 :
    assessment = float(input("enter your assessment score"))
    if assessment > 50 or assessment < 0:
      print("invalid score, try again")

finalexam = 101
while finalexam > 100 :
    finalexam = float(input("enter your final exam score"))
    if finalexam > 100 or finalexam < 0:
        print("invalid score, try again")

grade = resu(homework, assessment, finalexam)
print(grade)