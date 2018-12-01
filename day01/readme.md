### First day back in time

#### Part one
This one was your ordinary first day of Python type of challenge, nothing to
report here

#### Part two
Not much more difficult, but it will take quite a while to crunch the numbers
if you don't use a Python dict or a hash map as it's usually called.

Let me elaborate on that a bit.

So to find duplicates you do need to hold a previously seen numbers somwhere,
so you know which numbers you've seen already.

There are two ways of doing this, with an array or a dictionary.

If you hold your numbers in an array then in each iteration you have to look
at the entire thing number by number to compare with the one you have in the
current iteration. Time that it takes to do this will grow rapidly.
Benchmarking such a solition gives us these stats:
> 133584 function calls in 104.526 seconds

Using a dictionary, though, will reduce the time significantly as it requires
O(1) time to check if a certain number exists in it, instead of O(N) it takes
in case of an array. Giving us following stats:
> 133585 function calls in 0.204 seconds

So that's quite a change in terms of time it takes.