def find_border(palin_str):
    n = len(palin_str) // 2
    this_k = n
    this_border = None
    while this_k >= 0:
        if this_k == 0:
            this_border = ""
            break
        else:
            this_border = palin_str[0:this_k]
            if this_border == palin_str[len(palin_str) - this_k:len(palin_str)]:
                break
            else:
                this_k = this_k - 1
    return this_border, this_k


while True:
    data = input()
    if data == "end":
        break
    else:
        border, k = find_border(data)
        core = data[k:len(data) - k]
        if border != "" and core != "":
            nilapdrome = core + border + core
            print(nilapdrome)
