def namer(prompt):
    grades=['A','B','C','D','F']
    grade=input(prompt)
    grade=grade.upper()

    if grade in grades:
        return grade 
    else:
      return namer(prompt)
kal=namer("Enter grade: ")
print(kal)