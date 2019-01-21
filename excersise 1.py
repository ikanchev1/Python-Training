#hour in minutes
hour = 60
#acad. hour in minutes
akad_hour = 40
#break minutes
brk = 20
#acad. hours between breaks
interval = 4
#overal acad. hours
overal = 64

#how many breaks in overal acad. hours
breaks = (overal/interval)

#calc all breaks in minutes
break_min = breaks*20

#calc astronomical hours
print(((overal*akad_hour)+break_min)/hour)
