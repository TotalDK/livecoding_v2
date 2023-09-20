import re

#pattern = r"\w" #\w = A..Z a..z 0..9 _
#pattern = r"\b\w{3}\b"
#pattern = r"[A-Z@,]"
#pattern = r"\w$"
#pattern = r"\w\$"
#pattern = r"\b.+\b"
#pattern = r"^[A-Z@,]+"
#pattern = r"[^a-z]+"
#pattern = r"na{3}"
#pattern = r"(?:na){3}"
#pattern = r"[^A-Za-z\d]+"
#pattern = r"\b\w{3,6}\b"
pattern = r"\b\w{3,}\b"

pattern = re.compile(pattern)
s = f"""LOrem ipsum dolor @
d sit amet ipsum, dddd ddd consectetur adipiscing elit.
Nunc volutpat convallis accum$san. Nam vel, finibus ex.
Fusce vitae mauris, nec sapien pr_%etium mattis suscipit in sapien.
Praesent pretium tortor eu naaaa massa malesuada nananananananana batman facilisis"""
print(re.findall(pattern, s))