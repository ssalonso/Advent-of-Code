def is_safe(report):
    """ list -> bool
        OBJ: determina si el nivel es seguro o no
    """
    diff_array = [a - b for a, b in zip(report[:] + [0], [0] + report[:])][1:-1]
    return all((-3 <= x < 0) for x in diff_array) or all((3 >= x > 0) for x in diff_array)

def is_tolerated(original_report):
    """ list -> bool
        OBJ: determina si el nivel es tolerable o no
    """
    new_reports = []
    for i in range(len(original_report)):
        new_report = original_report[:]
        del new_report[i]
        new_reports.append(new_report)
    return any(is_safe(report) for report in new_reports)

f = open('input2.txt')
reports = [list(map(int, line.split())) for line in f]
print(reports)
f.close()
print('Part I: ', sum(is_safe(r) for r in reports))
print('Part II: ', sum(is_safe(r) or is_tolerated(r) for r in reports))

# any
# zip
# map
# list comprehensions: newlist = [expression for item in iterable if condition == True]
# enumerate
