/**
 * When passed a string, Glob will attempt to find each file that matches the
 * path given and return each path to the file as string[]
 */
const glob = require('glob');

/**
 * The Path API will be used to get the absolute path to the directory where we
 * plan to run Webpack
 */
const path = require('path');

var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

let compiled_subtring = "compiled";
let entries = glob.sync(`./*/static/*/*js/!(*${compiled_subtring}*).js`).reduce((acc, relative_path) => {
    /**
     * The "[name]" placeholder in the "output" property will be replaced
     * with each key name in our "entry" object. We need to make sure the
     * keys are a path to the "index.js" file but without the actual file
     * name. This is why we replace the file name, "index.js", with a string
     */
    const file_name = path.basename(relative_path);
    let directorysplit= relative_path.split('/');
    directorysplit = directorysplit.map(v => v.toLowerCase());
  
    directorysplit= directorysplit.filter(function(item, pos) {
        return (directorysplit.indexOf(item) === pos) && item !=="static";
    })
    directory_string = directorysplit.join('/');
    let  entry = directory_string.replace(`/${file_name}`, `/compiled_${file_name}`);
    entry = entry.replace('.js', '');
    /**
     * Here we start building our object by placing the "entry" variable from
     * the previous line as a key and the entire path including the file name
     * as the value
     */
    acc[entry] = relative_path
    return acc
},{});
console.log(entries);
 entries = glob.sync(`./*/static/*js/!(*${compiled_subtring}*).js`).reduce((acc, relative_path) => {
    /**
     * The "[name]" placeholder in the "output" property will be replaced
     * with each key name in our "entry" object. We need to make sure the
     * keys are a path to the "index.js" file but without the actual file
     * name. This is why we replace the file name, "index.js", with a string
     */
    
    const file_name = path.basename(relative_path);
    let directorysplit= relative_path.split('/');
    directorysplit = directorysplit.map(v => v.toLowerCase());
  
    directorysplit= directorysplit.filter(function(item, pos) {
        return (directorysplit.indexOf(item) === pos) && item !=="static";
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

console.log(entries);

// module.exports = {
//     context: __dirname,
//     entry: entries,
//     output: {
//         path: path.resolve(__dirname),
//         filename: "[name]"
//     },
  
//     plugins: [
//       new BundleTracker({filename: './webpack-stats.json'})
//     ]
//   }