# Enter your code here. Read input from STDIN. Print output to STDOUT

# accept inputs
no_eng = int(input())
eng_subs = set(input().split())
no_french = int(input())
fre_subs = set(input().split())

print(len(eng_subs.union(fre_subs)))
