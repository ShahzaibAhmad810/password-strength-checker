import re
def analyze_password(password):
    issues = list()
    score = 0
    # length
    if len(password) < 8:
        issues.append("password must be at least 8 character long. ")
    else:
        score += 1
    # uppercase
    if not re.search(r"[A-Z]",password):
       issues.append("Add at least one capital letter(A-Z).")
    else: 
        score += 1
    # lowercase
    if not re.search(r"[a-z]",password):
        issues.append("Add at least one lowercase letter(a-z). ")
    else:
        score += 1
    # number
    if not re.search(r"[0-9]",password):
        issues.append("add least one number(0-9). ")
    else:
        score += 1
    if not re.search(r"[@#$?*!]",password):
        issues.append("add at least one special character (@,$,#,!,?,&)")
    else:
       score +=1
    # Adjust score 0-4 
    if score > 4:
        score =4 
    return issues, score


    