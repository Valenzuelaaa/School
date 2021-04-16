function Astring(){

    var json = '{"quoteText": "Let us be grateful to people who make us happy; they are the charming gardeners who make our souls blossom.", "quoteAuthor" : "Marcel Proust" , "senderName" : "-" , "senderLink" : "-" , "quoteLink" :"http://forismatic.com/en/3fe08c5b2e/"}';
    var obj = JSON.parse(json);
        console.log(obj);

        document.querySelector("#res").value = obj.quoteText +  " " +  obj.quoteAuthor + " " + obj.senderName + " " + obj.senderLink + " " + obj.quoteLink;
    
    
  }

  document.querySelector("#btnconsulta").addEventListener("click",Astring);

 