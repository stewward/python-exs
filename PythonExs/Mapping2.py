#create a mapping of province to abbreviation 
provinces = {
    'Yukon': 'YT', 
    'Nunavut': 'NU',    
    'Prince Edward Island': 'PE',
    'Northwest Territories': 'NT', 
    'Alberta': 'AB',
    'British Columbia': 'BC'
}

#creates a basic set of states and some cities in them
capital = {
    'YT': 'Whitehorse',
    'NU': 'Iqaluit',
    'PE': 'Charlottetown'
}

#add some more cities 
capital['BC'] = 'Victoria'
capital ['AB'] = 'Edmonton'
capital ['NT'] = 'Yellowknife'

#print out some cities 
print('-' * 10)
print("BC Province has: ", capital['BC'])
print("AB Province has: ", capital ['AB'])

#print some provinces
print('-' * 10)
print("Prince Edward Island abbreviation is: ", provinces['Prince Edward Island'])
print("Northwest Territories abbrevation is: ", provinces['Northwest Territories'])

#do it by using the province then cities dict 
print('-' * 10)
print("Yukon has: ", capital[provinces['Yukon']])
print("Prince Edward Island has: ", capital[provinces['Prince Edward Island']])

#print every province abbreviation 
print('-' * 10)
for province, abbrev in list(provinces.items()):
    print(f"{province} is abbreviated {abbrev}")

#print every city in province
print('-' * 10)
for abbrev, city in list(capital.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time 
print('-' * 10)
for province, abbrev in list(provinces.items()): 
    print(f"{province} province is abbreviated {abbrev}")
    print(f"and has city {capital[abbrev]}")

print('-' * 10)
#safely get an abbreviation by province that might not be there 
province = provinces.get('Quebec')

if not province:
    print("Sorry, no Quebec.")

#get a city with a default value 
city = capital.get('QC', 'Does Not Exist')
print(f"The city for the province 'QC' is: {city}")