document.addEventListener('DOMContentLoaded', function() {

      // Creating a new channel javascript object
      const webSocketBridgeUser = new channels.WebSocketBridge();
      // Connecting to user-notification route
      webSocketBridgeUser.connect('/user-notifications/');

      // Listening to channel events
      webSocketBridgeUser.listen(function(action, stream) {
        if(action.event == "New User") {
            addToList(action);
            $.notify("New user added\n" + action.first_name + " " + action.last_name, "success");
        }
        else if(action.event == "User updated"){
            removeFromList(action.user_id);
            addToList(action);
            $.notify("User data updated\n" + action.first_name + " " + action.last_name, "info");
        }

        else if(action.event == "User deleted"){
            removeFromList(action.user_id);
            $.notify("User deleted\n" + action.first_name + " " + action.last_name, "error");
        }

        else if(action.event == "New comment") {
            $.notify("New user comment\n" + action.comment + "\n\n  - " + action.username, "success");
            addCommentToList(action);
        }
      })
})
// Removing user from list
function removeFromList(id){
   $('#user_' + id).remove();
}

// Pre-pending user to list
function addToList(data){
   $("ul.users").prepend("<li class='list-group-item' id='user_" + data.user_id + "'>"
   + data.first_name + " " + data.last_name
   + " | <b>Username</b>: " + data.username  + "</li>");
}

// Adding new comment to list
function addCommentToList(data){
  $("ul.comments").prepend("<li class='list-group-item'><p>"
   + data.comment + "<br><br><span>- <b>" + data.username +"</b></span></p></li>");
}
