$(function(){
    interval = 2000; //TODO make interval a local variable, argument to testFocus?
    setTimeout(testFocus, interval);
  });

function testFocus(){
  var focused = confirm("Focused since last time?");
  if(focused==true){
    increaseInterval();
  }
  else{
    decreaseInterval();
  }
  setTimeout(testFocus, interval);
}
function increaseInterval(){
  interval *= 2;
}

function decreaseInterval(){
  interval /= 2;
}