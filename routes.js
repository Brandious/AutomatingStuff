const express = require('express');
const router = express.Router();
const fs = require('fs');

router.get('/', (req, res) => {
    res.render('index');
})

let list = [];
router.get('/artikli',   (req, res) => {
    
  
  const {spawn} = require('child_process');
    const pyProg = spawn('python', ['./second.py']);
    console.log(pyProg);

   fs.readFile('test.json', 'utf8', (err, data) => { 
        if(err) throw err;
        console.log(typeof(data))
        let art = JSON.parse(data);
        list.push(art);
        //res.send(data);
    })

     res.render('index', { list });

})

module.exports = router;
