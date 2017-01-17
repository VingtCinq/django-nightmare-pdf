import random


def get_random_filename(nb=50):
	choices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	return "".join([random.choice(choices) for i in range(nb)])