const express = require("express");
const router = express.Router();
const fs = require("fs");
const execShellCommand = require("./util.js");

let list = [];
let returnArray = [];

router.get("/", (req, res) => {
  res.render('pages/index', {list:list ,returnList:returnArray, check: false});
});


async function runScript()
{
  let x = await execShellCommand("python3 second.py");
  console.log(1);
 
  return x;
}

router.post("/automate", async(req, res) => {
  return res.status(200).send({list: list,returnList: returnArray, check:false})
})

router.post("/artikli", async(req, res) => {

    let tab = JSON.parse(req.body.table);
    returnArray = tab;
    console.log(tab);
    
    const returnList = list[list.length-1].filter((el) => {
      return !tab.some((f) => {
        if(f === null) return false;
        return f.title === el.title;
      });
    });
    

    list[list.length-1] = returnList;
    return res.status(200).send({list: returnList, returnList: returnArray ,check: true});

})


router.get("/artikli", async (req, res) => {
  console.log("=> /Artikli");
 // let y = await runScript(); 
 // if(y)
 // {
      fs.readFile("test.json", "utf8", (err, data) => {
        console.log(2)
        if (err) throw err;
        let art = JSON.parse(data);

        list.push(art);
      });
  // }

  res.send({list:list,returnList:returnArray ,check: true});
});

module.exports = router;
