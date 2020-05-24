/**
 * When passed a string, Glob will attempt to find each file that matches the
 * path given and return each path to the file as string[]
 */
let  glob = require('glob');
let  autoprefixer = require('autoprefixer');
/**
 * The Path API will be used to get the absolute path to the directory where we
 * plan to run Webpack
 */
let MiniCssExtractPlugin = require('mini-css-extract-plugin');
let  path = require('path');

let  webpack = require('webpack');

let BundleTracker = require('webpack-bundle-tracker');

let postcssPresetEnv = require('postcss-preset-env');

let  WebpackNotifierPlugin = require('webpack-notifier');


let compiled_subtring = "compiled";
const exception_list = ['js', 'javascript', 'script', 'css', 'sass', 'scss', 'static'];
let entries = glob.sync(`./*/static/*/*js/!(*${compiled_subtring}*).js`).reduce((acc, relative_path) => {
  /**
   * The "[name]" placeholder in the "output" property will be replaced
   * with each key name in our "entry" object. We need to make sure the
   * keys are a path to the "index.js" file but without the actual file
   * name. This is why we replace the file name, "index.js", with a string
   */
  const file_name = path.basename(relative_path);
  let directorysplit = relative_path.split('/');
  directorysplit = directorysplit.map(v => v.toLowerCase());

  directorysplit = directorysplit.filter(function (item, pos) {
    return (directorysplit.indexOf(item) === pos) && !exception_list.includes(item);
  })
  directory_string = directorysplit.join('/');
  let entry = directory_string.replace(`/${file_name}`, `/compiled_${file_name}`);
  entry = entry.replace('.js', '');
  /**
   * Here we start building our object by placing the "entry" variable from
   * the previous line as a key and the entire path including the file name
   * as the value
   */
  acc[entry] = relative_path
  return acc
}, {});

entries = glob.sync(`./*/static/*js/!(*${compiled_subtring}*).js`).reduce((acc, relative_path) => {
  /**
   * The "[name]" placeholder in the "output" property will be replaced
   * with each key name in our "entry" object. We need to make sure the
   * keys are a path to the "index.js" file but without the actual file
   * name. This is why we replace the file name, "index.js", with a string
   */

  const file_name = path.basename(relative_path);
  let directorysplit = relative_path.split('/');
  directorysplit = directorysplit.map(v => v.toLowerCase());

  directorysplit = directorysplit.filter(function (item, pos) {
    return (directorysplit.indexOf(item) === pos) && !exception_list.includes(item);
  })
  directory_string = directorysplit.join('/');
  let entry = directory_string.replace(`/${file_name}`, `/compiled_${file_name}`);
  entry = entry.replace('.js', '');
  /**
   * Here we start building our object by placing the "entry" variable from
   * the previous line as a key and the entire path including the file name
   * as the value
   */
  acc[entry] = relative_path
  return acc
}, entries);

const jsRule = {
  test: /\.js$/,
  loader: 'babel-loader',
  include: path.resolve('./static/src/js'),
  exclude: /node_modules/
};

let plugins = [
  new BundleTracker({
    filename: './webpack-stats.json',
    relativePath: true,


  }),
  new MiniCssExtractPlugin({
    filename: '[name].bundle.css'
  }),
  new WebpackNotifierPlugin({title: 'Webpack'})
]

const styleRule = {
  test: /\.(sa|sc|c)ss$/,
  use: [
    MiniCssExtractPlugin.loader,
    { loader: 'css-loader', options: { sourceMap: true } },
    { loader: 'postcss-loader', options: { sourceMap: true, plugins: () => 
      [
        autoprefixer({ browsers: ['last 2 versions'] }),
        postcssPresetEnv({browsers:['last 2 versions']}),
      
      ] } },
    { loader: 'resolve-url-loader', options: { sourceMap: true } },
    { loader: 'sass-loader', options: { sourceMap: true } }
  ],
  exclude: /node_modules/
};
module.exports = {
  mode: 'development',
  context: __dirname,
  entry: entries,
  devtool: 'source-map',
  output: {
    path: path.resolve('./assets/webpack_bundle/'),
    filename: (chunk_data) => {
      return "[name].js";
    }
  },
  module: {
    rules: [
      jsRule, styleRule
    ],
  },

  plugins: plugins
}