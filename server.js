const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
console.log('starting....');
const cors = require('cors');

app.use(cors());

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const port = 3000;


app.post('/postExample', (req, res) => {
    const data = req.body;
    res.json(data);
});

app.listen(port, ()=>{
    console.log('Server is listening at localhost')
})