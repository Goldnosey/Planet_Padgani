import json

path = 'data/data.json'
def getyear(loaded_data):

    year = [i for i in loaded_data if i.startswith('year')]

    if year:
            cleaned_year = year[-1][len('year'):]
            cleaned_year = float(cleaned_year)
            if cleaned_year > -3001 and cleaned_year < -1999:
                    base_support_fascism = 0.0
                    base_support_democracy = 5.0
                    base_support_dictatorship = 15.0
                    base_support_oligarchy = 30.0
                    base_support_monarchy = 50.0
            elif cleaned_year > -2000 and cleaned_year < -999:
                    base_support_monarchy = 60.0
                    base_support_democracy = 5.0
                    base_support_oligarchy = 20.0
                    base_support_dictatorship = 15.0
                    base_support_fascism = 0.0
            elif cleaned_year > -1000 and cleaned_year < -499:
                    base_support_democracy = 17.0
                    base_support_monarchy = 50.0
                    base_support_oligarchy = 21.0
                    base_support_dictatorship = 12.0
                    base_support_fascism = 0.0
            elif cleaned_year > -500 and cleaned_year < 1:
                    base_support_democracy = 10.0
                    base_support_dictatorship = 20.0
                    base_support_fascism = 0.0
                    base_support_monarchy = 60.0
                    base_support_oligarchy = 10.0
            elif cleaned_year > 1 and cleaned_year < 501:
                    base_support_oligarchy = 5.0
                    base_support_democracy = 5.0
                    base_support_dictatorship = 20.0
                    base_support_monarchy = 70.0
                    base_support_fascism = 0.0
            elif cleaned_year > 500 and cleaned_year < 1001:
                    base_support_fascism = 0.0
                    base_support_democracy = 5.0
                    base_support_monarchy = 80.0
                    base_support_oligarchy = 10.0
                    base_support_dictatorship = 5.0
            elif cleaned_year > 1000 and cleaned_year < 1501:
                    base_support_monarchy = 75.0
                    base_support_oligarchy = 10.0
                    base_support_dictatorship = 10.0
                    base_support_democracy = 5.0
                    base_support_fascism = 0.0
            elif cleaned_year > 1500 and cleaned_year < 1751:
                    base_support_monarchy = 70.0
                    base_support_oligarchy = 10.0
                    base_support_dictatorship = 10.0
                    base_support_democracy = 10.0
                    base_support_fascism = 0.0
            elif cleaned_year > 1750 and cleaned_year < 1801:
                    base_support_monarchy = 60.0
                    base_support_oligarchy = 10.0
                    base_support_dictatorship = 10.0
                    base_support_democracy = 20.0
                    base_support_fascism = 0.0
            elif cleaned_year > 1800 and cleaned_year < 1851:
                    base_support_monarchy = 50.0
                    base_support_oligarchy = 10.0
                    base_support_dictatorship = 10.0
                    base_support_democracy = 30.0
                    base_support_fascism = 0.0
            elif cleaned_year > 1850 and cleaned_year < 1901:
                    base_support_monarchy = 40.0
                    base_support_oligarchy = 10.0
                    base_support_dictatorship = 10.0
                    base_support_democracy = 40.0
                    base_support_fascism = 0.0
            elif cleaned_year > 1900 and cleaned_year < 1921:
                    base_support_monarchy = 15.0
                    base_support_oligarchy = 10.0
                    base_support_dictatorship = 20.0
                    base_support_democracy = 50.0
                    base_support_fascism = 5.0
            elif cleaned_year > 1920 and cleaned_year < 1941:
                    base_support_monarchy = 10.0
                    base_support_oligarchy = 10.0
                    base_support_dictatorship = 30.0
                    base_support_democracy = 25.0
                    base_support_fascism = 25.0
            elif cleaned_year > 1940 and cleaned_year < 1961:
                    base_support_monarchy = 5.0
                    base_support_oligarchy = 10.0
                    base_support_dictatorship = 35.0
                    base_support_democracy = 45.0
                    base_support_fascism = 5.0
            elif cleaned_year > 1960 and cleaned_year < 1981:
                    base_support_monarchy = 5.0
                    base_support_oligarchy = 10.0
                    base_support_dictatorship = 40.0
                    base_support_democracy = 45.0
                    base_support_fascism = 0.0
            elif cleaned_year > 1980 and cleaned_year < 2001:
                    base_support_monarchy = 5.0
                    base_support_oligarchy = 15.0
                    base_support_dictatorship = 20.0
                    base_support_democracy = 60.0
                    base_support_fascism = 0.0
            elif cleaned_year > 2000 and cleaned_year < 2021:
                    base_support_monarchy = 5.0
                    base_support_oligarchy = 20.0
                    base_support_dictatorship = 30.0
                    base_support_democracy = 45.0
                    base_support_fascism = 0.0
    else:
            cleaned_year = -3000
            base_support_fascism = 0.0
            base_support_democracy = 5.0
            base_support_dictatorship = 15.0
            base_support_oligarchy = 30.0
            base_support_monarchy = 50.0
            loaded_data.append('year-3000')
            with open(path, 'w') as f:
                    json.dump(loaded_data, f)

    support = [base_support_monarchy, base_support_oligarchy, base_support_dictatorship, base_support_democracy, base_support_fascism]
    return support
