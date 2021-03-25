//Longitud
var input = document.getElementById('input');
var result = document.getElementById('result');
var inputType = document.getElementById('inputType');
var resultType = document.getElementById('resultType');

var inputTypeValue, resultTypeValue;

input.addEventListener("keyup",myResult);
inputType.addEventListener("change",myResult);
resultType.addEventListener("change",myResult);

inputTypeValue = inputType.value;
resultTypeValue = resultType.value;


function myResult()
    {     
    inputTypeValue = inputType.value;
    resultTypeValue = resultType.value;

    if(inputTypeValue === "metros" && resultTypeValue === "centimetros")
{
    result.value = Number(input.value) *100;
    
}
else if (inputTypeValue ==="centimetros" && resultTypeValue === "centimetros")
{
    result.value = (input.value);
}
else if(inputTypeValue === "centimetros" && resultTypeValue ==="metros")
{
    result.value = Number(input.value) /100;
}

else if(inputTypeValue === "metros" && resultTypeValue ==="metros")
{
    result.value = (input.value);
}
    }


//temperatura
var input2 = document.getElementById('input2');
var result2 = document.getElementById('result2');
var inputType2 = document.getElementById('inputType2');
var resultType2 = document.getElementById('resultType2');

var inputTypeValue2, resultTypeValue2;

input2.addEventListener("keyup",myResult2);
inputType2.addEventListener("change",myResult2);
resultType2.addEventListener("change",myResult2);

inputTypeValue2 = inputType2.value;
resultTypeValue2 = resultType2.value;


function myResult2()
    {     
    inputTypeValue2 = inputType2.value;
    resultTypeValue2 = resultType2.value;

    if(inputTypeValue2 === "celsius" && resultTypeValue2 === "fahrenheit")
{
    result2.value = Number(input2.value ) * 1.8  + 32;
    
}
else if (inputTypeValue2 ==="celsius" && resultTypeValue2 === "celsius")
{
    result2.value = (input2.value);
}
else if(inputTypeValue2 === "fahrenheit" && resultTypeValue2 ==="fahrenheit")
{
    result2.value = (input2.value);
}

else if(inputTypeValue2 === "fahrenheit" && resultTypeValue2 ==="celsius")
{
    result2.value = Number(input2.value -32)  * 0.55555555555;
}
    }
