function number_generator(){
  var number = Math.random();
  number = number*6;
  number = Math.round(number);
  return number;
}
var a = number_generator();
var b = number_generator();
var result = document.firstElementChild.lastElementChild.firstElementChild.firstElementChild;
var img1 = document.firstElementChild.lastElementChild.querySelectorAll("img")[0];
var img2 = document.firstElementChild.lastElementChild.querySelectorAll("img")[1]
if (a == 1){
  img1.src = "images/dice1.png";
}
else if (a == 2){
  img1.src = "images/dice1.png";
}
else if (a == 3){
  img1.src = "images/dice3.png";
}
else if (a == 4){
  img1.src = "images/dice4.png";
}
else if (a == 5){
  img1.src = "images/dice5.png";
}
else if (a == 6){
  img1.src = "images/dice6.png";
}
if (b == 1){
  img2.src = "images/dice1.png";
}
else if (b == 2){
  img2.src = "images/dice1.png";
}
else if (b == 3){
  img2.src = "images/dice3.png";
}
else if (b == 4){
  img2.src = "images/dice4.png";
}
else if (b == 5){
  img2.src = "images/dice5.png";
}
else if (b == 6){
  img2.src = "images/dice6.png";
}
if ( a>b ){
  result.innerHTML = "Player 1 won";
}
else if ( b>a ){
  result.innerHTML = "Player 2 won";
}
else{
  result.innerHTML = "its a draw this time";
}
