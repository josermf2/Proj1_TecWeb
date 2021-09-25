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
})

window.onload = function() {
  try{
    var modal = document.getElementById("modal");
    var allBtns = document.getElementsByClassName("edit-button");
    var spans = document.getElementsByClassName("close");
  
    var modal_title = document.getElementById("modal-title");
    var modal_content = document.getElementById("modal-content");
    var modal_tag = document.getElementById("modal-tag");
  
    var update_button = document.getElementById("update-button");
    let id = "";
    
    modal_title.innerHTML = "";
    modal_content.innerHTML = "";
    modal_tag.innerHTML = "";
  
    for(let i=0;i<allBtns.length;i++){
      allBtns[i].onclick = function() {
        console.log(allBtns[i].value.split("|")[1])
        modal_title.innerHTML = allBtns[i].value.split("|")[1];
        modal_content.innerHTML = allBtns[i].value.split("|")[2];
        modal_tag.innerHTML = allBtns[i].value.split("|")[3];
        modal.style.display = "block";
        id = allBtns[i].value.split("|")[0];
      }
    }
  
    update_button.addEventListener('click', ()=>{
      update_button.formAction = "update/"+id+"/"+modal_title.value+"/"+modal_content.value+"/"+modal_tag.value;
    });
  
    for(let i=0;i<spans.length;i++){
      spans[i].onclick = function() {
        modal.style.display = "none";
      }
    }
  }
  catch (e){
  }
    
  try{
    var tag_button = document.getElementsByClassName("tag-button")

    for(let i=0;i<tag_button.length;i++){
      tag_button[i].onclick = function() {
        tag_button[i].formAction = "specific_tag/"+tag_button[i].innerHTML.toString();
      }
    }
  }
  catch (e){
  }  
};