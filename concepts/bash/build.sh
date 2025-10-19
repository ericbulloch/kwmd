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
