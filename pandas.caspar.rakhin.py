import pandas as pd

# Creating a sample DataFrame
data = { 'Name': [
    "John", "Emily", "Michael", "Sophia", "James", "Olivia", "William", "Ava", "Benjamin", "Isabella",
    "Alexander", "Charlotte", "Daniel", "Emma", "Christopher", "Harper", "Matthew", "Amelia", "Ethan", "Madison",
    "Andrew", "Abigail", "David", "Elizabeth", "Joshua", "Sofia", "Joseph", "Grace", "Samuel", "Victoria",
    "Ryan", "Chloe", "Jack", "Evelyn", "Christopher", "Natalie", "Liam", "Lily", "Mason", "Zoey",
    "Gabriel", "Anna", "Christian", "Lillian", "Logan", "Avery", "Gavin", "Addison", "Isaac", "Riley",
    "Dylan", "Zoey", "Cameron", "Madelyn", "Nathan", "Eleanor", "Isaac", "Layla", "Jackson", "Aria",
    "Cooper", "Penelope", "Jonathan", "Hannah", "Daniel", "Ariana", "Owen", "Audrey", "Dylan", "Scarlett",
    "Wyatt", "Leah", "Isaiah", "Brooklyn", "Dominic", "Maya", "Josiah", "Julia", "Eli", "Elena",
    "Adam", "Paisley", "Jason", "Clara", "Tyler", "Ellie", "Angel", "Adeline", "Cameron", "Serenity",
    "Cole", "Gabriella", "Jaxon", "Kaitlyn", "Julian", "Gabrielle", "Austin", "Maria", "Luke", "Lauren"
],
        'Age': [
    43, 36, 62, 24, 78, 52, 29, 42, 70, 68, 61, 35, 49, 57, 72, 38, 76, 23, 75, 46,
    79, 32, 55, 59, 30, 71, 33, 63, 69, 45, 31, 73, 77, 41, 60, 37, 48, 18, 74, 50,
    39, 58, 56, 65, 64, 40, 54, 25, 67, 66, 53, 21, 27, 19, 20, 44, 51, 22, 28, 26,
    47, 80, 34, 19, 79, 55, 41, 48, 53, 49, 54, 65, 66, 44, 37, 52, 27, 59, 70, 47,
    73, 30, 20, 31, 78, 69, 72, 38, 61, 71, 43, 68, 23, 42, 35, 39, 58, 74, 56, 25
],
        'City': [
    'London', 'Birmingham', 'Glasgow', 'Liverpool', 'Bristol', 'Manchester',
    'Sheffield', 'Leeds', 'Edinburgh', 'Leicester', 'Coventry', 'Bradford',
    'Cardiff', 'Belfast', 'Nottingham', 'Hull', 'Newcastle', 'Stoke',
    'Southampton', 'Derby', 'Portsmouth', 'Brighton', 'Plymouth',
    'Northampton', 'Reading', 'London', 'Birmingham', 'Glasgow', 'Liverpool', 'Bristol', 'Manchester',
    'Sheffield', 'Leeds', 'Edinburgh', 'Leicester', 'Coventry', 'Bradford',
    'Cardiff', 'Belfast', 'Nottingham', 'Hull', 'Newcastle', 'Stoke',
    'Southampton', 'Derby', 'Portsmouth', 'Brighton', 'Plymouth',
    'Northampton', 'Reading', 'London', 'Birmingham', 'Glasgow', 'Liverpool', 'Bristol', 'Manchester',
    'Sheffield', 'Leeds', 'Edinburgh', 'Leicester', 'Coventry', 'Bradford',
    'Cardiff', 'Belfast', 'Nottingham', 'Hull', 'Newcastle', 'Stoke',
    'Southampton', 'Derby', 'Portsmouth', 'Brighton', 'Plymouth',
    'Northampton', 'Reading', 'London', 'Birmingham', 'Glasgow', 'Liverpool', 'Bristol', 'Manchester',
    'Sheffield', 'Leeds', 'Edinburgh', 'Leicester', 'Coventry', 'Bradford',
    'Cardiff', 'Belfast', 'Nottingham', 'Hull', 'Newcastle', 'Stoke',
    'Southampton', 'Derby', 'Portsmouth', 'Brighton', 'Plymouth',
    'Northampton', 'Reading'
]}

df = pd.DataFrame(data, index= [
    'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ',
    'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT',
    'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BA', 'BB', 'BC', 'BD',
    'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN',
    'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX',
    'BY', 'BZ', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH',
    'CI', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR',
    'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DA', 'DB',
    'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ', 'DK', 'DL',
    'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV'
])  # Adding custom row indices

## Displaying the DataFrame
print("Original DataFrame:")
print(df)
print("\n")

print("Second Row of the Dataframe:")
print(df.iloc[1])
print("\n")## Task iloc 

print("Third Row, Second Column of the Dataframe:")
print(df.iloc[2,1])
print("\n")## Task iloc

print("selects the whole row of c:")
print(df.loc["CC"])
print("\n")

print("The name and city of row b and d ")
print(df.loc[["BB", "DD"], ["Name", "City"]])## Task loc
print("\n")

old_30 = df[df['Age']>= 30]## Conditional logic
print("These are people older or as old as 30:")
print(old_30)
print("\n")

young_20_and_bristol = df[(df['City'] == 'Bristol') & (df['Age'] <= 30)]## Multiple conditions
print("People who are younger than 20, or as old as 20 and live in Bristol:")
print(young_20_and_bristol)
print("\n")

names_and_cities_old_30 = df.loc[df['Age'] > 30, ['Name', 'City']]## Multiple conditions
print("Names and cities of people who are older than 30:")
print(names_and_cities_old_30)
print("\n")

print("The total age below:")
print(df['Age'].sum())## The total age
print("\n")

print("Average age below:")
print(df['Age'].mean())## The average age
print("\n")

# class Person:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city

# people = [Person("Caspar", 18, "Bristol"), Person]