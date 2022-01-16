from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, SelectMultipleField


from wtforms.validators import DataRequired, Length

traits = ['clean', 'friendly', 'outgoing', 'shy', 'studious'] #can add more
age_range = [[18, 21], [22, 29], [30, 39], [40, 49], [50, 59], [60, 69], [70, 79], [80, 89], [90, 110]]
sex_options = ["male", "female"]

class questionnaireform():
  firstname = StringField('First name', validators = [DataRequired(), Length(min = 2, max = 20)])
  lastname = StringField('Last name', validators = [DataRequired(), Length(min = 2, max = 20)])
  age = SelectField("Select your age range", choices = age_range)
  sex = SelectField("Select sex", choices = sex_options) #unsure about this, trying to get radiobutton values
  dealbreakers = [age, sex]
  #def _init_(self, firstname, lastname, age, sex):

  #dealbreakers
  dealbreaker_choice = SelectMultipleField("Any Dealbreakers?:", choices = dealbreakers)
  


  ''''

  #traits
  flag1 = False
  while flag1 == False:
    my_traits = SelectMultipleField("Select 5 of the following traits that best describe you: ", choices = traits)
    
    if len(my_traits) == 5:
      flag1 = True
      break

    print('You have selected the incorrect number of traits, please try again.')

  #traits
  flag2 = False
  while flag2 == False:
    rm_traits = SelectMultipleField("Select 5 of the following traits that best describe you: ", choices = traits)
    
    if len(rm_traits):
      flag2 = True
      break

    print('You have selected the incorrect number of traits, please try again.')
    '''

  







  #i gotta figure out the correct field to pick multiple things still



