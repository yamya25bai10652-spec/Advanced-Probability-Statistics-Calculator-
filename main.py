#main.py
from stats import *
from probability import *
from distributions import *
from data_handler import load_csv

while True:
    print("\n--- Advanced Calculator ---")
    print("1. Load CSV Data")
    print("2. Enter Data Manually")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == '1':
        file = input("Enter CSV filename: ")
        data = load_csv(file)
    elif choice == '2':
        data = list(map(float, input("Enter numbers: ").split()))
    elif choice == '3':
        break
    else:
        continue

    print("\n1. Descriptive Stats\n2. Probability\n3. Distributions")
    op = input("Select: ")

    if op == '1':
        print("Mean:", mean(data))
        print("Quartiles:", quartiles(data))
        print("IQR:", iqr(data))
        print("Variance:", variance(data))

    elif op == '2':
        n = int(input("n: "))
        r = int(input("r: "))
        print("nCr:", nCr(n, r))

    elif op == '3':
        print("1. Binomial\n2. Normal")
        d = input("Choice: ")
        if d == '1':
            n = int(input("n: "))
            p = float(input("p: "))
            k = int(input("k: "))
            print("P(X=k):", binomial_pmf(n, k, p))
        elif d == '2':
            x = float(input("x: "))
            mu = float(input("mean: "))
            sigma = float(input("std dev: "))
            print("PDF:", normal_pdf(x, mu, sigma))


#statistics

import statistics

def mean(data):
    return statistics.mean(data)

def variance(data):
    return statistics.variance(data)

def quartiles(data):
    data = sorted(data)
    return (statistics.quantiles(data, n=4))

def iqr(data):
    q = quartiles(data)
    return q[2] - q[0]


#probablity

import math

def nCr(n, r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))


#distributions 

import math
from probability import nCr

def binomial_pmf(n, k, p):
    return nCr(n,k)*(p**k)*((1-p)**(n-k))

def normal_pdf(x, mu, sigma):
    return (1/(sigma*math.sqrt(2*math.pi))) * math.exp(-((x-mu)**2)/(2*sigma**2))

#data handlers
import csv

def load_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for val in row:
                data.append(float(val))
    return data



