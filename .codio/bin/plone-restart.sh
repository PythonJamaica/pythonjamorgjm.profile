#!/bin/sh

echo "Restarting Plone"
tmux kill-window -t 1

tmux new-window -t plone:1 -n 'Instance' '~/workspace/Plonedev/bin/instance fg'
 
tmux select-window -t plone:1
tmux -2 attach-session -t plone
