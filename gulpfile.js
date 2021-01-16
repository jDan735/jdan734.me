const { src, dest, parallel } = require('gulp')

const sass = require("gulp-sass")
const watch = require("gulp-watch")

function css(){
    return src('./scss/style.scss')
           .pipe(sass())
           .pipe(dest('./static/css'))
}

exports.default = css
