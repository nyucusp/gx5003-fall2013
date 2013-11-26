import os, subprocess, sys, time, datetime

waittime = 15 * 60
index = 0
storage_dir = "./json"
run = True

if not os.path.exists(storage_dir):
    print "NO json data dir! fix it."
    run = False

while run:
    print "Getting JSON from Citibike: %d" % (index)

    output = subprocess.check_output('curl http://citibikenyc.com/stations/json', shell=True)

    filepath = os.path.join(storage_dir, "citibike_%d.json" % (index) )
    with open(filepath, 'w') as f:
        f.write(output)
    index += 1

    for i in xrange(waittime):
        sys.stdout.write(str(datetime.datetime.now()) + ": " + str(i) + "s of " + str(waittime) + "s \r")
        sys.stdout.flush()
        time.sleep(1)
