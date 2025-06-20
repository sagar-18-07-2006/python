def sum_of_n_natural_numbers(n):
    if n==1:
        return 1;
    if n>1:
        return (n + sum_of_n_natural_numbers(n-1))
    if n<1:
        return "it is not a natural number"
n =int (input("enter the number: "))
print(sum_of_n_natural_numbers(n))
