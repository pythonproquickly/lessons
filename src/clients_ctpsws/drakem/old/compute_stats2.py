import sys
import fileinput


def compute_stats(lines):
    if not lines:
        return (None, None, None, None)
    o_min = min(lines)
    o_max = max(lines)
    o_avg = sum(lines) / len(lines)
    lines_len = len(lines)
    mid = (lines_len - 1) // 2
    if lines_len % 2:
        o_median = lines[mid]
    else:
        o_median = (lines[mid] + lines[mid + 1]) / 2.0
    return (o_min, o_max, o_avg, o_median)


def main(column_number, data_file):
    lines = []
    if not data_file:
        for line in fileinput.input():
            line = line.split(" ")
            line = line[column_number]
            line = line.rstrip()
            lines.append(float(line))
    else:
        f = open(data_file, 'r')
        for line in f:
            line = line.split(" ")
            line = line[column_number]
            line = line.rstrip()
            lines.append(float(line))
    lines.sort()
    o_min, o_max, o_avg, o_median = compute_stats(lines)

    print(f"minimum value {o_min}")
    print(f"maximum value {o_max}")
    print(f"average value {o_avg}")
    print(f"median value {o_median}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("must specify column number")
        exit()
    column_number = int(sys.argv[1])
    if len(sys.argv) == 3:
        data_file = sys.argv[2]
    else:
        input_lines = sys.argv.pop()
        data_file = ""
    main(column_number, data_file)
