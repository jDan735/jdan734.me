const { src, dest, parallel, task } = require('gulp')

const pug = require("gulp-pug")
const sass = require("gulp-sass")
const watch = require("gulp-watch")
const csso = require("gulp-csso")
// const csscomb = require("gulp-csscomb")

/* Watchers */

function html(){
    return watch('./dev/pug/*.pug', () => {
        return src('./dev/pug/*.pug')
               .pipe(pug())
               .pipe(dest('./'))
    })
}

function css(){
    return watch('./dev/sass/*.sass', () => {
        return src('./dev/sass/*.sass')
               .pipe(sass())
               .pipe(csso())
               .pipe(dest('./static/css'))
    })
}

exports.default = parallel(html, css)
