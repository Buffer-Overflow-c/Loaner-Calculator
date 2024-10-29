# Loaner-Calculator


Calculate the loaner fee based on the starting and ending date, using $5 as the fee 

To run the script make sure that you have python3.13 installed

python calc.py starting_date ending_date

eg.
  python calc.py 2024-01-01 2024-03-24

The output will be:
  Number of days used: 82 days
  Loaner price based on days used: $410

which is the result of the: 
  ((ending_date - 1) - starting_date) * 5
