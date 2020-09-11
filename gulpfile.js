const { src, dest, parallel, task } = require('gulp')

const pug = require("gulp-pug")
const sass = require("gulp-sass")
const watch = require("gulp-watch")
// const csscomb = require("gulp-csscomb")

/* Watchers */

function html(){
    return watch('./pug/*.pug', () => {
        return src('./pug/*.pug')
               .pipe(pug())
               .pipe(dest('./'))
    })
}

function css(){
    return watch('./sass/*.sass', () => {
        return src('./sass/*.sass')
               .pipe(sass())
               .pipe(dest('./css'))
    })
}

task("sass", () => {
    return src('./sass/*.sass')
           .pipe(sass())
//           .pipe(csscomb())
           .pipe(dest('./css'))
})

task("pug", () => {
    return src('./pug/*.pug')
           .pipe(pug())
           .pipe(dest('./'))
})

exports.default = parallel(html, css)
