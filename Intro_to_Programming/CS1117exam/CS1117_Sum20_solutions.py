# ENTER YOUR NAME AND STUDENT NUMBER HERE:
# Jack O'Connor 119319446
# CS1117 - BSc/DSA 2019/20
# Tuesday 28th April (Irish Summer Time)
#
# State here is you are registered with DSS: NO
#
# State here if availing of a spelling and grammar waiver: NO
#
# Place your work for each question/part in the appropriate section below.
#
# By submitting this exam, you declare
#    (1) that all of the  work is your own;
#    (2) that you did not seek whole or partial solutions for any part of
#        your submission from others; and
#    (3) that you did not and will not discuss, exchange, share, or
#        publish complete or partial solutions for this exam or any
#        part of it.
#
# This is to certify that the work I am submitting is my own and has been done by me solely and not in consultation with anyone else. Neither I nor anyone else have submitted this work for assessment, either at University College Cork or elsewhere. I have read and understood the regulations of University College Cork concerning plagiarism.  Where breaches of the declaration are detected, these will be reviewed under UCC student conduct and plagiarism policies. Any breach of the examination rules is a serious issue and can incur penalties.

# By proceeding you signify your agreement to ALL the above rules and declaration.

# QUESTION ONE
# ==========================================================================
def question_one():
    # the answer for each MCQ question will be added to this list
    question_one_answer = []

    # place your choice of A, B, C or D between the quotes for each question
    # of this MCQ, e.g., if you think D is the correct answer for part (i),
    # the code snippet will be:
    # part_i = "D"

    # Part (i)
    # --------------------------------------------------------
    part_i = "B"
    question_one_answer.append(part_i)

    # Part (ii)
    # --------------------------------------------------------
    part_ii = "C"
    question_one_answer.append(part_ii)

    # Part (iii)
    # --------------------------------------------------------
    part_iii = "D"
    question_one_answer.append(part_iii)

    # Part (iv)
    # --------------------------------------------------------
    part_iv = "B"
    question_one_answer.append(part_iv)

    # Part (v)
    # --------------------------------------------------------
    part_v = "B"
    question_one_answer.append(part_v)

    # Part (vi)
    # --------------------------------------------------------
    part_vi = "A"
    question_one_answer.append(part_vi)

    # Part (vii)
    # --------------------------------------------------------
    part_vii = "D"
    question_one_answer.append(part_vii)

    # Part (viii)
    # --------------------------------------------------------
    part_viii = "B"
    question_one_answer.append(part_viii)

    # Part (ix)
    # --------------------------------------------------------
    part_ix = "B"
    question_one_answer.append(part_ix)

    # Part (x)
    # --------------------------------------------------------
    part_x = "D"
    question_one_answer.append(part_x)

    return question_one_answer


# QUESTION TWO
# ===========================================================================

def loop_the_loop(a1, a2):
    new_loop = []
    for e1 in a1:
        for e2 in a2:
            new_loop.append(e1 + e2)
    return new_loop


# Part (a)
# --------------------------------------------------------
def loop_the_loop_while(a1, a2):
    # Place your work for Q2, Part (a) here.
    new_loop = []
    e1 = 0
    while e1 < len(a1):
        e2 = 0
        while e2 < len(a2):
            new_loop.append(a1[e1] + a2[e2])
            e2 += 1
        e1 += 1
    return new_loop


# Part (b)
# --------------------------------------------------------
def loop_the_loop_comp(a1, a2):
    # Place your work for Q2, Part (b) here.
    return [e1 + e2 for e1 in a1 for e2 in a2]


# Part (c)
# --------------------------------------------------------
def loop_the_loop_zip(a1, a2):
    # Place your work for Q2, Part (c) here.
    rotate = lambda x: x[1:] + x[0:1]  # rotate used to sum different pairs of numbers

    l = []
    for i in range(len(a1)):
        l += list(map(sum, zip(a1, a2)))
        a2 = rotate(a2)

        out = []
    for i in range(len(a1)):
        for j in range(len(a1)):
            out.append(l[3*j + i])
    # has the right numbers just not in the right order :(
    return out


