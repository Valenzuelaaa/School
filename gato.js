var bandera = false; 
var turno = 0;
var tab = new Array();

window.onload=function(){
var iniciar = document.getElementById("iniciar");
iniciar.addEventListener("click", comenzar);


}
function comenzar(){

bandera = true;
var jugador1= document.getElementById("jugador1");
var jugador2= document.getElementById("jugador2");
if(jugador1.value==""){

alert("Ingresa nombre del Jugador 1");
jugador1.focus();

        }
else{

if (jugador2.value=="") {
    
    alert("Ingresa nombre del Jugador 2");
jugador2.focus();
}else{

tab[0] = document.getElementById("Btn0");
tab[1] = document.getElementById("Btn1");
tab[2] = document.getElementById("Btn2");
tab[3] = document.getElementById("Btn3");
tab[4] = document.getElementById("Btn4");
tab[5] = document.getElementById("Btn5");
tab[6] = document.getElementById("Btn6");
tab[7] = document.getElementById("Btn7");
tab[8] = document.getElementById("Btn8");
for(var i=0; i<9; i++){

tab[i].className = "botonInicial";
tab[i].value = "I";

}
turno= 1;
document.getElementById("turnoJugador").innerHTML ="Adelante Jugador " + jugador1.value;
             }

         }

  }

function colocar(boton){
if(bandera==true){
if(turno==1 && boton.value== "I")
{ 
turno = 2;
document.getElementById("turnoJugador").innerHTML = "Adelante Jugador" + jugador2.value;
boton.value = "X";
boton.className = "botonJugador1";

         }else{
               if(turno==2 && boton.value== "I"){
                turno = 1;
                document.getElementById("turnoJugador").innerHTML = "Adelante Jugador" + jugador1.value; 
                boton.value = "O";
                boton.className = "botonJugador2";


               }
      

         }
  
     }
revisar();





} 

function revisar(){
if ((tab[0].value =="X" && tab[1].value=="X" && tab[2].value=="X")

||(tab[3].value =="X" && tab[4].value=="X" && tab[5].value=="X")
||(tab[6].value =="X" && tab[7].value=="X" && tab[8].value=="X")
||(tab[0].value =="X" && tab[3].value=="X" && tab[6].value=="X")
||(tab[1].value =="X" && tab[4].value=="X" && tab[7].value=="X")
||(tab[2].value =="X" && tab[5].value=="X" && tab[8].value=="X")
||(tab[0].value =="X" && tab[4].value=="X" && tab[8].value=="X")
||(tab[2].value =="X" && tab[4].value=="X" && tab[6].value=="X")




) {
alert("Felicidades ganaste Jugador " + jugador1.value);
bandera=false;

}
if ((tab[0].value =="O" && tab[1].value=="O" && tab[2].value=="O")

||(tab[3].value =="O" && tab[4].value=="O" && tab[5].value=="O")
||(tab[6].value =="O" && tab[7].value=="O" && tab[8].value=="O")
||(tab[0].value =="O" && tab[3].value=="O" && tab[6].value=="O")
||(tab[1].value =="O" && tab[4].value=="O" && tab[7].value=="O")
||(tab[2].value =="O" && tab[5].value=="O" && tab[8].value=="O")
||(tab[0].value =="O" && tab[4].value=="O" && tab[8].value=="O")
||(tab[2].value =="O" && tab[4].value=="O" && tab[6].value=="O")




) {
alert("Felicidades ganaste Jugador " + jugador2.value);
bandera=false;

}


}