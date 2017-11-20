"""Övningar på iterators."""


class Cubes():
    """En iterator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.

    """
    def __init__(self):
        """Init method."""
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current ** 3


class Primes():
    """En iterator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    """
    pass
    # def __init__(self):
    #     self.prime = 0
    #     self.count = 0
    #     self.possible_divider = []
    #
    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     for i in range(2, self.prime):
    #         variable = self.prime / i
    #         if isinstance(variable, int) == False:
    #             self.count += 1
    #             if self.count == self.prime - 2:
    #                 self.possible_divider.append(self.prime)
    #                 self.prime += 1
    #             else:
    #                 continue


class Fibonacci():
    """En iterator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """
    def __init__(self):
        """Init method."""
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        c, self.a, self.b = self.a, self.b, self.a+self.b
        return c


class Alphabet():
    """Class method."""

    """En iterator som returnerar namnen på tecknen i det hebreiska alfabetet.
    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, mTet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """
    def __init__(self):
        """Init method."""
        self.index = 0
        self.hebrew = ["Alef", "Bet", "Gimel", "Dalet", "He", "Vav",
                       "Zayin", "Het", "Tet", "Yod",
                       "Kaf", "Lamed", "Mem", "Nun",
                       "Samekh", "Ayin", "Pe", "Tsadi",
                       "Qof", "Resh", "Shin", "Tav"]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.hebrew):
            raise StopIteration

        a = self.hebrew[self.index]
        self.index += 1
        return a

        # while self.index < len(self.hebrew):
        #     a = self.hebrew[self.index]
        #     self.index +=1
        #     return a
        #     if self.index >= len(self.hebrew):
        #         raise StopIteration


class Permutations():
    """Class method."""

    """En iterator som returnerar alla permutationer av en inmatad sträng.
    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """
    pass

    #  def __init__(self, string):
    #      self.start = ''
    #      self.string = string
    #
    #
    #  def __iter__(self):
    #      return self
    #
    #  def __next__(self):
    #      count = 0
    #
    #      if self.start == "":
    #          self.start = self.string
    #          count +=1
    #          return self.start
    #      index, symbol= 1, self.start[0]
    #      result = []
    #
    #      for i in self.string and count != len(self.string):
    #          test_perm = self.string[1:len(self.string)] + symbol
    #          if test_perm not in result:
    #              symbol = self.string[index]
    #              result.append(test_perm)
    #              count += 1
    #          else:
    #              raise StopIteration
    #      if count == len(self.start):
    #          pass
    #      index += 1
    #      return result


class LookAndSay():
    """En iterator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """

    def __init__(self):
        """Init method."""
        self.string = ''

    def __iter__(self):
        return self

    def __next__(self):
        # count, index , symbol, result = 0, 1, self.string[0], ""
        if self.string == '':
            self.string = '1'
            return 1

        count, symbol, result = 0, self.string[0], ""
        for c in self.string:
            if symbol == c:
                count += 1
            else:
                result = result + str(count) + symbol
                symbol = c
                count = 1
#            index += 1

        result = result + str(count) + symbol  # Remember the last count
        self.string = result
        return int(result)

# '1 1 1 2 2 1'
#            ^
# count = 1
# symbol = '1'
# result = '3122'
