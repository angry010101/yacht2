function call(n){
    $.post( "/write", { number: n })
  .done(function( data ) {
    document.getElementById("content_popup").innerHTML = "<div class='button_close' id='button_close' ><i class='fa fa-close' style='font-size:48px;color: #92a8af'></i></div><p class='montserrata popup_text'>Ожидайте 15 секунд</p>";


      let btn_close = document.getElementById("button_close");
      btn_close.addEventListener('click',popupHide,false);
  });
}