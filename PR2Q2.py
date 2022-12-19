#implimentiong * quantifier
import re
pattern=re.compile("th[abc]?")
result=pattern.match("thesaurus")
if result==None:
    print(" no match")
else:
    print("match")
