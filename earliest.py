def get_earliest(*args):
  earliest_date = ''
  previous_date = '29991231'
  
  for my_date in args:
    temp_date = my_date[-4:] + my_date[:2] + my_date[3:5]

    if(temp_date < previous_date):
      earliest_date = my_date
    
    previous_date = temp_date
  
  return earliest_date