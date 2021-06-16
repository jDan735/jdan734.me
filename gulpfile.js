const { src, dest, parallel } = require('gulp')

const sass = require("gulp-sass")
const watch = require("gulp-watch")
const cssmin = require("gulp-cssmin")
const prefixer = require("gulp-autoprefixer")

function css(){
    return src('./scss/style.scss')
           .pipe(sass())
		   .pipe(prefixer())
           .pipe(cssmin())
           .pipe(dest('./css'))
}

exports.default = css
