#!/bin/bash
branch=$(git rev-parse --abbrev-ref HEAD)
msg=$(sed -n '/^#/!p' $1)
ticket_pattern='[[:alpha:]]+-[[:digit:]]+'
# Reject commits on release branches if they don't have a ticket number
if [[ $branch =~ 'release' ]]; then
    if ! [[ $msg =~ $ticket_pattern ]]; then
        echo 'Rejecting commit. Release branch commits need a ticket number'
        exit 1
    fi
fi
# If the branch is named after a ticket, prepend the branch name to the message
# if it doesn't already have a ticket
if [[ $branch =~ $ticket_pattern ]]; then
    ticket_from_branch=$BASH_REMATCH
    if ! [[ $msg =~ $ticket_pattern ]]; then
        sed -i.bak "1s;^;$ticket_from_branch ;" $1
        exit 0
    fi
fi
