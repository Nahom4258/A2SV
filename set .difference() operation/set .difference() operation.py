# Input
# 1st line - no of students subscribed to English
# 2nd line - space separated list of stud. roll nos. subscribed to English
# 3rd line - no of students subscribed to French
# 4th line - space separated list of stud. roll nos. subscribed to French

# accept all inputs
no_eng = int(input())
eng_subs = set(input().split())
no_french = int(input())
fre_subs = set(input().split())

# print the length of the difference
print(len(eng_subs.difference(fre_subs)))
