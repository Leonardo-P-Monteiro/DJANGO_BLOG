from secrets import SystemRandom as SR
import string as s

print(''.join((SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64))))


