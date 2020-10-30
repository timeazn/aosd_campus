var points = 0;
var rerolls = 5;
var cur_word = "NONE"
var cur_category = "";
var cur_level = "";

var dictionary = {
  "animals": {
    0: ["bee", "cat", "sea urchin", "bird", "fish", "butterfly", "snake", "sea urchin", "turtle"],
    1: ["elephant", "chicken", "giraffe", "bear", "sheep", "penguin", "octopus", "turtle"],
    2: ["alligator", "zebra", "walrus", "monkey", "hippopotamus", "whale", "shark", "bull"],
  },
  "house": {
    0: ["pencil", "balloon", "phone", "book", "bottle", "cup", "can", "hat", "plate"],
    1: ["shirt", "sweater", "chair", "table", "fan", "shoes", "wallet", "TV", "window"],
    2: ["coaster", "thermostat", "backpack", "bed", "rooftop", "makeup palette", "floss"],
  },
  "food": {
    0: ["ice cream", "pizza", "chicken", "bread", "donut", "watermelon", "eggs", "lollipop"],
    1: ["tacos", "burritos", "steak", "rice", "cereal", "hotdog", "pie", "candycorn", "soda", "apple"],
    2: ["spaghetti", "coffee", "burger", "french fries", "cinnamon roll", "hummus", "pancakes"],
  },
  "surprise": {
    0: ["sad", "light bulb", "clock", "shorts", "heart", "star", "anger", "paperclip"],
    1: ["dress", "music", "sword", "hammer", "mountains", "pokeball", "yin yang"],
    2: ["binary", "america", "river", "gummybear", "storm", "tornado", "airplane", "grave"],
  },
}

function randomIntFromInterval(min, max) { // min and max included
  return Math.floor(Math.random() * (max - min + 1) + min);
}

function render(){
  $("#points_obj").text(points);
  $("#rerolls_obj").text(rerolls);
  $("#word").text(cur_word.toUpperCase());
}

function setWord(category, level){
  if(dictionary[category][level].length > 0){
    var rand_idx = randomIntFromInterval(0, dictionary[category][level].length-1);
    cur_word = dictionary[category][level][rand_idx];
    dictionary[category][level].splice(rand_idx, 1);
    if(dictionary[category][level].length == 0){
      $("#" + category + "_" + level).hide();
    }
    $("#guess").show()
  }
  render()
}

//doc ready
$(document).ready(function(){

  //on click
  $(".roll").click(function(){
    if ($("#guess").is(":hidden")){
      var this_id = $(this).prop("id").split("_");
      cur_category = this_id[0];
      cur_level = this_id[1];
      setWord(cur_category, cur_level);
    }
  });
  $("#reroll_btn, #already_btn").click(function(){
    if(cur_category != "" && cur_level != ""){
      if(dictionary[cur_category][cur_level].length > 0){
        if($(this).prop("id") != "already_btn"){
          rerolls--;
        }
        setWord(cur_category, cur_level);
      }
    }
  });
  $("#yes").click(function(){
    points += (parseInt(cur_level) + 1)*100;
    $("#guess").hide()
    render();
  });
  $("#nope").click(function(){
    $("#guess").hide()
    render();
  });

  //init
  $("#guess").hide();
  render();

});
