Just put together some content which I felt were quite ingenious and powerful. Most of them are just functions of existing python libraries. While some of them are for enhancing computational speed, some others are for convinience which you didn't know you could have.
I will keep updating as and when I encounter more such things.

- [Pickle](#pickle)
- [Subprocess](#subprocess)
- [Map](#map)

## Pickle

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

## Map
