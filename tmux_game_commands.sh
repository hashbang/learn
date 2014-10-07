
function get_active_window() {
  tmux list-windows | grep "\* ([0-9]* panes)" | sed 's/:.*//'
}
function get_active_pane() {
  tmux select-window -t `get_active_window`
  tmux list-panes | grep "(active)$" | sed 's/:.*//'
}

# add_notice "
# Hello HashBanger!
# We would like to
# invite you to a 
# celebration!"
function add_notice() {
  tmux split-window -t `get_active_pane` -h -p 20 "echo \"$@\"; read"
}

