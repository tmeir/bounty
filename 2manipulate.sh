#!/bin/bash
grep -v -F -x -f list-temp.txt $@  >toManipulate.txt && cat toManipulate.txt >>list-temp.txt
