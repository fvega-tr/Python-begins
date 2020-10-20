import random

def create_word_map(filepath):
	words={}
	f = open(filepath, 'r', encoding='utf8')
	done=False
	lastword=''
	while not done:
		t=f.readline()
		if len(t)==0:
			done=True
		else:
			for c in t.split(' '):
				c = c.strip('\n')
				if not c in words:
					words[c]={}
				if len(lastword)>0:
					if c in words[lastword]:
						words[lastword][c]= words[lastword][c] + 1.0
					else:
						words[lastword][c] = 1.0
				lastword=c
	f.close()
	return words


def markov_net(chars):
	for c in chars:
		tot=0
		for n in chars[c]:
			tot=tot+chars[c][n]
		for n in chars[c]:
			chars[c][n]=chars[c][n]/tot
	return chars

def generate_text(chars, initial_char, num_chars):
	text=''
	ch=initial_char
	for c in range(num_chars-1):
		text += ' '+ch
		ch=str(prob_choice(chars[ch]))
	return text

def prob_choice(prob_chars):
	probability = []
	char = []
	cur_prob = 0.0

	for c, p in prob_chars.items():
		cur_prob = cur_prob + p
		probability.append(cur_prob)
		char.append(c)

	rnd = random.random() * cur_prob
	for i, total in enumerate(probability):
		if rnd < total:
			return char[i]


if __name__ == "__main__":

	words = create_word_map("./science.txt")
	words = markov_net(words)
	text = generate_text(words, 'The', 100)
	print(text)
	#for key, value in words.items():
	#	print(value)