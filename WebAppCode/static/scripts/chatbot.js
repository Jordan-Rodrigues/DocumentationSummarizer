$(document).ready(function () {
  $(this).scrollTop(0);
});

$("#inputMessage").keypress(function (event) {
  if (event.which == 13) {
    var truth = userSend()
    chatScroll()
    if (truth) {
    setTimeout(robotSend, 2000)
    setTimeout(chatScroll, 2000)
    }
  }
});

$(".sendButton").click(function () {
  var truth = userSend()
  chatScroll()
  if (truth) {
  setTimeout(robotSend, 2000)
  setTimeout(chatScroll, 2000)
  }
})

$("#target").submit(function (e) {
  e.preventDefault()
  return false;
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
      return true;
  }
  else {
    return false;
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
    $(".input").val('')
}


//This section controls the Mic option. IMPORTANT: If you don't speak into the mic after calling, it breaks everything.
function textSpeech() {
  if (recognizing) {
    recognition.stop();
    return;
  }
  final_transcript = '';
  recognition.start();
  $("#inputMessage").val("   Feel free to speak. ROKBot is listening!")
}

var final_transcript = '';
var recognizing = false;
var recognition = new webkitSpeechRecognition();
recognition.onstart = function () {
  recognizing = true;
};

recognition.onresult = function (event) {
    for (var i = event.resultIndex; i < event.results.length; ++i) {
      final_transcript += event.results[i][0].transcript;
      final_transcript = capitalize(final_transcript);
      $("#inputMessage").val(final_transcript)
      final_transcript = ''
      $('.sendButton').trigger('click');
      recognizing = false;
      $("#inputMessage").val("")
    };

    /** Functions to do line breaks */
    var two_line = /\n\n/g;
    var one_line = /\n/g;

    function linebreak(s) {
      return s.replace(two_line, '<p></p>').replace(one_line, '<br>');
    }
    var first_char = /\S/;

    function capitalize(s) {
      return s.replace(first_char, function (m) {
        return m.toUpperCase();
      });
    }

  }
