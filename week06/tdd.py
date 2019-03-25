import pytest

# Step 1: Write an empty method

#python program to calculate simple interest
def  calculate_simple_interest(p,n,r):
	# pass
    return p*n*r/100


# Step 2: Write a test (that fails) for the above method and run the test
def  test_calculate_simple_interest():
	principal =  1000
	interest =  4
	years =  5
	assert(calculate_simple_interest(principal,interest,years) ==  200)


# Step 3: Write just enough code to make the above test succeed


# Step 4: Re-run the test and ensure that the test succeeds


# Step 5: Repeat the above steps to add a 2nd method to calculate the compound interest for a given principal, interest and period.

#python program that calculates annual compound interest
def calculate_compound_interest(p,n,r):
    # pass
	return p * (1.0  + r/100) ** n - p

#2nd test case
def test_calculate_compount_interest():
	principal =  1000
	interest =  5
	years =  5
	assert(calculate_compound_interest(principal,interest,years) ==  276.2815625000003)
