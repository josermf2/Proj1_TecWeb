function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }

  let deletedCards = document.getElementsByClassName("deleted-card");
  for (let i = 0; i < deletedCards.length; i++) {
    let deletedCard = deletedCards[i];
    deletedCard.className += ` card-color-${getRandomInt(
      1,
      5
    )}`;
  }
});

var modal = document.getElementById("modal");
var allBtns = document.getElementsByClassName("edit-button");
var spans = document.getElementsByClassName("close");

var modal_title = document.getElementById("modal-title");
var modal_content = document.getElementById("modal-content");

var update_button = document.getElementById("update-button");
let id = "";

for(let i=0;i<allBtns.length;i++){
  allBtns[i].onclick = function() {
    modal_title.innerHTML = allBtns[i].value.split("|")[1];
    modal_content.innerHTML = allBtns[i].value.split("|")[2];
    modal.style.display = "block";
    id = allBtns[i].value.split("|")[0];
  }
}

update_button.addEventListener('click', ()=>{
  update_button.setAttribute("value", "id=" + id + "&title=" + modal_title.value + "&details=" + modal_content.value);
});    

for(let i=0;i<spans.length;i++){
   spans[i].onclick = function() {
    modal.style.display = "none";
   }
}

let xhr = new XMLHttpRequest();
console.log(xhr.responseText);

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
  document.body.style.backgroundColor = "white";
}
