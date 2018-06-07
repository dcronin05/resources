#!/bin/bash

echo Hello World!
echo "Hello * World"
echo Hello * World
echo "Hello" World
echo Hello "           " World
echo "hello "*" World"

MY_MESSAGE="Hello World!!!"
echo $MY_MESSAGE

echo What is your name?
read MY_NAME
echo "Hello $MY_NAME - hope you're well."
echo $MY_NAME

echo "MYVAR IS: $MYVAR"
MYVAR="hi there"
echo "MYVAR IS: $MYVAR"

for i in *
    do
        echo "$i"
    # if [ "$i" == "test2.file" ]; then
        # echo ${i}" is a text file!"
    # fi
    done
