                                    #Import the libraries
from pylab import *
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
                                    #Do some processing on the output
output = output.split("\n")
output = array(output)
                                    #Convert some of the values to floats
output = np.genfromtxt(output,delimiter=' ',dtype=str)
floats = output[-1]
floats = floats.astype("float")

print(list(floats))
