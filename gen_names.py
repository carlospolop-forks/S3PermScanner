
# Create new possible bucket names from a domain

def newBucketNames(inBucket, wpath):
    newNames = []
    if ".amazonaws.com" in inBucket:    # We were given a full s3 url
        bucket = inBucket[:inBucket.rfind(".s3")]
    elif ":" in inBucket:               # We were given a bucket in 'bucket:region' format
        bucket = inBucket.split(":")[0]
    else:                           # We were either given a bucket name or domain name
        bucket = inBucket

    newNames.append(bucket)
    domain = bucket.split(".")[0]
    with open(wpath, 'r') as f:
        for line in f:
            newNames.append(domain+"-"+str(line))
            newNames.append(str(line)+"-"+domain)
    
    return newNames
    