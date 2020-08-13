temps=[222,235,151,987,-222]
new_temps=[temp/10 for temp in temps if temp > 0]
print(new_temps)
#but if i want to replace it by something else
new_temps=[temp/10 if temp > 0 else 0 for temp in temps]
print(new_temps)
