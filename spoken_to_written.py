import numpy as np

def spoken_to_written(spoken_input):
	temp = spoken_input
	temp[0].upper()
	written_output = temp
	return written_output

spoken_input = "hello please put a triple a battery in the remote"
written_output = spoken_to_written(spoken_input)
print(written_output)