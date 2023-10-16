'''
The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:

Note that "" represents the consecutive values in between.
Example

Print the string .
Input Format
The first line contains an integer .
Constraints

Output Format
Print the list of integers from  through  as a string, without spaces.
Sample Input 0
3
Sample Output 0
123
'''

def str_1(n):
    str_1 = ""
    i = 1

    while i <= n:
        str_1 += str(i)
        i += 1

    return str_1

if __name__ == '__main__':
    n = int(input())
    str_1 = str_1(n)
    print(str_1)
