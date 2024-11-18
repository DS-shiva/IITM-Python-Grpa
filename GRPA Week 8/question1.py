def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    with open(filename, "r") as f:
        data = f.read().splitlines()  
        d = {}
        for x in data:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        return d        
        
