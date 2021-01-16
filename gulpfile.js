const { src, dest, parallel } = require('gulp')

const sass = require("gulp-sass")
const watch = require("gulp-watch")
const cssmin = require("gulp-cssmin")

function css(){
    return src('./scss/style.scss')
           .pipe(sass())
           .pipe(cssmin())
           .pipe(dest('./static/css'))
}

exports.default = css
