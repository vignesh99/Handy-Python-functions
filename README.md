Listed below are a set of functions from existing python libraries. Some of them are for enhancing computational speed, and others are for convinience. 

- [Pickle](#pickle)
- [Subprocess](#subprocess)

[//]: # "- [Map](#map)"

## Pickle

```Python
from pickle import dump
from pickle import load
                                    #Use load to feed data to variable
names = load(open('greekgods.pkl', 'rb'))
print(names)
                                    #Store required data using dump
flip = shuffle(names)
dump(flip, open('flipped.pkl', 'wb'))
```

## Subprocess

```Python
import subprocess
                                    #String containing your command to run on terminal
filename = "HelloWorld.py"
args = ["python3 "+filename]        #We want to run "python3 HelloWorld.py"

                                    #Run the command on terminal using subprocess
popen = subprocess.Popen(args, stdout=subprocess.PIPE,shell=True)
popen.wait()
                                    #Read the output given from the terminal
output = popen.stdout.read()
output = output.decode("utf-8")
```

[//]: # "## Map"


Will add more such functions as and when I come across them..
