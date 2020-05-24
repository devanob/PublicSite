var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: './About/static/js/about.js',
  output: {
      path: path.resolve(__dirname),
      filename: "[name]"
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ]
}