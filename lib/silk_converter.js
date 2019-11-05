var binary = require('node-pre-gyp');
var path = require('path');
var binding_path = binary.find(path.resolve(path.join(__dirname,'../package.json')));
var binding = require(binding_path);
var silk_converter = module.exports = exports = binding;
var EventEmitter = require('events').EventEmitter;
