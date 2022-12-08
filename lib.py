import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange


def shamir_create_polynomial(secret, t, n):
    # create a list of t-1 random numbers
    # and add the secret to the list
    coeff = []
    for i in range(t-2):
        coeff.append(random.randint(-100, 100))
    coeff.append(secret)
    # return the list
    return coeff


def shamir_create_shares(coeff, n):
    # create a list of n shares
    shares = []
    for i in range(n):
        # create a list of the x values
        x = i+1
        # create a list of the y values
        y = np.polyval(coeff, x)
        # append the x and y values to the shares list
        shares.append([x, y])
    # return the list of shares
    return shares


def shamir_recover_secret(shares, t):
    shares = shares[:t-1]
    # create a list of the x values
    x = [i[0] for i in shares]
    # create a list of the y values
    y = [i[1] for i in shares]
    # create the lagrange polynomial
    l = lagrange(x, y)  # lagrange is not stable for large numbers of shares
    # print(l.coef)
    # return the secret
    return l(0)


if __name__ == "__main__":
    secret = 420
    t = 8
    n = 10
    coeff = shamir_create_polynomial(secret, t, n)
    shares = shamir_create_shares(coeff, n)

    # round to nearest integer to avoid floating point errors
    recovered_secret = round(shamir_recover_secret(shares, t))
    print("the secret is:", secret)
    print("the recovered secret is:", recovered_secret)
    assert secret == recovered_secret
