
# Create new possible bucket names from a domain

def newBucketNames(inBucket, wpath, isSubdomain):
    newNames = []
    if ".amazonaws.com" in inBucket:    # We were given a full s3 url
        bucket = inBucket[:inBucket.rfind(".s3")]
    elif ":" in inBucket:               # We were given a bucket in 'bucket:region' format
        bucket = inBucket.split(":")[0]
    else:                           # We were either given a bucket name or domain name
        bucket = inBucket

    newNames.append(bucket)
    domain = bucket.split(".")[0]
    if not domain in newNames:
	    newNames.append(domain) # sub.domain.com

    if isSubdomain:
        if bucket.split(".") > 2:
            newNames.append(".".join(bucket.split(".")[:-1]))    # sub.domain
            newNames.append("-".join(bucket.split(".")[:-1]))   # sub-domain
            newNames.append("".join(bucket.split(".")[:-1]))    # subdomain

    else:
        with open(wpath, 'r') as f:
            for line in f:
                line = line.rstrip()
                newNames.append(domain+"-"+str(line))
                newNames.append(str(line)+"-"+domain)
    print(str(newNames))
    return newNames
    
