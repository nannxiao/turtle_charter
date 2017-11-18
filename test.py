def count_observations(myfile):
    count_l = int(sum(1 for line in myfile) / 3)
    return count_l

def get_max_value(fname, feature):
    myfile = open(fname)
    lst = myfile.readlines()
    for i,s in enumerate(lst):
        lst[i] = s.strip()
    max_array = 0
    count = int(len(lst)/3)
    feature_l = int(feature.split(' ')[1])
    for i in range(0, count):
        max_array = max(int(lst[i*3+feature_l]), max_array)
    return max_array

if __name__ == '__main__':
    fname = input('Enter the file path to visualize:')
    feature = input('Enter the feature you want to analyze:')
    myfile = open(fname)

    count_l = count_observations(myfile)
    max_l = get_max_value(fname, feature)
    print(max_l)
    print(count_l)