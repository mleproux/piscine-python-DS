def mean(args):
    return (sum(args) / len(args))


def median(args):
    mid = len(args) // 2
    return ((args[mid] + args[~mid]) / 2)
    
    
def quartile(args):
    length = len(args)
    if length < 4:
        raise
    return ([float(args[int(length*(1/4))]), float(args[int(length*(3/4))])]) 

def variance(args):
    deviations = [(x - mean(args)) ** 2 for x in args]
    return mean(deviations)

def standard_deviation(args):
    return variance(args) ** .5
    
def ft_statistics(*args: any, **kwargs: any) -> None:
    sequence = list(args)
    sequence.sort()
    for value in kwargs.values():
        try:
            if args == None:
                raise
            if value == "mean":
                print(f"mean : {mean(sequence)}")
            elif value == "median":
                print(f"median : {median(sequence)}")
            elif value == "quartile":
                print(f"quartile : {quartile(sequence)}")
            elif value == "std":
                print(f"std : {standard_deviation(args)}")
            elif value == "var":
                print(f"var : {variance(args)}")
        except:
            print("ERROR")

