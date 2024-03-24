#!/bin/bash

echo "Enter the number to find factorial:"
read n

fact=1
factorial=1

while [ $fact -le $n ]; do
    factorial=$((factorial * fact))
    fact=$((fact + 1))
done

echo "Factorial of $n = $factorial"

