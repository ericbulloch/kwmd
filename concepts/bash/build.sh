#!/bin/bash

info () { printf "  [ \033[00;34mINFO\033[0m ] $1\n"; }
success () { printf "\r\033[2K  [ \033[00;32mOK\033[0m ] $1\n"; }
fail () { printf "\r\033[2K  [\033[0;31mFAIL\033[0m] $1\n"; echo ''; exit 1; }

OPERATION=${1:-'all'}
OPERATION="${OPERATION//-}"

OPERATIONS=( 'all' 'build' 'clean' 'lint' 'pep8' 'search' 'test')
HELP_OPERATIONS=( 'help' 'h' )

if [[ " ${OPERATIONS[*]} " == *" ${OPERATION} "* ]]; then
    info "Starting the checks script with parameter: $OPERATION"
else
    echo "Here are a list of valid operations:"
    echo ''
    printf '%s\n' "${OPERATIONS[@]}"
    echo ''
    printf "\033[00;32mThis script defaults to 'all' as the operation when an operation is not provided\033[0m\n"
    echo "Usage: ./checks.sh [operation]"

    if [[ " ${HELP_OPERATIONS[*]} " == *" ${OPERATION} "* ]]; then
        echo ''
        exit 0
    else
        echo ''
        fail "${OPERATION} is not a valid operation";
    fi
fi

ensure_directory () {
    if [ ! -d 'build' ]; then
        mkdir build
    fi
    if [ ! -d 'build/checks' ]; then
        mkdir build/checks
    fi
    if [ ! -d "build/checks/$1" ]; then
        mkdir "build/checks/$1"
    fi
}

if [ ${OPERATION} = "all" ]; then
    info "Removing the checks directory"
    rm -rf build
    success "Checks directory removed"
fi

if [ ${OPERATION} = "build" ]; then
    pyinstaller main.py
    cp -r images/ dist/main
    cp -r maps/ dist/main
    cp -r music/ dist/main
    cp -r settings/ dist/main
    cp logging.ini dist/main
    mkdir dist/main/saves
    cp -rf dist/main build
    rm -rf dist
fi

if [ ${OPERATION} = "clean" ]; then
    info "Cleaning the project"
    rm build local -rf
    success "Done cleaning the project"
fi

if [ ${OPERATION} = "all" ] || [ ${OPERATION} = "lint" ]; then
    info "Running PyLint"
    ensure_directory "pylint"
    pylint py_dwc *.py > build/checks/pylint/output.txt
    success "PyLint finished"
fi

if [ ${OPERATION} = "all" ] || [ ${OPERATION} = "pep8" ]; then
    info "Running PEP8"
    ensure_directory "pep8"
        pep8 --show-source --show-pep8 --exclude=bin,lib,local . > build/checks/pep8/output.txt
    success "PEP8 finished"
fi

if [ ${OPERATION} = "search" ]; then
    info "Running Search"
    grep $2 -rn --exclude=\.coverage --exclude-dir=local --exclude-dir=lib --exclude-dir=build --exclude-dir=include .
    success "Search finished"
fi

if [ ${OPERATION} = "all" ] || [ ${OPERATION} = "test" ]; then
    info "Running PyTest"
    ensure_directory "pytest"
    python -m pytest test/unit/*.py --cov py_dwc --cov-report html --durations=30
    mv htmlcov/* build/checks/pytest
    rm -rf htmlcov
    success "PyTest finished"
fi

success "All checks have finished"
