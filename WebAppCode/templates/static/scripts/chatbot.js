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

function textSpeech() {
    if (recognizing) {
      recognition.stop();
      return;
    }
    final_transcript = '';
    recognition.start();
    final_span.innerHTML = '';
    interim_span.innerHTML = '';
    }

var final_transcript = '';
var recognizing = false;
var recognition = new webkitSpeechRecognition();
recognition.continuous = true;
recognition.interimResults = true;
recognition.onstart = function() {
recognizing = true;
};
recognition.onend = function() {
  recognizing = false;
  if (window.getSelection) {
    window.getSelection().removeAllRanges();
    var range = document.createRange();
    range.selectNode(document.getElementById('final_span'));
    window.getSelection().addRange(range);
  }
};
recognition.onresult = function(event) {
  var interim_transcript = '';
  for (var i = event.resultIndex; i < event.results.length; ++i) {
    if (event.results[i].isFinal) {
      final_transcript += event.results[i][0].transcript;
    } else {
      interim_transcript += event.results[i][0].transcript;
    }
  }
  final_transcript = capitalize(final_transcript);
  final_span.innerHTML = linebreak(final_transcript);
  interim_span.innerHTML = linebreak(interim_transcript);
};

var two_line = /\n\n/g;
var one_line = /\n/g;
function linebreak(s) {
return s.replace(two_line, '<p></p>').replace(one_line, '<br>');
}
var first_char = /\S/;
function capitalize(s) {
return s.replace(first_char, function(m) { return m.toUpperCase(); });
}