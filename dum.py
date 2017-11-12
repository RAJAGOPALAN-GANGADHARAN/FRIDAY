import re
s=input()
p=str(len(s))
str1='[QWERTYUIOP]'
str2='[ASDFGHJKL]'
str3='[ZXCVBNM]'
str4=str1+'|'+str2+'|'+str3+'{'+p+'}'
if re.match(str4,s):
	print('Yes')
else:
	print('No')