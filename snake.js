// variable diclaration
var canv = document.getElementById('s_canvas').getContext('2d');
var c_score = 0;

var sposx =80;
var sposy =80;

var nposx =0;
var nposy =0;
var fposx =140;
var fposy =180;
var snake = [];
var snakesize = 1;
var gamestatus = 'Ready'
// onload fun
window.onload = function(){
  document.addEventListener("keydown",inputcontrol);
    game=setInterval(mainfun,200);
}


// main fun
function mainfun(){
  
     sposx +=nposx;
     sposy +=nposy;
     // disply score
     document.getElementById('c_score').innerHTML =c_score;
     document.getElementById('c_status').innerHTML =gamestatus;
     
 // main ground
    canv.fillStyle = 'black';
    canv.fillRect(0,0,400,400);
    
  //column grid
   for (var cl=0;cl<=400;cl += 20) {
    canv.moveTo(cl, 0);
    canv.lineTo(cl, 400);
   }
   
  //row grid
    for (var rl=0;rl<=400;rl += 20) {
    canv.moveTo(0, rl);
    canv.lineTo(400, rl);
    }
    
    canv.strokeStyle = 'gray';

    canv.stroke();
    
    // snake
    canv.fillStyle = 'lightblue'
    
    for (var i =0 ;i<snake.length;i++){
      canv.fillRect(snake[i].x,snake[i].y,20,20)
      
      if(sposx==snake[i].x && sposy==snake[i].y && snakesize>1){
        clearInterval(game)
        gamestatus = "Game over"
   
        document.getElementById('c_status').innerHTML =gamestatus;
        document.getElementById('c_status').style.color ='red'
      }
    }
    
    //fruit
    canv.fillStyle = 'red'
    canv.fillRect(fposx,fposy,20,20)
   
    //snake move
    if (sposx > 400){
      sposx = 0;
    }
    if (sposx < 0){
      sposx = 400;
    }
    if (sposy < 0){
      sposy = 400;
    }
    if (sposy > 400){
      sposy = 0;
    }
     //fruitmove snake bite
     if (sposx ==fposx && sposy==fposy){
      snakesize++;
      fposx  = Math.floor( Math.random()*20)*20;
      
      fposy = Math.floor( Math.random()*20)*20;  
      c_score +=10;
    }
    snake.push({x:sposx,y:sposy});
    while(snake.length>snakesize){
      snake.shift();
    }
}
 

// controll fun
function inputcontrol(e){
console.log(e.keyCode);
console.log(e.key );
//up
 if (e.keyCode ==38 ){
  nposy -= 20;
  nposx = 0;
 }//down
 if(e.keyCode ==40){
  nposy += 20;
  nposx = 0;

 }//right
 if(e.keyCode ==39 ){
   nposx += 20;
  nposy = 0;

 }//left
  if(e.keyCode ==37){
    nposx -= 20;
    nposy = 0;

 }
if(e.keyCode ==39||e.keyCode ==37||e.keyCode ==38||e.keyCode ==40 && document.getElementById('c_status').innerHTML !='Game over'){
  gamestatus = "Game started"
  document.getElementById('c_status').innerHTML =gamestatus;
  
}

}