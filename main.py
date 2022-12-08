from lib import *
secret = 42

# create shamir shares
l = 8
v = 10
coeff = shamir_create_polynomial(secret, l, v)
shares = shamir_create_shares(coeff, v)

print(shares)
