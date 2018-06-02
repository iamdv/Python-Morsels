def get_earliest(first_date, second_date):
  new_first_date = first_date[-4:] + first_date[:2] + first_date[3:5]
  new_second_date = second_date[-4:] + second_date[:2] + second_date[3:5]

  return first_date if new_first_date < new_second_date else second_date



