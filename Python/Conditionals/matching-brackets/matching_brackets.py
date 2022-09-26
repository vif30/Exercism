def is_paired(input_string):
    openings = ("(","[","{")
    closings = (")","]","}")
    open = []
    for i in input_string:
        if i in openings:
            open.append(i)
        if i in closings:
            if len(open) == 0:
                return False
            paired = matched(i, open)
            if paired:
                open.pop()
            else:
                return False
    if len(open) != 0:
        return False
    return True

def matched(last, open):
    if last == "]":
        return bool("[" == open[len(open)-1])
    if last == ")":
        return bool("(" == open[len(open)-1])
    if last == "}":
        return bool("{" == open[len(open)-1])