# Part (d)
# --------------------------------------------------------
def loop_the_loop_error(a1, a2):
    # Place your work for Q2, Part (d) here.
    try:
        new_loop = []
        for e1 in a1:
            for e2 in a2:
                new_loop.append(e1 + e2)
        return new_loop
    except:
        return "Oops, error..."


# QUESTION THREE
# ==========================================================================
def add_to_list(element, alist, index=0):
    """
    index has default value 0 for when no argument is passed to index.
    """
    # Place your work for Q3 here.
    try:
        if index < 0:
            return [element] + alist
        else:
            return alist[:index] + [element] + alist[index:]
    except:
        return "Oops, error..."


# QUESTION FOUR
# ==========================================================================
# Part (a)
# --------------------------------------------------------
def read_file(input_file):
    # Place your work for Q4, Part (a) here.
    try:
        f = open(input_file, 'r')
        lines = f.readlines()
        f.close()

        # formatting of file
        for i in range(len(lines)):
            for symbol in [')', '(', '\n', '"']:
                lines[i] = lines[i].replace(symbol, '')
            lines[i] = lines[i].split(', ')

        d = {}
        for line in lines:
            if int(line[0]) not in d:
                d[int(line[0])] = line[1:]  # add name and address
            else:
                d[int(line[0])].append(line[2])  # append additional address
        return d
    except:
        return "Oops, error..."


# Part (b)
# --------------------------------------------------------
def write_dict(d):
    # Place your work for Q4, Part (b) here.
    try:
        file = open("output.txt", 'w')

        # I've put two spaces after the id number to match the example from the .docx file.
        for key in d.keys():
            if len(d[key]) > 2:  # for when a person has more than one address
                file.write(f"id {key}  {d[key][0]} has an address of {d[key][1]}\n")
                for address in d[key][2:]:
                    file.write(f"id {key}  {d[key][0]} also has an address of {address}\n")
            else:
                file.write(f"id {key}  {d[key][0]} has an address of {d[key][1]}\n")

        file.close()
        return
    except:
        return "Oops, error..."


# QUESTION FIVE
# ==========================================================================
# Part (a)
# --------------------------------------------------------
def biggest_retail_chain(d):
    # Place your work for Q5, Part (a) here.
    try:
        if not d:
            return []

        chains = []
        greatest_number = 0
        for chain, serves in d.items():
            if len(serves) > greatest_number:
                chains = [chain]
                greatest_number = len(serves)
                continue
            if len(serves) == greatest_number:
                chains.append(chain)
        return chains
    except:
        return "Oops, error..."


# Part (b)
# --------------------------------------------------------
def common_towns(d, rc1, rc2):
    # Place your work for Q5, Part (b) here.
    try:
        out = []
        if rc1 not in d or rc2 not in d:
            return out

        for town in d[rc1]:
            if town in d[rc2]:
                out.append(town)
        return out
    except:
        return "Oops, error..."


# Part (c)
# --------------------------------------------------------
def sorted_print(d):
    # Place your work for Q5, Part (c) here.
    try:
        l = []
        for key, value in d.items():
            l.append([key, value])
        l = sorted(l)  # sort by key first

        for i in range(len(l)):  # sort each keys values
            l[i][1] = sorted(l[i][1])

        # find the lengths of the longest store name and town name for consistent tabbing
        longest_store = 0
        longest_town = 0
        for i in range(len(l)):
            if len(l[i]) > longest_store:
                longest_store = len(l[i])
            for j in range(len(l[i])):
                if len(l[i][j]) > longest_town:
                    longest_town = len(l[i][j])

        for pair in l:
            if len(pair[1]) == 0:  # store serves no towns
                print(pair[0].capitalize())
            else:
                # double tabs to try match sample spacing
                print(pair[0].capitalize() + ' ' * (longest_store - len(pair[0])), end='\t\t')
                for town in pair[1][:-1]:
                    print(town.capitalize() + ' ' * (longest_town - len(town)), end='\t\t')
                print(pair[1][-1].capitalize())  # end of the line
        return
    except:
        return "Oops, error..."
