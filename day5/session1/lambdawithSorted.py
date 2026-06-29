students=[
    ("aslaha",25),
    ("dinix",23),
    ("sussan",25),
]
sorted_student=sorted(
    students,
    key=lambda x:x[1]
    
)
print(sorted_student)