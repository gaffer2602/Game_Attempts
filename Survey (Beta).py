print('Welcome To This Survey')
consent_given = False
while consent_given == False:
    print('Do You Consent To Your Answers And Information Being Used For Market Research?')
    consent = (input()).upper()
    answer_validity = False
    while answer_validity ==  False:
        if consent == 'YES':
            print('Splendid! Thank You For Your Co-Operation! We Shall Continue, Then.')
            answer_validity = True
            consent_given = True
        elif consent == 'NO':
            print('What A Shame! This Survey Is Ending Now, But Thank You For Your Co-Operation.')
            break
        else:
            print('You Are Not Co-Operating!')
            break

print('The Survey Shall Now Commence')

movie_title = input('What is your favourite movie? ' )
print('Movie Title:', movie_title)

movie_duration = int(input('How long is it? '))
print('Movie duration:', movie_duration)

ticket_price = float(input('How much is a ticket? '))
print('Ticket Price:', ticket_price)

answer_validity = False
tries = 0
while answer_validity == False:
    is_comedy = input('True Or False: This Movie Is A Comedy. ')
    if is_comedy == 'True':
        is_comedy = True
        answer_validity = True
    elif is_comedy == 'False':
        is_comedy = False
        answer_validity = True
    else:
        print('Not A Valid Answer. Try Again')
        tries = tries + 1
        if tries < 10:
            print('Tries Remaining:', 10 - tries)
        else:
            print('Your Session Has Been Terminated For Your Lack Of Co-Operation.')
            print('Goodbye')
            break
if answer_validity == True:
    print('True Or False: This Movie Is A Comedy. ', is_comedy,)
    print('Thank You For Your Co-Operation')
