

def third_latest(dates):

    # converting date objects to strings
    dates_as_strings = [str(element) for element in dates]

    # convert each date string into tuple and reverse the tuple to get it in (year, month, day) format
    dates_to_sort = [tuple(s.split('-'))[::-1] for s in dates_as_strings]

    # sort the dates
    output_as_tuple = sorted(dates_to_sort)[-3][::-1]

    output = '-'.join(output_as_tuple)
    for element in dates:
        if str(element) == output:
            return element


# dates = ['07-01-1973', '19-07-2014', '11-03-1992']
dates = ['14-04-2001', '29-12-2061', '21-10-2019', '07-01-1973', '07-01-1973', '19-07-2014', '11-03-1992']
print(third_latest(dates))
