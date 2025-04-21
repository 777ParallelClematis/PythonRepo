wifi_enabled: bool = True
has_electricity: bool = True
has_subscription: bool = True

# if wifi_enabled and has_subscription and has_electricity:
#     print('Connected to internet!')

requirements: list[bool] = [wifi_enabled, has_electricity, has_subscription]

if all(requirements):
    print('Connected to Internet!')

people_voted: list[int] = [1, 1, 1, 1, 0, 1, 1, 0]

if all(people_voted): #if not all(people_voted):
    print('Everyone Voted!')
else:
    print('Some people did not vote!')


people_voted2: list[int] = [0,1,0,0,0]

if any(people_voted2):
    print('At least one person voted')
else:
    print('No one voted')