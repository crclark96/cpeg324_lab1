# description

`asi.py` is a simulator for a ficticious isa implementation documented in
`isa.txt`

to run, invoke `asi.py` followed by a filename containing the ascii
representation of the binary instructions you would like to simulate

comments are supported with the `#` character at the beginning of lines

please do not include extraneous newline characters at the end of simulation
files

# benchmarks

four example simulations are included. they have the `.asi` extension

additionally, `.res` files document the expected output of the simulation

the `test.sh` script will show the difference between a provided `.res`
file and the output of the simulator. invoke this as follows:

`./test.sh <file>.asi <file>.res`

# feedback

during benchmarks, we discovered that our simulator did not implement the
compare instruction correctly. it skipped one too few instructions. we
discovered this when writing the `test_comp.asi` and `test_comp.res` files,
included in this repository

no other discrepancies were found with our benchmarks

# todo

we would like to add a simple interpreter to make writing benchmark code
less tedious
