const { src, dest, parallel } = require('gulp')

const sass = require("gulp-sass")
const watch = require("gulp-watch")

function css(){
    return watch('./scss/**/*.scss', () => {
        return src('./scss/*.scss')
               .pipe(sass())
               .pipe(dest('./static/css'))
    })
}

exports.default = css
