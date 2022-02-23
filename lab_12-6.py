#author: LM (AMDG) 2/23/22
#dictionary with assignment and grades
gradesdictionary = {'endS1labs': 100, 'startS2labs': 100, 'cycle11labs': 0, 'midyearproposal': 100}
#prints keys
gradesdictionary.values()
#prints key using loop
for k in gradesdictionary:
    print(k)
# prints grade and assignment on anythoing above than a 70
for k, v in gradesdictionary.items():
    if v > 70:
        print(k,v)
# prints grade and assignment on anythoing below 50
for k, v in gradesdictionary.items():
    if v < 50:
        print(k,v)
