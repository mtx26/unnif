#!/usr/bin/env bash

# Test scripts on a temporary copy of the current directory.
# Edit and save scripts outside the sandbox; restart it to test an updated copy.
# Originals are mounted read-only at /src; tests run on the copy in /mnt.
# Changes to the copy are discarded when the sandbox fully exits.
# To leave, stop your programs, then type exit in each tmux pane.
# Switch panes by pressing Ctrl-b, releasing it, then pressing an arrow key.

export SHELL="/bin/bash"
bwrap \
    --unshare-all \
    --die-with-parent \
    --dev /dev \
    --proc /proc \
    --tmpfs /tmp \
    --ro-bind /usr /usr \
    --ro-bind /bin /bin \
    --ro-bind /lib /lib \
    --ro-bind-try /lib64 /lib64 \
    --ro-bind "$(pwd)" /src \
    --tmpfs /mnt \
    --chdir /mnt \
    /bin/bash -c '
        cp -a /src/. /mnt/ &&
        exec /usr/bin/tmux new \; splitw -h \; splitw -v
    '
