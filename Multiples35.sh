#!/bin/bash

total=0; for a in {1..999}; do test=$((a%3)); test1=$((a%5)); if [ $test == 0 ] || [ $test1 == 0 ]; then total=$((total + a)); fi; done; echo $total
