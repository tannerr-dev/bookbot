def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    words = file_contents.split()
    # print(len(words))

    letter_count = {}
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lower_file = file_contents.lower()
    for i in alpha:
        letter_count[i] = lower_file.count(i)
    # print(letter_count)

    lc_list = []
    for i in alpha:
        lc_list.append({'letter':i, 'num': letter_count[i]})
    # print(lc_list)

    def sort_on(dict):
        return dict['num']

    lc_list.sort(reverse=True, key=sort_on)

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{len(words)} words found in the document')
    print()
    for i in lc_list:
        # print(i)
        print(f"The '{i['letter']}' character was found {i['num']}")
    print('--- End report ---')
main()
