import Vue from 'vue'
import BotUI from 'botui'

console.log("test")
var botui = new BotUI('my-botui-app');

botui.message.add({
    content: 'Hello from bot.'
  });