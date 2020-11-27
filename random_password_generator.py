import random
import string

def generate_pass(size):

    generate_pass=''.join([random.choice(string.ascii_letters+string.digits) for n in range(size)])
    return generate_pass

password=generate_pass(10)
print(password)