const request = require("request");
const express = require('express');
const router = express.Router();
var fs = require('fs');



router.post('/', function(req, res) {

  var melon = fs.readFileSync('/Users/bonghayun/Desktop/project/js/real_time_kakao/python/data/melon.json', 'utf8')

  function removeByteOrderMark(str){
    return str.replace(/^\ufeff/g,"")
  }

  melon = removeByteOrderMark(melon)

  var melonList = JSON.parse(melon);
  console.log(melonList[0])

  var sendText ="[멜론 인기 차트]\n"

  melonList.map(data => {
    sendText = sendText + +data[0] +"위 " + data[2] + " by "+ data[1] + "\n\n"
  })

	var responseBody = {
    version: "2.0",
    template: {
      outputs: [
      {
        simpleText: {text : sendText}
      }
      ]
    }
  };
	
	res.status(200).send(responseBody);	

	
});

module.exports = router;

