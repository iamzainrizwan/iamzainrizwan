from datetime import date
from calendar import monthrange
import re

birthday = date(2006, 11, 14)
today = date.today()

years = today.year - birthday.year
months = today.month - birthday.month
days = today.day - birthday.day

if days < 0:
    prev_month = today.month -1 if today.month > 1 else 12
    prev_year = today.year if today.month > 1 else today.year - 1
    days += monthrange(prev_year, prev_month)[1]
    months -= 1

if months < 0:
    years -= 1
    months += 12

uptime_str = f"{years} years, {months} months, {days} days"

with open("README.md", "r") as f:
    content = f.read()

update = re.sub(r'(\$uptime\n)[^\n]*', rf'\g<1>{uptime_str}', content)
print(repr(content[:200]))

with open("README.md", "w") as f:
    f.write(update)

print(f"new uptime: {uptime_str}")
