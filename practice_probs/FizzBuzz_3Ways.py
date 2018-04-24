from traceback import print_exc


def print_fb(start=1, end=101):
    """
    a) solution to Fizz Buzz problem using for, else, elif
    """
    try:
        if end > start:
            for num in range(start, end):
                if num % 15 == 0:
                    print('FizzBuzz')
                elif num % 3 == 0:
                    print('Fizz')
                elif num % 5 == 0:
                    print('Buzz')
                else:
                    print(num)
        else:
            print("\nThe Ending value of the list should be greater than the Starting value.")
    except TypeError:
        print("The type of the input arguments should be Integer Values. Not strings")
        print_exc()


def print_fb_comp(start=1, end=101):
    """
    b) solution to Fizz Buzz problem using list-comprehension (for else, inside list-comprehension)
    """
    try:
        if end > start:
            op_fizzbuzz = ['FizzBuzz' if num % 15 == 0 else
                           'Fizz' if num % 3 == 0 else
                           'Buzz' if num % 5 == 0 else
                           num for num in range(start, end)]
            print("\nPrinting the output of Fizz Buzz solution in List format")
            print(op_fizzbuzz)
            print("\nPrinting the output of Fizz Buzz solution without list format")
            for val in op_fizzbuzz:
                print(val)
        else:
            print("\nThe Ending value of the list should be greater than the Starting value.")
    except TypeError:
        print("The type of the input arguments should be Integer Values. Not strings")
        print_exc()


class Fizzbuzz:
    """
    c) solution to Fizz Buzz problem as a class object using an init method where the start, end values are set
    but has defaults of start=0, end=100 if start, end values are not specified at time of obj instance creation.
    """

    def __init__(self, start=1, end=100):
        self.start_val = start
        self.end_val = end

    def print_fb_class(self):
        try:
            if self.end_val > self.start_val:
                for num in range(self.start_val, self.end_val):
                    if num % 15 == 0:
                        print('FizzBuzz')
                    elif num % 3 == 0:
                        print('Fizz')
                    elif num % 5 == 0:
                        print('Buzz')
                    else:
                        print(num)
            else:
                print("\nThe Ending value of the list should be greater than the Starting value.")
        except TypeError:
            print("The type of the input arguments should be Integer Values. Not strings")
            print_exc()


if __name__ == "__main__":
    print("\nExecuting the FizzBuzz problem using for, else, elif.")
    print_fb(end=20)
    print("\nExecuting the FizzBuzz problem using List Comprehension")
    print_fb_comp(10, 30)
    print("\nExecuting the FizzBuzz problem using Class Object and Dunder Init method.")
    fb = Fizzbuzz(15, 50)
    fb.print_fb_class()
