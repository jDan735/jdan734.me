const { src, dest, parallel } = require('gulp')

const pug = require("gulp-pug")
const sass = require("gulp-sass")
const watch = require("gulp-watch")
const csscomb = require("gulp-csscomb")

function html(){
    return watch('./pug/*.pug', () => {
        return src('./pug/*.pug')
               .pipe(pug({pretty: true}))
               .pipe(dest('./'))
    })
}

function css(){
    return watch('./sass/*.sass', () => {
        return src('./sass/*.sass')
               .pipe(sass())
               .pipe(csscomb())
               .pipe(dest('./css'))
    })
}

exports.default = parallel(html, css)
