def compare_files(f1, f2):
    f1 = open(f1)
    f2 = open(f2)
    l1 = f1.readline()
    line_no = 0
    while l1:
        line_no += 1
        # add line numbers
        l2 = f2.readline()
        if not l2:
            print('line number:', line_no)
            print('missing l2, no match for:', repr(l1))
            return False
        l1 = l1.rstrip() # avoid cross-platform eol character issues
        l2 = l2.rstrip()
        if l1 != l2:
            print('line number:', line_no)
            print('l1:', repr(l1))
            print('l2:', repr(l2))
            return False
        l1 = f1.readline()
    l2 = f2.readline()
    if l2:
        print('line number:', line_no + 1)
        print('extra l2:', repr(l2))
        return False
    return True
