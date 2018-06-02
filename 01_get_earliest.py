# This code only works for the first part
def get_earliest(first_date, second_date):
  new_first_date = first_date[-4:] + first_date[:2] + first_date[3:5]
  new_second_date = second_date[-4:] + second_date[:2] + second_date[3:5]

  return first_date if new_first_date < new_second_date else second_date

# This code caters the bonus lecture too.
def get_earliest2(*args):
  earliest_date = ''
  previous_date = '29991231'
  
  for my_date in args:
    temp_date = my_date[-4:] + my_date[:2] + my_date[3:5]

    if(temp_date < previous_date):
      earliest_date = my_date
    
    previous_date = temp_date
  
  return earliest_date


# print(20160240 > 20160301)
# print(get_earliest('02/40/2006', '03/01/2006'))

print(get_earliest2('01/24/2007', '01/21/2008', '02/29/2009', '02/30/2006'))


