faces = ['George Washington', 'Thomas Jefferson', 'Abrahan Lincoln', 'Alexander Hamilton', 'Andrew Jackson',
         'Ulysses S. Grant', 'Benjamin Franklin']
numnotes = int(input('How many denominations do you have?: '))


def noteface():
    if note == 1:
        print(f'{faces[0]} is printed on the $1 note')
    elif note == 2:
        print(f'{faces[1]} is printed on the $2 note')
    elif note == 5:
        print(f'{faces[2]} is printed on the $5 note')
    elif note == 10:
        print(f'{faces[3]} is printed on the $10 note')
    elif note == 20:
        print(f'{faces[4]} is printed on the 20$ note')
    elif note == 50:
        print(f'{faces[5]} is printed on the $50 note')
    elif note == 100:
        print(f'{faces[6]} is printed on the $100 note')
    else:
        print('No such note exists')


for i in range(numnotes):
    note = int(input(f'What is No {i + 1} denomination?: '))
    noteface()
