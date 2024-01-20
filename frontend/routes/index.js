var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'NFT SEASONS' });
});


router.get('/register', function(req, res, next){
  res.render('register')
});

router.get('/login', function(req, res, next){
  res.render('login')
});

router.get('/about', function(req, res, next) {
  res.render('about')
});

router.get('/productindividual', function(req, res, next){
  res.render('productindividual')
});

router.get('/basket', function(req, res, next){
  res.render('basket')
});

router.get('/checkout', function(req, res, next){
  res.render('checkout')
});

router.get('/order', function(req, res, next){
  res.render('order')
});

router.get('/contact', function(req, res, next){
  res.render('contact')
});

router.get('/footer', function(req, res, next) {
  res.render('footer')
});

router.get('/error', function(req, res, next) {
  res.render('error')
});


module.exports = router;
