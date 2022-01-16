# idk what im doing 
# code to match people to roommates given an apartment and other people that have liked said apartment
#import questionnaire_script

#user Class to give attributes such as age, sex, and delimiting factors
class User:
  def personal(self, name, age, sex, personal_traits):
    self.name = name
    self.age = age
    self.sex = sex


  def pref(self, personal_traits, wanted_traits, age_pref, sex_pref):
    self.personal_traits = personal_traits
    self.wanted_traits = wanted_traits
    self.age_pref = age_pref
    self.sex_pref = sex_pref
  #im trying something dw


  def get_age(self):
    return self.age

  def get_sex(self):
    return self.age

  def get_personal_traits(self):
    return self.personal_traits

  def get_wanted_traits(self):
    return self.wanted_traits



# fake values below to fill up table
'''
apartment1 = 1
apartment2 = 2
apartment3 = 3

name1 = 'meadow'
name2 = 'callie'
name3 = 'lauren'
'''
#cursor.execute('''INSERT INTO apartment_likes(apartment, name) VALUES(?,?)''', apartment1, name1)
#cursor.execute('''INSERT INTO apartment_likes(apartment, name) VALUES(?,?)''', apartment2, name2)
#cursor.execute('''INSERT INTO apartment_likes(apartment, name) VALUES(?,?)''', apartment3, name3)


def get_likes(apartment, db, cursor):
  # a function to get the people that have liked a certain apartment
  # apartment: type int
  # db: type database
  # cursor: type database cursor
  cursor.execute('''SELECT name FROM apartment_likes WHERE apartment = ?''', apartment )
  return cursor.fetchall()

def check_age_preference(user_one, user_two):
  # a function that checks if the age range for the two roommates are compatible
  age_one = user_one.get_age
  age_two = user_two.get_age
  age_one_pref = user_one.get_age_pref
  age_two_pref = user_two.get_age_pref
  if age_one_pref[0] >= age_two and age_two >= age_one_pref[1]:
    return False
  elif age_two_pref[0] >= age_one and age_two_pref[1] <= age_one:
    return False
  else:
    return True

 #checks if two users' sex preferences match, NoneType is an "any" select
def check_sex(u_one, u_two):
  sex_one = u_one.get_sex
  sex_two = u_two.get_sex
  sex_pref1 = u_one.get_sex_pref
  sex_pref2 = u_two.get_sex_pref
  if sex_pref1 == sex_two or sex_pref1 == None:
    if sex_pref2 == sex_one or sex_pref2 == None:
      return True
  return False

#removes anyone with the incorrect preferences
def remove_incompatible(user, user_list):
  compatible_users = [] 
  for u in user_list:
    if check_age_preference(user, u) and check_sex(user, u):
      compatible_users.append(u)

def find_match(user, other_users):
  max = 0
  match = other_users[0]
  wanted_traits = user.get_wanted_traits
  for u in other_users:
    traits = user.get_personal_traits
    common_traits = set_comparison(wanted_traits, traits)
    if common_traits > max:
      max = common_traits
      match = u
  return match

def set_comparison(user1, user2):
  # a function that compares two sets of traits and returns which they have in common
  traits_one = set(user1.get_wanted_traits)

  traits_two = set(user2.get_personal_traits)

  score = len( list(traits_one.intersection(traits_two)) )
  
  return score

  # traits_one: type list[strings]
  # traits_two: type list[strings]
  