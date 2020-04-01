const express = require("express");
const router = express.Router();
const fs = require("fs");
const execShellCommand = require("./util.js");

let list = [];

router.get("/", (req, res) => {
  res.render('pages/index', {list});
});


async function runScript()
{
  let x = await execShellCommand("python3 second.py");
  console.log(1);
 
  return x;
}

router.post("/artikli", async(req, res) => {

    let tab = JSON.parse(req.body.table);

    console.log(tab);

    const returnList = list[list.length-1].filter((el) => {
      return !tab.some((f) => {
        if(f === null) return false;
        return f.title === el.title;
      });
    });
    

    list[list.length-1] = returnList;
    return res.status(200).send({list: returnList});

})


router.get("/artikli", async (req, res) => {
  console.log("=> /Artikli");
  let y = await runScript(); 
  if(y)
  {
      fs.readFile("test.json", "utf8", (err, data) => {
        console.log(2)
        if (err) throw err;
        let art = JSON.parse(data);

        list.push(art);
      });
   }

  res.send(list);
});

module.exports = router;
