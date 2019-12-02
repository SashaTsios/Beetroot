'''
import wikipedia

search = input('Please enter what you are looking for in wikipedia: ')

def wiki(search):
    while search.lower() != 'quit0':
        num_of_results = 1
        searchNEW = search
        try:
            wiki_search = wikipedia.search(search, num_of_results)
        except wikipedia.exceptions.PageError as p:
            print(f'write more, {p.options}')
            print('Your search does not match any pages')
            searchNEW = input('Enter again: ')  # or type \'quit0\' to quit
        try:
            wiki_search = wikipedia.summary(search)
        except wikipedia.exceptions.DisambiguationError  as d:
            print(f'Few variants appeared, please choose one: {d.options}')
            ind = int(input('Enter index!: '))
            print('================================')
            searchNEW = d.options[ind]

        search = searchNEW
        print(search)  # checking
        print(type(search))  # checking
        print(f'The best searched is: {search}')
        print(f'Next 5 proposed variants are:{wikipedia.search(search)[1:6]}')
        print('Let\'s review the first one:\n')
        #search0 = wikipedia.page(search)
        search0 = wikipedia.page('Zarichne, Donetsk Oblast')  # delete this, use previous line
        print(f'Title: {search0.title}')
        print(f'url: {search0.url}')
        print('Summary, first 5 sentences:')
        num_of_sentences = 5
        print(wikipedia.summary(search, num_of_sentences))
        print('================================')
        search = input('Another search? Or type \'quit0\' to quit: ')
    print('Bye')


if __name__ == '__main__':
    wiki(search)
'''

import wikipedia


def wiki(search):
    while search.lower() != 'quit0':
        num_of_results = 1
        searchNEW = search
        while True:
            search = searchNEW
            try:
                wikipedia.search(search, num_of_results)
                wikipedia.summary(search)
            except wikipedia.exceptions.PageError as p:
                print('================================')
                print(f'write more, {p.options}')
                print('Your search does not match any pages')
                searchNEW = input('Enter again: ')  # or type \'quit0\' to quit
            except wikipedia.exceptions.DisambiguationError as d:
                print('================================')
                dict_from_d_options = {}
                for k, index in enumerate(d.options):
                    dict_from_d_options[k] = index
                print(f'Few variants are on wiki, please choose one: {dict_from_d_options}')
                print('These articles are on wiki, but may be completely empty and you\'ll get new proposal to enter index')
                ind = int(input('Enter index!: '))
                print('================================')
                searchNEW = dict_from_d_options[ind]
            else:
                break
        search = searchNEW
        # print(search)
        print(f'The best searched is: {search}')
        print(f'Next 10 proposed variants connected with {search}: {wikipedia.search(search)[1:11]}')
        print('Let\'s review the first one:\n')
        search0 = wikipedia.page(search)
        # search0 = wikipedia.page('Zarichne, Rivne Oblast')  # delete this, use previous line
        print(f'Title: {search0.title}')
        print(f'url: {search0.url}')
        print('Summary, up to 5 sentences:')
        num_of_sentences = 5
        print(wikipedia.summary(search, num_of_sentences))
        print('================================')
        search = input('Another search? Or type \'quit0\' to quit: ')
    print('Bye')


if __name__ == '__main__':
    aaa = input('Want to search geo coordinates, y or Y - yes: ')
    if aaa.lower() == 'y':
        coord_x = float(input('GeoX?: '))
        coord_y = float(input('GeoY?: '))
        search = str(f'{coord_x}, {coord_y}')
    else:
        search = input('Please enter text what you are looking for in wikipedia: ')    
    wiki(search)