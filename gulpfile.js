'use strict';

var gulp = require('gulp');
var gutil = require('gulp-util');
var compass = require('gulp-compass');
var scsslint = require('gulp-scss-lint');
var jshint = require('gulp-jshint');
var minify = require('gulp-minify');
var shell = require('gulp-shell');
var connect = require('gulp-connect');

var theme = './awesomeconference_theme/';

var paths = {
    'css': '' + theme + 'static/css/',
    'js': '' + theme + 'js/',
    'sass': '' + theme + 'sass/',
    'templates': '' + theme + 'templates/',
    'settings': './settings/',
    'content': './content/',
};

var patterns = {
    'sass': [
        paths.sass + '*.scss',
        paths.sass + '_*.scss',
        paths.sass + '**/*.scss'
    ],
    'js': [
        paths.js + '*.js',
        paths.js + '**/*.js',
        '!' + paths.js + '*.min.js',
        '!' + paths.js + '**/*.min.js'
    ],
    'css': [
        paths.css + 'screen.css'
    ],
    'pelican': [
        paths.templates + '*.html',
        paths.templates + '**/*.html',
        paths.content + '*.rst',
        paths.content + '**/*.rst',
        paths.settings + '*.py',
    ]
};

gulp.task('jslint', function() {
    gulp.src(patterns.js)
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

gulp.task('pelican', shell.task([
    'pelican'
]));

gulp.task('jscompress', function() {
    gulp.src(patterns.js)
        .pipe(minify({
            noSource: true,
            mangle: true
        }))
        .pipe(gulp.dest('' + theme + 'static/js/'))
});

gulp.task('scsslint', function() {
    gulp.src(patterns.sass)
        .pipe(scsslint({
            'config': '' + theme + 'scss-lint.yml',
        }))
        .on('error', function(error) {
            gutil.log(error);
        });
});

gulp.task('compass', function() {
    gulp.src(patterns.sass)
        .pipe(compass({
            style: 'compressed',
            comments: false,
            sourcemap:true,
            force: true,
            css: paths.css,
            sass: paths.sass
        }))
        .on('error', function(error) {
            gutil.log(error);
        });
});

gulp.task('watch', function() {
    gulp.start('jslint');
    gulp.start('scsslint');
    gulp.start('jscompress');
    gulp.start('compass');
    gulp.start('pelican');

    gulp.watch(patterns.js, ['jslint']);
    gulp.watch(patterns.js, ['jscompress']);
    gulp.watch(patterns.js, ['pelican']);
    gulp.watch(patterns.pelican, ['pelican']);
    gulp.watch(patterns.css, ['pelican']);
    gulp.watch(patterns.sass, ['scsslint']);
    gulp.watch(patterns.sass, ['compass']);
});

gulp.task('connect', function() {
    connect.server({
        root: 'output',
        livereload: true
    });
});

gulp.task('default', ['connect', 'watch']);
