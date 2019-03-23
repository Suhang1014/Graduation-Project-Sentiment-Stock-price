import os


class FinishedDealer(object):
    def __init__(self):
        self.__new_ls = []

    def remove_duplicate(self):
        with open('../data/finished.reuters', 'r') as f:
            rows = f.readlines()
            for row in rows:
                row = row.strip()
                self.__new_ls.append(row)
        # new_ls.sort()
        self.__new_ls = set(self.__new_ls)
        return self.__new_ls

    def rewrite(self):
        with open('../data/finished2.reuters', 'w') as f:
            for item in self.__new_ls:
                f.writelines(item)
                f.write('\n')


if __name__ == '__main__':
    dealer = FinishedDealer()
    result = dealer.remove_duplicate()
    print(len(result), '\t', result)
    dealer.rewrite()



