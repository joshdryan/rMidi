# Constants
# represent transitions between two notes, starting with a base note.

import random

min_pitch=48
max_pitch=95

# SCALES

major = [0,2,2,1,2,2,2,1]
natural_minor = [0,2,1,2,2,1,2,2]
harmonic_minor = [0,2,1,2,2,1,3,1]
melodic_minor = [0,2,1,2,2,2,2,1]

scales = [major,natural_minor,harmonic_minor,melodic_minor]

def get_random_scale():

	return major

	# return random.choice(scales)

def get_random_key():

	return random.randint(min_pitch,min_pitch+12)