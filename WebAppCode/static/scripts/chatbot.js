$(document).ready(function () {
  $(this).scrollTop(0);
});

$("#inputMessage").keypress(function (event) {
  if (event.which == 13) {
    userSend()
    chatScroll()
    setTimeout(robotSend, 2000)
    setTimeout(chatScroll, 2000)
  }
});

$(".sendButton").click(function () {
  userSend()
  chatScroll()
  setTimeout(robotSend, 2000)
  setTimeout(chatScroll, 2000)
})

$("#Target").submit(function (e) {
  e.preventDefault()
})


function userSend() {
  if ($(".input").val() != "") {
      $(' <div class="userSection"> ' +
      '<div class="userBubble">' +
      '<h5 class="userMessage">' + $(".input").val() + '</h5>' +
      '</div>' +
      '<img class="userIcon" src="static/css/Images/person.png">' +
      '<hr class="chatBreaker">' +
      '</div>').hide().appendTo(".chatMed").fadeIn(1500)
    $(".input").val('')
  }
}

function chatScroll() {
  $(".chatMed").scrollTop($(this).height())
}

function robotSend() {
  $(' <div class="botSection"> ' + '<img class="botIcon" src="static/css/Images/robot4.png">' +
  '<div class="botBubble">' +
  '<h5 class="botMessage">' + "Sorry I can't help you with that at this moment." + '</h5>' +
  '</div>' +
  '<hr class="chatBreaker">' +
  '</div>').hide().appendTo(".chatMed").fadeIn(1500)
}