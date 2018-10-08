# generate random midi

# variables: length, key, complexity?

from midiutil.MidiFile import MIDIFile

import constants

import random


def main():
	scale = constants.get_random_scale()

	key = constants.get_random_key()
	# random.seed()
	generate_midi(key,scale)


def generate_midi(key, scale):

	# create MIDI object
	# one track for chords, one for other
	mf = MIDIFile(2)


	print(len(scale))
	print(key)
	
	###################
	###### CHORDS #####
	###################
	# each note is a half note
	note_length=4

	# Total number of notes
	num = 4
	note = key
	# times=[0,2,4,6,8,10,12,14]
	times=[0,4,8,12]

	track = 0   # the only 
	time = 0    # start at the beginning
	mf.addTrackName(track, time, "Generated Track")
	mf.addTempo(track, time, 120)

	channel = 0
	volume = 100

	for i in times:

		for n in range(num):

			note = key
			note = note + (12*random.randint(0,1))

			pitch = (note + sum(scale[:random.randint(0,len(scale))]))          # C4 (middle C)
			# time = random.choice(times)             # start on beat 0
			time = i             # start on beat 0
			duration = note_length         # 2 beat long
			mf.addNote(track, channel, pitch, time, duration, volume)


	
	###################
	###### NOTES #####
	###################
	# different note lengths
	note_lengths = [1/8,1/4]

	# Total number of notes
	num = 10
	note = key
	# times=[0,2,4,6,8,10,12,14]
	times=[0,1,2,3,4,5,6,7]
	# time_multipliers=[1/8,1/4,1/2,]
	time_multipliers=[1/4,1/2,3/4]


	simple_times=[0,1/4,1/2,3/4,1,5/4,3/2,7/4,2,9/4,5/2,11/4,3,13/4,7/2,15/4,4,
	17/4,9/2,19/4,5,21/4,11/2,23/4,6,25/4,13/2,27/4,7,29/4,15/2,31/4]

	track = 1   # the only 
	time = 0    # start at the beginning
	mf.addTrackName(track, time, "Generated Track")
	mf.addTempo(track, time, 120)

	channel = 1
	volume = 100


	for t in simple_times:
		
		note = key
		note = note + (12*random.randint(1,2))

		chance = random.randint(0,9)
		if chance > 5:
			pitch = (note + sum(scale[:random.randint(0,len(scale))]))          # C4 (middle C)
			# time = random.choice(times)             # start on beat 0
			time = t             # start on beat 0
			duration = random.choice(note_lengths)         # 2 beat long
			mf.addNote(track, channel, pitch, time, duration, volume)


	# for i in range(num):

	# 	note = key
	# 	note = note + (12*random.randint(1,2))

	# 	pitch = (note + sum(scale[:random.randint(0,len(scale))]))          # C4 (middle C)
	# 	# time = random.choice(times)             # start on beat 0
	# 	time = random.choice(times)+random.choice(time_multipliers)             # start on beat 0
	# 	duration = random.choice(note_lengths)         # 2 beat long
	# 	mf.addNote(track, channel, pitch, time, duration, volume)

	# write it to disk
	with open("output.mid", 'wb') as outf:
	    mf.writeFile(outf)
	pass

if __name__ == '__main__':
	main()


