const express = require('express');
const app = express();
const mongoose =require('mongoose');
const bodyParser=require('body-parser');
const cors = require('cors');
require('dotenv/config');

app.use(bodyParser.json());
/*Middlewares
app.use('/posts',()=>{
    console.log('This is middleware running');
});
*/
app.use(cors());
app.use(bodyParser.json());
//Import Routes
const postsRoute = require('./routes/posts');
app.use('/posts',postsRoute);


//ROUTES
app.get('/',(req,res) =>{
    res.send('we are on home');
});
/*
app.get('/posts',(req,res) =>{
    res.send('we are on posts');
});
*/
//Connect to DB
mongoose.connect(
    process.env.DB_CONNECTION,
    { useNewUrlParser: true, useUnifiedTopology: true },
    ()=>
    console.log('Connected to DB!')
);
//How to start listening to server
app.listen(3000);