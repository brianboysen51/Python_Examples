#Q1 - 

gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []

for x in country:
    try:
        country_gold.append(gold[x])
    except Exception as e:
        country_gold.append("Did not get gold")
        
print(country_gold)

#Q2 - 

di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, 
      {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except Exception as e:
        print("Error")
print("Total number of puppies:", total)

#Q3 - 
numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
remainder = []
for num in numb:
    try:
        rem=36%num
        remainder.append(rem)
    except Exception as e:
        remainder.append("Error")
        print('Error')
print(remainder)

#Q4 - 

lst = [2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,465,56,7,3,43,23]
lst_three = []
for num in lst:
    try:
        if 3 % num == 0:
            lst_three.append(num)
    except ZeroDivisionError:
        print("Error")
print(lst_three)

#Q5 - 
full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']
attempt = []
for elem in full_lst:
    try:
        attempt.append(elem[1])
    except Exception as e:
        attempt.append("Error")
        print('error')
print(attempt)

#Q6 - 
conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'], ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'], 
         ['Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'], ['Australia'], ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'], ['Antarctica']]
third_countries = []
for c in conts:
    try:
        third_countries.append(c[2])
    except Exception as e:
        third_countries.append("Continent does not have 3 countries")
        print('error')
print(third_countries)

#Q7 - 

sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]
ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}
for x in sport:
    try:
        print(ppl_play[x])
    except Exception as e:
        ppl_play[x]=1
        print('error')
print(ppl_play)

#Q8 - 
di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, 
      {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except Exception as e:
        diction["Puppies"]=0
        print('error')
print("Total number of puppies:", total)




