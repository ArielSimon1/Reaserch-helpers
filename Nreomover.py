import sys

def solve(a, n):
    max1 = -sys.maxsize - 1
    start =0
    for index1 in range(0, n-1):
        if (abs(a[index1+1] - a[index1]) > max1):
                max1 = abs(a[index1+1] - a[index1])
                start = a[index1]

    return max1, start


# Driver Code
if __name__ == '__main__':
    raw_seq = sys.argv[1]
    with open(raw_seq, 'r') as file:
        first_line = file.readline()
        s1 = file.read().replace('\n', '')

res = [i for i in range(len(s1)) if s1.startswith("N", i)]
#print(res)
size = len(res)
max, index = solve(res, size)
#print("Largest gap is :", solve(res, size))
final_seq = s1[index+1: (index+max)]
#print(s1[index+1: (index+max)])

first_line = first_line.rstrip()
first_line = first_line.replace(">",'')
file1 = open(first_line+".txt","w")
file1.write(">"+first_line+'\n')
file1.write(final_seq)
file1.close()

# run me with the line
# for f in *".seq"; do   python /home/stu/nissan/Ariel/PCR/Nreomover.py "$f"; done
