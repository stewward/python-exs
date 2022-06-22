#create a mapping of each province to abbreviation 
provinces = {
    'Yukon': 'YT', 
    'Nunavut': 'NU',    
    'Prince Edward Island': 'PE',
    'Northwest Territories': 'NT', 
    'Alberta': 'AB',
    'British Columbia': 'BC'
}

#creates a basic set of provinces and some capital cities in them
capital_city = {
    'AB': 'Edmonton',
    'NT': 'Yellowknife',
    'BC': 'Victoria',
    'YT': 'Whitehorse'
}

#add some more capital cities 
capital_city['YT'] = 'Yukon'
capital_city ['NU'] = 'Nunavut'

#print out some cities 
print('-' * 10)
print("AB's captial city is: ", capital_city['AB'])
print("NT's captial city is: ", capital_city ['NT'])

#print some states
print('-' * 10)
print("Alberta's abbreviation is: ", provinces['Alberta'])
print("Nothwest Territories' abbrevation is: ", provinces['Northwest Territories'])

#do it by using the state then cities dict 
print('-' * 10)
print("British Columbia has: ", capital_city[provinces['British Columbia']])
print("Yukon has: ", capital_city[provinces['Yukon']])

#print every state abbreviation 
print('-' * 10)
for province, abbrev in list(provinces.items()):
    print(f"{province} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, capital_city in list(capital_city.items()):
    print(f"{abbrev} has the city {capital_city}")

#now do both at the same time 
print('-' * 10)
for province, abbrev in list(provinces.items()): 
    print(f"{province} province is abbreviated {abbrev}")
    print(f"and has city {capital_city[abbrev]}")

print('-' * 10)
#safely get an abbreviation by state that might not be there 
province = provinces.get('Quebec')

if not province:
    print("Sorry, no Quebec.")

#get a city with a default value 
capital_city = capital_city.get('QC', 'Does Not Exist')
print(f"The city for the province 'QC' is: {capital_city}")