#ques2:compute a person's income tax
#all values are in $s
gross_income=input("enter gross income=")
gross_income=float(gross_income)
standard_deduction=10000
dependents=input("enter no, of dependents=")
dependents=int(dependents)
#there is a $3000 deduction for each dependent
dependent_deduction=3000
#tax rate=20%
taxable_income=gross_income-standard_deduction-(dependent_deduction*dependents)
print("taxable income=",taxable_income)
tax=(taxable_income*20)/100
print("tax",tax)
