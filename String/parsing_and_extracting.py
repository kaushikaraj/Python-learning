data = 'From kaushik.ashutosh@ac.in sat jan 04'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)
