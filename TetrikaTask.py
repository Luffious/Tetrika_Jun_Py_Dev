import requests
from bs4 import BeautifulSoup
import urllib


def task(array):
    return array.find('0')


def animals():
    print('Counting animals!')
    url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
    amount = 0
    result = {}
    flag = True
    while flag:
        soup = BeautifulSoup(requests.get(url=url).content, 'html.parser')
        letters = soup.find(id='mw-pages').find_all('h3')
        if (len(letters) >= 2):
            length = len(letters)
            for letter in letters:
                if letter.next != 'A':
                    animals = letter.find_parent('div').find('ul').get_text().split('\n')
                    if length > 1:
                        amount += len(animals)
                        result.update({letter.next: amount})
                        amount = 0
                        length -= 1
                        print('Letter ' + str(letter.next) + ' is over!')
                    else:
                        amount += len(animals) - 1
                        result.update({letter.next: amount})
                else:
                    flag = False
        else:
            animals = soup.find(id='mw-pages').find('ul').get_text().split('\n')
            amount += len(animals) - 1
            result.update({letters[0].next: amount})
        url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=' + urllib.parse.quote(animals[len(animals) - 1]) + '#mw-pages'
    return result


def appearance(intervals):
    temp_results, results = [], []
    i = 0
    while i < len(intervals['pupil']):
        try:
            if i % 2 == 0:
                if intervals['pupil'][i] < intervals['lesson'][0]:
                    intervals['pupil'][i] = intervals['lesson'][0]
                if intervals['pupil'][i] > intervals['lesson'][1]:
                    del intervals['pupil'][i:i + 2]
                    i -= 1
            else:
                if intervals['pupil'][i] < intervals['lesson'][0]:
                    del intervals['pupil'][i - 1:i + 1]
                    i -= 3
                if intervals['pupil'][i] > intervals['lesson'][1]:
                    intervals['pupil'][i] = intervals['lesson'][1]
        except:
            pass
        i += 1
    i = 0
    while i < len(intervals['tutor']):
        try:
            if i % 2 == 0:
                if intervals['tutor'][i] < intervals['lesson'][0]:
                    intervals['tutor'][i] = intervals['lesson'][0]
                if intervals['tutor'][i] > intervals['lesson'][1]:
                    del intervals['tutor'][i:i + 2]
                    i -= 1
            else:
                if intervals['tutor'][i] < intervals['lesson'][0]:
                    del intervals['tutor'][i - 1:i + 1]
                    i -= 3
                if intervals['tutor'][i] > intervals['lesson'][1]:
                    intervals['tutor'][i] = intervals['lesson'][1]
        except:
            pass
        i += 1
    i, j = 0, 0
    while i < len(intervals['tutor']):
        while j < len(intervals['pupil']):
            if intervals['tutor'][i] < intervals['pupil'][j]:
                temp_results.append(intervals['pupil'][j])
            else:
                temp_results.append(intervals['tutor'][i])
            if intervals['tutor'][i + 1] > intervals['pupil'][j + 1]:
                temp_results.append(intervals['pupil'][j + 1])
            else:
                temp_results.append(intervals['tutor'][i + 1])
            j += 2
        i += 2
        j = 0
    i = 0
    while i < len(temp_results):
        try:
            if temp_results[i] > temp_results[i + 1] and i % 2 == 0:
                del temp_results[i:i + 2]
                i -= 1
        except:
            pass
        i += 1
    i = 0
    while i < len(temp_results):
        if i % 2 == 0:
            temp_results[i] -= 1 
        i += 1
    i = 0
    while i < len(temp_results):
        temp = temp_results[i] + 1
        try:
            while temp < temp_results[i + 1]:
                results.append(temp)
                temp += 1
        except:
            pass
        i += 2
    results.sort()
    results = list(dict.fromkeys(results))
    return len(results)


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

print('Task 1: First zero\'s index is ' + str(task('111111111110000000000000000')))
print('Task 2: ' + str(animals()))
print('Task 3: ', end='') 

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       if i != 2:
            print(str(test_answer) + ' seconds;', end=' ') 
       else:
           print(str(test_answer) + ' seconds.') 
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
