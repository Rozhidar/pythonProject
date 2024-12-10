age_of_person = float(input())
gender_of_person = input()

if gender_of_person == 'm':

    if age_of_person >= 16:
        print('Mr.')
    elif age_of_person < 16:
        print('Master')

elif gender_of_person == 'f':

    if age_of_person >= 16:
        print('Ms.')
    elif age_of_person < 16:
        print('Miss')
