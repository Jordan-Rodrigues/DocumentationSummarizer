function nameFade() {
  console.log("test")
  $(".name").hide().fadeIn(2500)

  $(".bold").animate()
}

$(document).ready(nameFade())
