#!/bin/bash

install(){
    echo 'Download & Install mjpg-streamer'

    echo 'update apt'
    sudo apt-get update

    echo 'upgrade apt'
    sudo apt-get upgrade

    echo 'package install'
    sudo apt-get install gcc g++ cmake libjpeg8-dev

    echo 'Download mjpg-streamer...'
    git clone https://github.com/jacksonliam/mjpg-streamer.git
    
    echo 'Building...'
    cd mjpg-streamer/mjpg-streamer-experimental

    make distclean
    make CMAKE_BUILD_TYPE=Debug
    sudo make install

    echo ''
    echo 'Download & Install Complete!'
}


run(){
    # echo 'export LD_LIBRARY_PATH=.'
    export LD_LIBRARY_PATH=./mjpg-streamer/mjpg-streamer-experimental/

    mjpg_streamer -o "output_http.so -w ./www -p 9090" -i "input_raspicam.so -fps 30 -preview" 
}


start(){
    echo 'mjpg-streamer Load Manager By overload'
    echo 'Select Your Action''s'
    echo '======================'
    echo '1) mjpg-streamer Install'
    echo '2) mjpg-streamer Run'
    echo 'any) cancel'
    echo '======================'
    echo -n 'number: '
    read num

    case $num in
      1)
        install
        ;;
      2)
	run
        ;;
      *)
	echo 'cancel'
    esac
}

start
