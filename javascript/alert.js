$(function(){
    interval = $("#initial_interval").attr("value"); //TODO make interval a local variable, argument to testFocus?
    setTimeout(testFocus, interval);
  });

function testFocus(){
  var key = $("#key").attr("value");
  var focused = confirm("Focused since last time?");
  if(focused==true){
    increaseInterval(); //TODO tweak formula for adjusting interval
  }
  else{
    decreaseInterval();
  }
  setTimeout(testFocus, interval);
  saveAlert(key, focused, interval);
}

function increaseInterval(){
  interval *= 2;
}

function decreaseInterval(){
  interval /= 2;
}

function saveAlert(key, focused, interval){
  $.post("/alert", {session: key, was_focused: focused, interval: interval},
	 function(data){

	 });
}