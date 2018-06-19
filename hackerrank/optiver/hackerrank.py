dates = ['07-01-1973', '19-07-2014', '11-03-1992']
dates_for_sort = [(i.split('-')[2], i.split('-')[1], i.split('-')[0]) for i in dates]
output_reversed = dates_for_sort[2]
output_right_order = (output_reversed[2], output_reversed[1], output_reversed[0])
output = '-'.join(output_right_order)
print(output)



"""
hash_dates = list()
hash_dates.append(dates[0])
hash_dates.append(dates[1])
hash_dates.append(dates[2])
if len(dates) > 3:
    for element in dates[3:]:
        for hashed_date in hash_dates:
            if str(element).split('-')[2] > str(hashed_date).split('-')[2]:
                hash_dates.remove(hashed_date)
                hash_dates.append(element)
            elif str(element).split('-')[2] == str(hashed_date).split('-')[2]:
                if str(element).split('-')[1] > str(hashed_date).split('-')[1]:
                    hash_dates.remove(hashed_date)
                    hash_dates.append(element)
                elif str(element).split('-')[1] == str(hashed_date).split('-')[1]:
                    if str(element).split('-')[0] > str(hashed_date).split('-')[0]:
                        hash_dates.remove(hashed_date)
                        hash_dates.append(element)
"""