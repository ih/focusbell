$(function(){
    interval = Number($("#initial_interval").attr("value")); //TODO make interval a local variable, argument to testFocus?
    if(interval == NaN){
      alert("error with initial interval");
      interval = minutes(5);
    }
    setTimeout(testFocus, interval);
  });

function testFocus(){
  var key = $("#key").attr("value");
  var focused = confirm("Focused since last time?");
  saveAlert(key, focused, interval);
  if(focused==true){
    increaseInterval(); //TODO tweak formula for adjusting interval
  }
  else{
    decreaseInterval();
  }
  setTimeout(testFocus, interval);
}

function increaseInterval(){
  interval += minutes(5);
}

function decreaseInterval(){
  interval -= minutes(5);
  if(interval <= 0){
    interval = minutes(5);
  }
}

function minutes(milliseconds){
  return milliseconds*60000;
}

function saveAlert(key, focused, interval){
  $.post("/alert", {session: key, was_focused: focused, interval: interval},
	 function(data){

	 });
}