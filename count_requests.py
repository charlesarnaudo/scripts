# Count the number of requests a unique host made given a logfile
def parse_hostname(line):
    # return re.search(r'\w+\.\w+\.\w+', line).group(0)
    return (line.split(" ")[0])
 

filename = input()
request_counts = {}

with open(filename) as fp:
    for line in fp:
        hostname = parse_hostname(line)
        if hostname not in request_counts:
            request_counts[hostname] = 1
        else:
            request_counts[hostname] += 1

with open("records_%s" % filename, 'w') as fp:
    for k, v in sorted(request_counts.items()):
        fp.write("%s %s\n" % (k, v))
