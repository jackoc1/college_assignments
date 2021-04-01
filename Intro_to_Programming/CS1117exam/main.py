from CS1117_Sum20_solutions import *

def main():
    a1, a2 = [1, 2, 3], [7, 5, 2]
    print(loop_the_loop(a1, a2))
    print(loop_the_loop_while(a1, a2))
    print(loop_the_loop_comp(a1, a2))
    print(loop_the_loop_zip(a1, a2))
    print(loop_the_loop_error(a1, a2))

    alist = [1, 2, 3, 4, 5]
    element = 'a'
    print(add_to_list(element, alist, -1))
    print(add_to_list(element, alist, 0))
    print(add_to_list(element, alist, 3))
    print(add_to_list(element, alist, 10))
    print(add_to_list(element, alist))
    print(add_to_list(element, alist, 'a'))
    
    print(read_file("details.txt"))
    print(write_dict(read_file("details.txt")))
    
    d = {'tesco': ["cork", "dublin"], 'dunnes': ["kerry", "cobh", "dublin", "wilton"]}
    print(biggest_retail_chain(d))
    print(common_towns(d, 'tesco', 'dunnes'))
    sorted_print(d)

    return


if __name__ == '__main__':
    main()